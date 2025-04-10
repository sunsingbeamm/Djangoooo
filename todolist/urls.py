from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  
    path('work/', views.work, name='work'), 
    path('work/<int:todo_id>/', views.work, name='work_detail'),
    path('update/<int:todo_id>/', views.update, name='update'),
    
    # delete url 추가   
	  path('delete/<int:todo_id>/', views.delete, name='delete'),
]
