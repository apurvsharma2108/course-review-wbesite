
from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('',views.home,name="home"),
    path('details/<int:id>/',views.detail,name="detail"),
    path('addcourses/',views.add_courses,name="add_courses"),
    path('editcourses/<int:id>/',views.edit_courses,name="edit_courses"),
    path('deletecourses/<int:id>/',views.delete_courses,name="delete_courses")
]
