from flask import Blueprint, request, jsonify
from models import db, Intern
from flask_login import login_required

hr_bp = Blueprint('hr', __name__)

@hr_bp.route('/hr/create_intern', methods=['POST'])
@login_required
def create_intern():
    data = request.json
    intern = Intern(
        name=data['name'],
        email=data['email'],
        education=data.get('education'),
        skills=data.get('skills')
    )
    db.session.add(intern)
    db.session.commit()
    return jsonify({'message': 'Intern created successfully'})
