from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home'), # API - POSTMAN 
    path('post/<int:post_id>/',post_detail,name="post_detail"),
]
