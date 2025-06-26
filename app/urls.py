from django.urls import path
from .views import file_data, report_data


urlpatterns = [
    path('users_data/', report_data, name="User's data"),
    path('upload_files/', file_data, name="User's File"),
    
]
