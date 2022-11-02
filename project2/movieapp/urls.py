from .import views
from django.urls import path
app_name='movieapp'
urlpatterns = [
    path('',views.reg,name='reg'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.movie_add,name='movie_add'),
    path('update/<int:id>/',views.update,name='update'),
    path ('delete/<int:id>/', views.delete, name='delete')

]