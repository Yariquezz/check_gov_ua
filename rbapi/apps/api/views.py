from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse
from rest_framework.decorators import api_view, permission_classes
from .models import RBAresponse
from .serializers import RBAresponseSerializer
from .permissions import IsCheckGov
from django.shortcuts import render
from django.utils import timezone
from .create_pdf import CreateFile
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

    permission_classes = [IsCheckGov]

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

        try:
            obj = RBAresponse.objects.get(link_code=kwargs['link_id'])
        except Exception as err:
            logger.info("Receipt is not found %s" % err)
            message = "Receipt is not found"
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        else:
            check = CreateFile()
            buffer = check.get_pdf(obj)

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.

        return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')



