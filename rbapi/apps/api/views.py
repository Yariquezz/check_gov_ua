from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from apps.api.models import RBAresponse
from apps.api.serializers import RBAresponseSerializer
import io
import json
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


class Aval(APIView):
    permissions_classes = IsCheckGov

    def loging(self, request, **kwargs):
        logfile = '/Users/yarique/PycharmProjects/my_check_gov/rbapi/api.log'
        with open(logfile, 'a', encoding='UTF-8') as log:
            l = ''
            if kwargs.get('message'):
                msg = str(kwargs.get('message'))
                rkvst = 'Request method: {} X-Time: {} X-Check-Id: {} X-Real_Ip: {} Request body: {}'.format(request.method, request.headers['X-Time'], request.headers['X-Check-Id'],request.headers['x-real-ip'], request.body)
                l = '{} {}'.format(rkvst, msg)
            else:
                l = 'Request method: {} X-Time: {} X-Check-Id: {} X-Real_Ip: {} Request body {}'.format(request.method,request.headers['X-Time'], request.headers['X-Check-Id'],request.headers['x-real-ip'], request.body)

            log.write('{}\n'.format(l))
            log.close()

    def get(self, request):
        if request.method == 'GET':
            try:
                x_time = request.headers['X-Time']
                x_check = request.headers['X-Check-Id']
                x_ip = request.headers['x-real-ip']
            except Exception as e:
                self.loging(request, message='Something goes wrong')
                return Response({'messsage': 'Something goes wrong'})
            else:
                try:
                    check = RBAresponse.objects.get(reciept_id=x_check)
                except ObjectDoesNotExist:
                    message = {'message': 'Check is not found'}
                    self.loging(request, message=message)
                    return Response(message, status=status.HTTP_404_NOT_FOUND)
                else:
                    serializer = RBAresponseSerializer(check)
                    message = '{}{}'.format({ "payments": [serializer.data], }, request.method)
                    self.loging(request, message=message)
                    return Response({ "payments": [serializer.data], })
        elif request.method == 'POST':
            message = {'messsage': 'POST method not supported!'}
            self.loging(request, message=message)
            return Response(status.HTTP_204_NO_CONTENT)


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
                     Paragraph('Receipient: {}'.format(serializer.data['recipient']), styleN),
                     Paragraph('Amount: {}'.format(serializer.data['amount'] / 100), styleN),
                     Paragraph('Description: {}'.format(serializer.data['description']), styleN),
                     Paragraph('Comission: {}'.format(serializer.data['comissionRate']), styleN)]
        # Draw things on the PDF. Here's where the PDF generation happens.
        canv = Canvas(buffer)
        canv.setFont("Times-Roman", 24)
        frm = Frame(inch, inch, 6*inch, 9*inch)
        frm.addFromList(cheq_body, canv)
        canv.save()
        # Close the PDF object cleanly, and we're done.
        buffer.seek(0)
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')
