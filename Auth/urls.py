from django.urls import path ,include

from Auth.views import MyModelViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'id',MyModelViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs in your URLconf
    path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('allauth/account/', include('allauth.account.urls')),

]
