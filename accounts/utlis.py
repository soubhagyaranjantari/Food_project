from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

def send_verification_email(request):
    current_site=get_current_site(request)
    message = 'please verify your email'
    message_body=render_to_string('accounts/email/email_verification.html',{
        
    })
