from .import views
from django.urls import path
app_name='todoapp'
urlpatterns = [
    path('',views.add,name='add'),
    path('details',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classviewhome/',views.TaskListview.as_view(),name='classviewhome'),
    path('classviewdetails/<int:pk>/',views.TaskDetailview.as_view(),name='classviewdetails'),
    path('classviewupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='classviewupdate'),
    path('classdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='classdelete'),
]
