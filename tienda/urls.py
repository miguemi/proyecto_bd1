import imp
from xml.dom.minidom import Document
from django.urls import path

from .import views 


urlpatterns = [

 
    path('',views.tienda, name="Tienda"),
   
  

]

