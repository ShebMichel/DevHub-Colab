# Perth SMB Automation System

Flask-based automation system for Perth small businesses.

## Features

- ✅ Appointment management with automatic reminders
- ✅ Customer relationship management (CRM)
- ✅ Inventory tracking with low-stock alerts
- ✅ SMS & Email notifications
- ✅ RESTful API
- ✅ Background task scheduling

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your credentials

# Initialize database
flask db init
flask db migrate
flask db upgrade

# Run the application
python run.py
```

## Project Structure

```
perth-smb-automation/
├── app/                    # Main application package
│   ├── models/            # Database models
│   ├── routes/