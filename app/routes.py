from flask import render_template
from app import app


# region Helper methods
def get_user(name: str) -> dict:
    user: dict = dict(username=name)
    return user


def get_context() -> dict:
    user: dict = get_user(name="ajp")
    context: dict = dict(title="Home", user=user, posts=get_posts())
    return context


def get_posts() -> list[dict]:
    posts: list[dict] = [
        dict(author=get_user(name="John"), body="Beautiful day in Portland!"),
        dict(author=get_user(name="Susan"), body="The Avengers movie was so cool!"),
    ]
    return posts


# endregion Helper methods


@app.route("/")
@app.route("/index")
def index():
    context: dict = get_context()
    view: str = render_template(template_name_or_list="index.html", **context)

    return view
