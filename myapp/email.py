from django.core.mail import send_mail
from django.conf import settings

def send_summary_email(summary_html):
    subject = "Python Assignment - Arnav More"
    message = f"Here is the summary of the uploaded data:<br><br>{summary_html}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['morearnav019@gmail.com','tech@themedius.ai',]
    send_mail(subject, '', email_from, recipient_list, html_message=message)

