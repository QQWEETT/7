from django.urls import include, path
from rest_framework import routers

from product.views import *

router = routers.DefaultRouter()
router.register(r'product', ProductAPIList)
router.register('category', CategoryAPIList)


urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartItemView.as_view(), name="cart"),
    path('cart/add/', CartItemAddView.as_view()),
    path('cart/delete/<int:pk>/', CartItemDelView.as_view()),
    path('cart/add_one/<int:pk>/', CartItemAddOneView.as_view()),
    path('cart/reduce_one/<int:pk>/', CartItemReduceOneView.as_view()),

]
