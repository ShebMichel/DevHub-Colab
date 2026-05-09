from flask import current_app
from twilio.rest import Client

def send_sms(to_phone, message):
    try:
        client = Client(
            current_app.config['TWILIO_ACCOUNT_SID'],
            current_app.config['TWILIO_AUTH_TOKEN']
        )
        
        result = client.messages.create(
            body=message,
            from_=current_app.config['TWILIO_PHONE_NUMBER'],
            to=to_phone
        )
        
        return True, result.sid
    except Exception as e:
        current_app.logger.error(f"SMS Error: {str(e)}")
        return False, str(e)