from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login, Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='Tareas'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='Tarea'),    
    path('task/add/', TaskCreate.as_view(), name='CrearTarea'),    
    path('task/update/<int:pk>', TaskUpdate.as_view(), name='ActualizarTarea'),    
    path('task/delete/<int:pk>', TaskDelete.as_view(), name='EliminarTarea'),    
    path('login/', Login.as_view(), name='Login'),    
    path('logout/', LogoutView.as_view(next_page='Login'), name='Logout'),   
    path('register/', Register.as_view(), name='Register'),    
    

]