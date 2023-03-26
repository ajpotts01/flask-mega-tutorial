from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app
from app.forms import LoginForm
from app.models import User


# region Helper methods
def get_user(name: str) -> dict:
    user: dict = dict(username=name)
    return user


def get_context_index() -> dict:
    # user: dict = get_user(name="ajp")
    context: dict = dict(title="Home", posts=get_posts())
    return context


def get_context_login(form: LoginForm) -> dict:
    context: dict = dict(title="Sign In", form=form)

    return context


def get_posts() -> list[dict]:
    posts: list[dict] = [
        dict(author=get_user(name="John"), body="Beautiful day in Portland!"),
        dict(author=get_user(name="Susan"), body="The Avengers movie was so cool!"),
    ]
    return posts


# endregion Helper methods


# region Endpoints/views
@app.route("/")
@app.route("/index")
@login_required
def index() -> str:
    context: dict = get_context_index()
    view: str = render_template(template_name_or_list="index.html", **context)

    return view


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form: LoginForm = LoginForm()
    context: dict = get_context_login(form=form)

    if form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(password=form.password.data):
            flash(f"Invalid username or password.")
            return redirect(url_for("login"))

        login_user(user, remember=form.remember_me.data)
        next_page: str = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")

        return redirect(url_for("index"))

    view: str = render_template(template_name_or_list="login.html", **context)

    return view


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


# endregion Endpoints
