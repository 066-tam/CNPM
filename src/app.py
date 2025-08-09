from flask import Flask, render_template_string, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ims.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --------- Models ---------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # intern, mentor, hr, admin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------- Routes ---------
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        return "Login Failed"
    return render_template_string("""
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    """)

@app.route('/dashboard')
@login_required
def dashboard():
    return f"Welcome {current_user.username}! Role: {current_user.role}"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --------- Init DB & Create Test User ---------
@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        hashed_pw = bcrypt.generate_password_hash('123').decode('utf-8')
        new_user = User(username='admin', password=hashed_pw, role='admin')
        db.session.add(new_user)
        db.session.commit()

# --------- Run ---------
if __name__ == '__main__':
    app.run(debug=True)

