# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from allauth.account.models import EmailConfirmation

from rest_framework import viewsets
from .models import MyModels
from .serializers import MyModelSerializer


class ResendActivationEmail(APIView):
    def post(self, request):
        user = request.user  # Assuming you are working with authenticated users

        email_confirmation = EmailConfirmation.create(user)
        email_confirmation.sent = None
        email_confirmation.save()

        # TODO: Send the activation email here (you can use Django's send_mail)

        return Response({'message': 'Activation email resent successfully'}, status=status.HTTP_200_OK)


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModels.objects.all()
    serializer_class = MyModelSerializer