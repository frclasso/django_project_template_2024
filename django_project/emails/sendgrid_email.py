import os
import environ
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

def sendEmail(from_email,to_emails,subject,message):
    """Sendgrid send mail -  https://app.sendgrid.com/"""
    # $19.95/month
    context = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        html_content=f"<p>{message}</p>")
    try:
        key = config['SENDGRID_API_KEY']
        sg = SendGridAPIClient(key)
        response = sg.send(context)
        print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        print(e.context)


from_email = 'administracao@floripacodegurus.com.br'
to_emails = 'agilcontabil2023@gmail.com'
subject = 'Sending with Twilio SendGrid is Fun'
message = 'A new message from Fabio.'
sendEmail(from_email,to_emails,subject, message)