# HR Services
def create_internship_campaign(data):
    return {"status": "success", "message": "Campaign created"}

def get_intern_profiles():
    return [{"id": 1, "name": "John Doe"}]

def generate_reports():
    return {"report": "Performance Report"}

# Coordinator Services
def schedule_interview(data):
    return {"status": "scheduled", "interview": data}

def setup_training(data):
    return {"status": "training setup", "details": data}

def track_performance():
    return {"performance": "Good"}

# Mentor Services
def log_daily_progress(data):
    return {"status": "logged", "details": data}

def assess_skills(data):
    return {"status": "assessed", "skills": data}

def send_message_to_intern(data):
    return {"status": "message sent", "to": data.get("intern_id")}

# Intern Services
def get_personal_dashboard():
    return {"tasks": [], "schedule": []}

def submit_feedback(data):
    return {"status": "feedback received", "feedback": data}

def track_skill_development():
    return {"skills": {"Python": "Intermediate"}}

# Admin Services
def configure_system(data):
    return {"status": "configured", "settings": data}

def provide_technical_support(data):
    return {"status": "support ticket created", "ticket": data}
