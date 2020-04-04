from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from django.http import FileResponse
import io
from django.shortcuts import get_object_or_404
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts


class Cheq(APIView):

    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):

        MyFontObject = ttfonts.TTFont('Arial', '../rbapi/static/fonts/arial.ttf')
        pdfmetrics.registerFont(MyFontObject)

        obj = get_object_or_404(RBAresponse,link_code=kwargs.get('link_id'))
        serializer = RBAresponseSerializer(obj)

        buffer = io.BytesIO()
        # Create a file-like buffer to receive PDF data.
        styleSheet = getSampleStyleSheet()
        styleH = styleSheet['Heading1']
        styleN = styleSheet['Normal']
        styleB = styleSheet['BodyText']
        cheq_body = []
        cheq_body.append(Paragraph('Receipt # {}'.format(obj.reciept_id), styleH))
        cheq_body.append(Paragraph('Sender: {}'.format(serializer.data['sender']),styleB))
        cheq_body.append(Paragraph('Receipient: {}'.format(serializer.data['recipient']),styleN))
        cheq_body.append(Paragraph('Amount: {}'.format(serializer.data['amount']/100),styleN))
        cheq_body.append(Paragraph('Description: {}'.format(serializer.data['description']),styleN))
        cheq_body.append(Paragraph('Comission: {}'.format(serializer.data['comissionRate']),styleN))
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