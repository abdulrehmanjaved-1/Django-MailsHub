import smtplib
import os
import threading

def send_email(subject, body, recipient):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    from_email = os.getenv('FROM_EMAIL')

    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(from_email, recipient, message)
    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

def send_emails(subject, body, recipients):
    threads = []
    for recipient in recipients:
        thread = threading.Thread(target=send_email, args=(subject, body, recipient))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Example usage:
    subject = "Subject of the Email"
    body = "Body of the Email"
    recipients = ["recipient1@example.com", "recipient2@example.com"]
    send_emails(subject, body, recipients)
