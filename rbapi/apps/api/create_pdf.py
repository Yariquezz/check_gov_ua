import io
import logging
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase import ttfonts
from .serializers import RBAResponseSerializer
from .models import BankInfo

logger = logging.getLogger(__name__)


class CreateFile:

    @staticmethod
    def get_pdf(obj):
        # Get Receipt INFO from serializer

        serializer = RBAResponseSerializer(obj)
        bank_info = BankInfo.objects.get(tax_code=obj.sender_bank_tax_code.tax_code)

        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Draw things on the PDF. Here's where the PDF generation happens.

        # Register DejaVuSerif fonts which support cyrillic encoding.

        DejaVuSerif = ttfonts.TTFont('DejaVuSerif', '../rbapi/apps/api/static/fonts/DejaVuSerif.ttf')
        DejaVuSerifBold = ttfonts.TTFont('DejaVuSerifBold', '../rbapi/apps/api/static/fonts/DejaVuSerif-Bold.ttf')
        DejaVuSerifItalic = ttfonts.TTFont('DejaVuSerifItalic', '../rbapi/apps/api/static/fonts/DejaVuSerif-Italic.ttf')
        DejaVuSerifBoldItalic = ttfonts.TTFont('DejaVuSerifBoldItalic',
                                               '../rbapi/apps/api/static/fonts/DejaVuSerif-BoldItalic.ttf')

        pdfmetrics.registerFont(DejaVuSerif)
        pdfmetrics.registerFont(DejaVuSerifBold)
        pdfmetrics.registerFont(DejaVuSerifItalic)
        pdfmetrics.registerFont(DejaVuSerifBoldItalic)

        check_body = []
        frame = Frame(cm, cm, 20 * cm, 25 * cm)

        # Set styles

        style_normal = ParagraphStyle(
            name='russian_text',
            fontName='DejaVuSerif',
            fontSize=14,
            leading=1 * cm
        )
        style_bold = ParagraphStyle(
            name='russian_text',
            fontName='DejaVuSerifBold',
            fontSize=14,
            leading=1 * cm,
            spaceBefore=0.5 * cm
        )

        # Add attributes and additional info in the top of the check
        check_body.append(
            Paragraph(
                f'<img src="../rbapi{bank_info.logo.url}" valign = "bottom" height="50" width="150"/>',
                style_normal
            )
        )

        check_body.append(
            Paragraph(
                f'{bank_info.bank_name}',
                style_normal
            )
        )

        check_body.append(
            Paragraph(
                f'Інфомаційний центр {bank_info.support_number_1}',
                style_normal)
        )

        # Add breaklines
        check_body.append(Paragraph(f'\n<br />\n<br />', style_normal))

        # Add title
        check_body.append(Paragraph(f'<strong>Квитанція № {obj.receipt_id}</strong>', style_bold))
        check_body.append(Paragraph(f"<strong>Платник:</strong> {serializer.data['sender']}", style_normal))
        check_body.append(Paragraph(f"<strong>Отримувач:</strong> {serializer.data['recipient']}", style_normal))
        check_body.append(Paragraph(f"<strong>Сума:</strong> {serializer.data['amount']}", style_normal))
        check_body.append(Paragraph(f"<strong>Призначення платежу:</strong> {serializer.data['description']}", style_normal))
        check_body.append(Paragraph(f"<strong>Комісія:</strong> {serializer.data['commissionRate']}", style_normal))

        # Add breaklines
        check_body.append(Paragraph(f'\n<br />\n<br />', style_normal))

        # Add signature to text
        check_body.append(
            Paragraph(f'{bank_info.signature_info}', style_normal)
        )
        check_body.append(
            Paragraph(f'{bank_info.signature_person}', style_normal)
        )
        check_body.append(
            Paragraph(
                f'<br />\n<br />\n<br />\n<br />\n<br />\n<img src= "../rbapi{bank_info.sign.url}" valign="bottom" height="150" width="200"/>',
                style_bold)
        )

        # set Canvas
        canvas = Canvas(buffer)
        canvas.setFont('DejaVuSerif', 24)

        frame.addFromList(check_body, canvas)
        canvas.save()
        # Close the PDF object cleanly, and we're done.
        buffer.seek(0)

        logger.info('Return receipt: {}'.format(check_body))

        return buffer
