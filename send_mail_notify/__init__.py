import azure.functions as func
from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import Mail

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        to_email = req_body.get("to_email")
        subject = req_body.get("subject")
        message = req_body.get("message")

        if not to_email:
            return func.HttpResponse("Missing to_email", status_code=400)

        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])

        email = Mail(
            from_email="oanaalexandrasidorencu@gmail.com",
            to_emails=to_email,
            subject=subject,
            plain_text_content=message
        )
        sg.send(email)

        return func.HttpResponse("Email trimis!")
    except Exception as e:
        return func.HttpResponse(f"Eroare: {str(e)}", status_code=500)


{
  "to_email": "cineva@email.com",
  "subject": "Test email",
  "message": "Salut!"
}
