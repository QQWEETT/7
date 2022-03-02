from django.urls import include, path
from rest_framework import routers

from product.views import ProductAPIList, CategoryAPIList

router = routers.DefaultRouter()
router.register(r'product', ProductAPIList)
router.register('category', CategoryAPIList)


urlpatterns = [
    path('', include(router.urls)),

]
