from django.urls import path
from .views import post_employee

urlpatterns =[
    path('post_employee/', post_employee),

]