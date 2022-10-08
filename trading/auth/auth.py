from flask import Blueprint, redirect, request, url_for
from flask_login import logout_user, current_user, login_user

from .forms import LoginForm, SignupForm
from .models import db, User

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/signup', methods=['GET', 'POST'])
# @login_required
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    error = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user is None:
                user = User(
                    name=form.name.data,
                    username=form.username.data,
                    email=form.email.data,
                    role=form.role.data,
                    balance=0
                )
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()  # Create new user
                login_user(user)  # Log in as newly created user
                if form.role.data == 'Admin':
                    return redirect(url_for('admin_bp.dashboard'))
                elif form.role.data == 'User':
                    return redirect(url_for('user_bp.dashboard'))


            else:
                error = 'User with Email ID already exists'
        else:
            error = ''
            for _, values in form.errors.items():
                error = values[0] + '\n'
    return form


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        if current_user.role == 'Admin':
            return redirect(url_for('admin_bp.dashboard'))
        elif current_user.role == 'User':
            return redirect(url_for('user_bp.dashboard'))

    form = LoginForm()
    # Validate login attempt
    error = ''
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if not user:
                error = 'Email ID Does not exist'
            else:
                if user and user.check_password(password=form.password.data):
                    login_user(user)
                    next_page = request.args.get('next')
                    if user.role == 'Admin':
                        return redirect(url_for('admin_bp.dashboard'))
                    elif user.role == 'User':
                        return redirect(url_for('user_bp.dashboard'))
                elif not user.check_password(password=form.password.data):
                    error = 'Invalid Password'
                else:
                    error = 'System Currently Down. Try after some time'
            return form
        else:
            error = 'Invalid details'
    return form


@auth_bp.route("/logout")
# @login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))