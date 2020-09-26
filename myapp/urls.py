from django.contrib import admin
from django.urls import path
from .views import getalldata, getfavdata, updatefavdata,\
    postmodeldata,postdata,searchdata,deletedata,allApi,setdata

urlpatterns = [
    path('all_data/', allApi),
    path('get_all_data/', getalldata.as_view()),
    path('get_fav_data/', getfavdata.as_view()),
    path('update_fav_data/<int:pk>/', updatefavdata.as_view()),
    path('post_model_data/', postmodeldata.as_view()),
    path('post_data/', postdata.as_view()),
    path('set_data/', setdata),
    path('search/', searchdata.as_view()),
    path('delete/<int:pk>/', deletedata.as_view()),
]
