from django.urls import path
from website.views import home,logout_user,register_user,customer_record,delete_record,Add_record,update_record

urlpatterns = [
path('', home, name='home'),
path('logout/',logout_user,name='logout'),
path('register/',register_user,name='register'),
path('record/<int:pk>/',customer_record,name='record'),
path('deleterecord/<int:pk>/',delete_record,name='delete-record'),
path('add_record/',Add_record,name='add_record'),
path('update_record/<int:pk>', update_record, name='update_record'),


]