import requests
from dotenv import load_dotenv, dotenv_values
config = dotenv_values(".env")



def send_simple_message(to_email, subject, message):
    """Mailgun API send mail - https://app.mailgun.com/"""
    # $15.00/ month
    return requests.post(
                        "https://api.mailgun.net/v3/sandbox2bf5f20a05ef43bdad8033d96f8c97f5.mailgun.org/messages",
                        auth=("api", config["API_KEY"]),
                        data={
                                "from": "Excited User <mailgun@sandbox2bf5f20a05ef43bdad8033d96f8c97f5.mailgun.org>",
                                "to": to_email,
                                "subject": subject,
                                "text": message
                            }
                        )


# from_email = 'administracao@floripacodegurus.com.br'
to_email = "frclasso@yahoo.com.br"
subject = 'Sending with Mailgun'
message = 'A new message from Fabio by using Mailgun.'
send_simple_message(to_email, subject, message)