from flask import Blueprint, request, jsonify
from services import (
    create_internship_campaign, get_intern_profiles, generate_reports,
    schedule_interview, setup_training, track_performance,
    log_daily_progress, assess_skills, send_message_to_intern,
    get_personal_dashboard, submit_feedback, track_skill_development,
    configure_system, provide_technical_support
)

bp = Blueprint("ims", __name__)

def register_routes(app):
    app.register_blueprint(bp)

# HR Managers
@bp.route("/hr/campaign", methods=["POST"])
def hr_create_campaign():
    data = request.json
    return jsonify(create_internship_campaign(data))

@bp.route("/hr/interns", methods=["GET"])
def hr_get_intern_profiles():
    return jsonify(get_intern_profiles())

@bp.route("/hr/reports", methods=["GET"])
def hr_generate_reports():
    return jsonify(generate_reports())

# Internship Coordinators
@bp.route("/coordinator/interview", methods=["POST"])
def coordinator_schedule_interview():
    return jsonify(schedule_interview(request.json))

@bp.route("/coordinator/training", methods=["POST"])
def coordinator_setup_training():
    return jsonify(setup_training(request.json))

@bp.route("/coordinator/performance", methods=["GET"])
def coordinator_track_performance():
    return jsonify(track_performance())

# Mentors
@bp.route("/mentor/daily", methods=["POST"])
def mentor_log_daily_progress():
    return jsonify(log_daily_progress(request.json))

@bp.route("/mentor/skills", methods=["POST"])
def mentor_assess_skills():
    return jsonify(assess_skills(request.json))

@bp.route("/mentor/message", methods=["POST"])
def mentor_send_message():
    return jsonify(send_message_to_intern(request.json))

# Interns
@bp.route("/intern/dashboard", methods=["GET"])
def intern_dashboard():
    return jsonify(get_personal_dashboard())

@bp.route("/intern/feedback", methods=["POST"])
def intern_feedback():
    return jsonify(submit_feedback(request.json))

@bp.route("/intern/skills", methods=["GET"])
def intern_skill_tracking():
    return jsonify(track_skill_development())

# Admin
@bp.route("/admin/config", methods=["POST"])
def admin_configure():
    return jsonify(configure_system(request.json))

@bp.route("/admin/support", methods=["POST"])
def admin_support():
    return jsonify(provide_technical_support(request.json))
