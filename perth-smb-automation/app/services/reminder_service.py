from app import db
from app.models import Notification
from app.services.sms_service import send_sms

def send_appointment_reminder(appointment):
    customer = appointment.customer
    business = appointment.business
    
    message = f"Reminder: Your appointment for {appointment.service} is on {appointment.appointment_date} at {appointment.appointment_time.strftime('%I:%M %p')} with {business.name}."
    
    success, result = send_sms(customer.phone, message)
    
    if success:
        appointment.reminder_sent = True
        
        notification = Notification(
            business_id=business.id,
            notification_type='reminder',
            message=f"Reminder sent to {customer.name} for {appointment.service}",
            channel='SMS',
            status='sent'
        )
        db.session.add(notification)
        db.session.commit()
    
    return success, result