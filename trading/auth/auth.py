from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user

from .forms import SignupForm
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
    return render_template("/register.html", form=form, error=error)
