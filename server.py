import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root_handler() -> str:
  return "<a href='/env'>env</a>"

@app.route("/env")
def env_handler() -> str:
  return render_template("env.html", env_vars=os.environ)
