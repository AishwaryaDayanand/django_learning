from django.urls import path
from . import views

urlpatterns = [
    path('greet/' ,views.sayHello , name="greet" ),
    path('',views.viewProjects,name="projects"),
    path('project/<str:id>/' , views.displayProject , name='project' ),
    path('create-project/',views.createProject,name='create-project'),
    path('update-project/<str:id>/',views.updateProject,name="update-project"),
    path('delete-project/<str:id>/',views.deleteProject,name="delete-project"),

    # without confirm for delete
    # path('delete-project/<str:id>/',views.deleteProjectNoConfirm,name="delete-project"),

]





