from config.mail import mail
from flask_mail import Message


def send_email(emails, message, title, sender):
    mailable = Message(title, sender=sender, recipients=[emails])
    mailable.body = message
    try:
        mail.send(mailable)
        return {
            "success": True,
            "message": "Email was successfully sent"

        }, 201
    except Exception as e:
        return {
            "success": False,
            "message": str(e)

        }, 500
