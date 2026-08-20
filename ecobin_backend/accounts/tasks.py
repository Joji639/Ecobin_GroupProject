from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, max_retries=3)
def send_email_otp_task(self, email, otp_code):
    try:
        send_mail(
            subject="EcoBin - Your Password Reset OTP",
            message=f"Your OTP for password reset is {otp_code}. It is valid for 5 minutes.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        return f"Email OTP sent to {email}"
    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)