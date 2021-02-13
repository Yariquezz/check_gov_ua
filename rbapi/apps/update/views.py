from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.update.serializers import UpdateBaseSerializer
from .permissions import IsRO
import logging

logger = logging.getLogger(__name__)


class UpdateBase(APIView):

    permissions_classes = [IsRO]

    def get(self, request):

        return Response(status.HTTP_404_NOT_FOUND)

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
