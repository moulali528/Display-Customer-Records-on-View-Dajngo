from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_record/', views.add_record, name='add_record'),
    path('record/<record_id>', views.update_record, name='update_record'),
    path('delete_record/<record_id>', views.delete_record, name='delete_record'),
    #path('display_delete_record', views.display_delete_record, name='display_delete_record'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),
]
