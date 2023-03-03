from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


# region Helper methods
def get_user(name: str) -> dict:
    user: dict = dict(username=name)
    return user


def get_context_index() -> dict:
    user: dict = get_user(name="ajp")
    context: dict = dict(title="Home", user=user, posts=get_posts())
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
def index() -> str:
    context: dict = get_context_index()
    view: str = render_template(template_name_or_list="index.html", **context)

    return view


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    form: LoginForm = LoginForm()
    context: dict = get_context_login(form=form)

    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect("/index")

    view: str = render_template(template_name_or_list="login.html", **context)

    return view


# endregion Endpoints
