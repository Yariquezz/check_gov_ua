from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import RBAresponse
from .serializers import RBAresponseSerializer
import io
from django.http import FileResponse
from reportlab.lib.units import inch
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from .permissions import IsCheckGov
from django.shortcuts import render
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


def index(request):
    now = timezone.now() + timezone.timedelta(hours=3)
    context = {
        'now': now,
    }
    logger.info('show api/index.html page with context {}'.format(context))
    return render(request, 'api/index.html', context)


class Enter(APIView):

    permissions_classes = IsCheckGov

    def get(self, request):

        try:
            x_check = request.headers['X-Check-Id']
        except Exception as err:
            logger.info(err)
            return Response(
                {
                    'message': 'Something goes wrong'
                }
            )
        else:
            try:
                check = RBAresponse.objects.get(reciept_id=x_check)
                self.check_object_permissions(request, check)
            except ObjectDoesNotExist:
                message = {
                    'message': 'Check is not found'
                }
                logger.info(message)
                return Response(message, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = RBAresponseSerializer(check)
                message = '{}{}'.format({"payments": [serializer.data], }, request.method)
                logger.info(message)
                return Response({"payments": [serializer.data], })


class Check:
    @api_view(['GET'])
    @permission_classes([AllowAny])
    def get_check(request, **kwargs):

        MyFontObject = ttfonts.TTFont('Arial', '../rbapi/static/fonts/arial.ttf')
        pdfmetrics.registerFont(MyFontObject)

        obj = get_object_or_404(RBAresponse, link_code=kwargs.get('link_id'))
        serializer = RBAresponseSerializer(obj)

        buffer = io.BytesIO()
        # Create a file-like buffer to receive PDF data.
        styleSheet = getSampleStyleSheet()
        styleH = styleSheet['Heading1']
        styleN = styleSheet['Normal']
        styleB = styleSheet['BodyText']
        cheq_body = [Paragraph('Receipt # {}'.format(obj.reciept_id), styleH),
                     Paragraph('Sender: {}'.format(serializer.data['sender']), styleB),
                     Paragraph('Recipient: {}'.format(serializer.data['recipient']), styleN),
                     Paragraph('Amount: {}'.format(serializer.data['amount'] / 100), styleN),
                     Paragraph('Description: {}'.format(serializer.data['description']), styleN),
                     Paragraph('Commission: {}'.format(serializer.data['commissionRate']), styleN)]
        # Draw things on the PDF. Here's where the PDF generation happens.
        canv = Canvas(buffer)
        canv.setFont("Times-Roman", 24)
        frm = Frame(inch, inch, 6 * inch, 9 * inch)
        frm.addFromList(cheq_body, canv)
        canv.save()
        # Close the PDF object cleanly, and we're done.
        buffer.seek(0)
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        logger.info('Return receipt: {}'.format(cheq_body))
        return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')
