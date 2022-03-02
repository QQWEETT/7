from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from product.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/cart/', CartItemView.as_view(), name="cart"),
    path('api/v1/cart/add/', CartItemAddView.as_view()),
    path('api/v1/cart/delete/<int:pk>/', CartItemDelView.as_view()),
    path('api/v1/cart/add_one/<int:pk>/', CartItemAddOneView.as_view()),
    path('api/v1/cart/reduce_one/<int:pk>/', CartItemReduceOneView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/auth', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify', TokenVerifyView.as_view(), name='token_verify'),


]