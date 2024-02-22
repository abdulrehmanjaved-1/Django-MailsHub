# email_api_project/urls.py

from django.urls import path
from email_api import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line to define the root URL pattern
    path('scrape/', views.scrape_emails, name='scrape_emails'),
    path('send/', views.send_emails, name='send_emails'),
]
