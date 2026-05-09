from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app import db
from app.models import Appointment, Inventory, Notification
from app.services.reminder_service import send_appointment_reminder

def check_and_send_reminders():
    from app import create_app
    app = create_app()
    
    with app.app_context():
        appointments = Appointment.query.filter(
            Appointment.reminder_sent == False,
            Appointment.status == 'confirmed'
        ).all()
        
        for apt in appointments:
            apt_datetime = datetime.combine(apt.appointment_date, apt.appointment_time)
            hours_until = (apt_datetime - datetime.now()).total_seconds() / 3600
            
            if 0 < hours_until <= 24:
                send_appointment_reminder(apt)
                print(f"✅ Reminder sent for appointment ID: {apt.id}")

def check_low_stock():
    from app import create_app
    app = create_app()
    
    with app.app_context():
        low_stock_items = Inventory.query.filter(
            Inventory.quantity <= Inventory.min_stock
        ).all()
        
        for item in low_stock_items:
            notification = Notification(
                business_id=item.business_id,
                notification_type='low_stock',
                message=f"Low Stock Alert: {item.item_name} - Only {item.quantity} {item.unit} left!",
                channel='System'
            )
            db.session.add(notification)
        
        if low_stock_items:
            db.session.commit()
            print(f"📦 Low stock alerts created for {len(low_stock_items)} items")

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(
        func=check_and_send_reminders,
        trigger="interval",
        minutes=15,
        id='reminder_check',
        replace_existing=True
    )
    
    scheduler.add_job(
        func=check_low_stock,
        trigger="interval",
        hours=6,
        id='stock_check',
        replace_existing=True
    )
    
    scheduler.start()
    print("⏰ Scheduler started: Reminders (15 min), Stock checks (6 hours)")