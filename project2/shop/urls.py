from .import views
from django.urls import path
app_name='shop'
urlpatterns = [
    path('',views.shopreg,name='shopreg'),
    path('mobadd/',views.mob_add,name='mob_add'),
    path('mobile/<int:mobid>/',views.mobdetail,name='mobdetail'),
    path ('update/<int:id>/' ,views.update , name='update'),
    path ('edit/<int:id>/' , views.edit , name='edit' ) ,
]