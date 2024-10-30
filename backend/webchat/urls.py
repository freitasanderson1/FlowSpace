from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from webchat.views import IndexView, GetUserUsernameView, GetUserChatMessages
from webchat.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('getUserUsername/', GetUserUsernameView.as_view(), name="getUserUsername"),

    path('', IndexView.as_view(), name="Index"),
    path('login/', LoginView.as_view(), name='login'),
]

router = DefaultRouter(trailing_slash=False)
router.register(r'api/UserMessages',GetUserChatMessages, basename='GetUserMessages')
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)