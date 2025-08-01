from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from models import Intern

interns_bp = Blueprint('interns', __name__)

@interns_bp.route('/interns/me')
@login_required
def my_profile():
    if current_user.role != 'Intern':
        return {'error': 'Unauthorized'}, 403
    intern = Intern.query.filter_by(email=current_user.username).first()
    return jsonify({
        'name': intern.name,
        'email': intern.email,
        'education': intern.education,
        'skills': intern.skills,
        'performance_notes': intern.performance_notes
    })
