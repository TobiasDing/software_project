# coding:utf8

from . import home
from flask import render_template, redirect, url_for


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))


@home.route("/register/")
def register():
    return render_template("home/register.html")


@home.route("/user/")
def user():
    return render_template("home/user.html")


@home.route("/pwd/")
def pwd():
    return render_template("home/pwd.html")


@home.route("/comments/")
def comments():
    return render_template("home/comments.html")


@home.route("/login_log/")
def login_log():
    return render_template("home/login_log.html")


@home.route("/collections/")
def collections():
    return render_template("home/collections.html")


@home.route("/animation/")
def animation():
    return render_template("home/animation.html")


@home.route("/search/")
def search():
    return render_template("home/search.html")


@home.route("/play/")
def play():
    return render_template("home/play.html")


@home.route("/pay/")
def pay():
    return render_template("home/pay.html")
