import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def send_email(to_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = current_app.config['SMTP_EMAIL']
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(
            current_app.config['SMTP_SERVER'],
            current_app.config['SMTP_PORT']
        )
        server.starttls()
        server.login(
            current_app.config['SMTP_EMAIL'],
            current_app.config['SMTP_PASSWORD']
        )
        server.send_message(msg)
        server.quit()
        
        return True, "Email sent successfully"
    except Exception as e:
        current_app.logger.error(f"Email Error: {str(e)}")
        return False, str(e)