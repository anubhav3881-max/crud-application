from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.addmissionpage, name="addmission"),
    
    path('update', views.updatepage, name="update"),
    path('signup', views.signuppage, name="signup"),
    path('login',views.loginpage, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('display', views.displaypage, name="display"),
    path('delete/<int:id>',views.deleterecord,name="delete"),
    path('edit/<int:id>', views.editrecord, name="edit")
]