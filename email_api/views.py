from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import scraping_email
from . import scraping_email

# email_api/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to your Django email API!")


@api_view(['POST'])
def scrape_emails(request):
    search_query = request.data.get('search_query', '')
    emails = scraping_email.scrape_emails(search_query)
    return Response({'emails': emails})

@api_view(['POST'])
def send_emails(request):
    subject = request.data.get('subject', '')
    body = request.data.get('body', '')
    recipients = request.data.get('recipients', [])
    scraping_email.send_emails(subject, body, recipients)
    return Response({'message': 'Emails sent successfully!'})
