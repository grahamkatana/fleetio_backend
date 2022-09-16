from config.mail import mail
from flask_mail import Message


#  context={
#    "fullname": fullname,
#    "otp_code": otp_code,
#    "year": datetime.now().year,
#    "subject":"Registration Mail",
# }
# email_message = Message(
#    subject=mail_subject,
#    sender=os.getenv("ADMIN_EMAIL"),
#    recipients=[receipients_email],
#    html=render_template(template_name_or_list="otp.html", **context)
# )
# send_mail.send(email_message)


def send_email(recipients, message, subject, sender):
    
    mailable = Message(subject, sender=sender, recipients=[recipients])
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
