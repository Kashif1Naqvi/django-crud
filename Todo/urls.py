from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
    path('' ,  views.todo , name='todo'),
    path('create/',views.createtodo, name='createtodo'),
    path('<int:pk>/',views.viewtodo, name='viewtodo'),
    path('<int:pk>/complete/',views.completetodo, name='completetodo'),
    path('complete/',views.completelisttodo, name='completelisttodo'),
    path('<int:pk>/delete/',views.deletetodo, name='deletetodo'),
]
