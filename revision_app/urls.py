from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('view/<id>',views.viewStudent, name='view-student'),
    path('update/<id>',views.update, name='update-student'),
    path('delete/<id>',views.delete, name='delete-student'),
    path('add-student/',views.create, name='create'),
    path('search/',views.searchStudent, name='search'),
]
