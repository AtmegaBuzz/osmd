from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("services/",views.services,name="services"),
    path("contact/",views.contact,name="contact"),
    path("detail_group/<int:pk>",views.detailGroup_view,name="detail_group"),
]
