from django.urls import path,include
from rest_framework import *

from .views import *

urlpatterns = [
    path("",include()),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("product/",ProductView.as_view(),name="product"),
    path("product/<int:id>/",ProductView.as_view(),name="productdetal"),

]
