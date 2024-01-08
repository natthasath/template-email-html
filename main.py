import resend
from decouple import config

resend.api_key = config("RESEND_KEY")

file_path = 'template/maily-to.html'
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

r = resend.Emails.send({
  "from": config("EMAIL_FROM"),
  "to": config("EMAIL_TO"),
  "subject": "Confirm Email",
  "html": file_content
})