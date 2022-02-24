from django.urls import path

from .views import homePage, student_list, coach_list, student_details


urlpatterns = [
    path('home/',homePage, name="home"), #name="home" n'est pas obligatoire
    path('students/',student_list, name="student_list"),
    path('coachs/', coach_list , name="coach_list"),
    path('student/<int:id>', student_details , name="student_details"),
]

