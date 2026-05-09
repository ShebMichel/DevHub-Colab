from app import create_app, db
from app.tasks.scheduler import start_scheduler

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Database initialized")
    
    start_scheduler()
    print("🚀 Perth SMB Automation Server Starting...")
    print("📡 API running at http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)