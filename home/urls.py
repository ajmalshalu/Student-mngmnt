from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
 
    path('home/',views.Home.as_view(),name='home'),
    path('enquiry/',views.Enquiry.as_view(),name='enquiry'),
    path('staff/',views.Staffs.as_view(),name='staff'),
    path('profile/',views.Profile.as_view(),name='profile'),
    path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
    path('edit/',views.Edit.as_view(),name='edit'), 
    path('student/',views.Form.as_view(),name='student'),
    path('showstudent/',views.Showstudent.as_view(),name='showstudent'),
    path('delete/',views.Delete.as_view(),name='delete'),
]