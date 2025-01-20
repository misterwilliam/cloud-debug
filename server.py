import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_handler():
  return "<a href='/env'>env</a>"

@app.route("/env")
def env_handler():
  lines = []
  for key, value in os.environ.items():
    lines.append(f"{key}={value}")
  output = "<p>%s</p>" % "<br>".join(lines)
  return output
