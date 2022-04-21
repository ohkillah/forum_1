from mailersend import emails
from celery import shared_task


mailersend_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNmI0ODkzZTM4ODVhMTQxNzc3MGU3Yjc3Mzk3MjA5NTEzZGZlMTAzZjcxZmFiMzUyNTM1OTNmZjA4YjIxYTA1ODhhOGM3MWQyM2QwZjFjNjkiLCJpYXQiOjE2NDg3MTM4NjcuNjM1NTQ0LCJuYmYiOjE2NDg3MTM4NjcuNjM1NTQ3LCJleHAiOjQ4MDQzODc0NjcuNjMyMjE2LCJzdWIiOiIyMTcwNCIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCJdfQ.S9TiBMHQPGMQmMi5iHEAhDzwcgcPyU-Njw25Cggeu4_6N6G3xkmOIxlADO2l4OhVVfqRkI1LCoB1lN2rFz76J0nprnBjM8wIPsoomokwdoUd23nYQFsaXXlXy0MpN1ynnQ37utVlIy3U36aPv1_HCRjHH3oDfL7GZK-E6Xvk1RzriUwbQe-4fZeAup9bv2J1fXboDwmoEBkYgIcfJIzML-wE1EgxBMHqnpiXth06o6wf__uhgMmN3dm16930pNApCw_9Js2BS3MP4eVyIcBIkKj0jkA-xtMu0lvnRxWvE5cAVwRn88oNtGkE8IK8L0U4TGU4zOJHhX2D4ZVYjJPWWP9Ue78yeDToHTK3d36dIVxATHUI4q_W9WYh_tjv81Iv9Ia__Pu92yjECLEhkLhm8JvwB9yWuUz2pJ22CLZEivqmEMpr4wg5nSuFUgvCC3n1kQiQFtHC3-44a6SQiUquPGYFAp_tDrMQwHWXa-HfoFweaXKrON_uOT2Tpg6ZcE17X1FFgg6Okiv9bQuovyilK_Dhdxyln9a0RqYyfzC0Ptf8dW8czymbvtppACzh0cdvKftIb7FyZzt0eo8IrC6hAINHgeEqkciHSm0T2DfpfLPQv2xF6QfRG1ytRmopUTYT68z-4BBRkfB-iIXbV1Dicjd9VYPXbO02h6QE9JsETUc"


@shared_task(name="send_email_with_mailersend")
def send_email(email: str, subject: str, text: str) -> None:
    mailer = emails.NewEmail(mailersend_token)

    mail_body = {}

    mail_from = {
        "name": "Data Science Academy",
        "email": "info@dsacademy.kz",
    }

    recipients = [
        {
            "name": "Your Client",
            "email": email,
        }
    ]

    reply_to = [
        {
            "name": "Data Science Academy",
            "email": "info@dsacademy.kz",
        }
    ]

    html = f"""
    <HTML>
      <body>
         <h3>{text}</h3>
      </body>
    </HTML>
    """

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject(subject, mail_body)
    mailer.set_html_content(html, mail_body)
    mailer.set_plaintext_content(text, mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    print("Sending email to:", email)
    return mailer.send(mail_body)
