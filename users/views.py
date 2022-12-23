from drf_yasg.utils import swagger_auto_schema

from rest_framework import status, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet


from requests.exceptions import HTTPError

from social_django.utils import psa

from .serializers import (
    OAuth2Serializer,
    User,
    UserSerializer
)


@swagger_auto_schema(request_body=OAuth2Serializer, method='post')
@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def social_auth(request, backend):
    """
    Receives an auth token from OAuth Backend and authenticate a user
    If using google set backend = google-oauth2
    """
    serializer = OAuth2Serializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        try:
            user = request.backend.do_auth(serializer.data['access_token'])
            print(user)

            if user is not None:
                return Response(
                    user.get_auth_tokens(),
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'errors': 'Authentication failed'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except HTTPError as e:
            return Response(
                data={
                    'error': 'Invalid token',
                    'detail': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class UserViewset(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer