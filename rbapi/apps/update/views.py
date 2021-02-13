from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsRO
from apps.update.serializers import UpdateBaseSerializer
import logging

logger = logging.getLogger(__name__)


class UpdateBase(APIView):

    permission_classes = [IsRO]

    def post(self, request):

        serializer = UpdateBaseSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save()
            except Exception as err:
                logger.error('Error saving by %s' % err)
                return Response(status=status.HTTP_304_NOT_MODIFIED)
            else:
                logger.info("Receipt created")

            return Response(status=status.HTTP_201_CREATED)
        else:
            logger.info("Receipt not created")
            return Response(status=status.HTTP_400_BAD_REQUEST)
