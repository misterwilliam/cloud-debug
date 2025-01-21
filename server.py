import os

from flask import Flask, make_response, render_template, request, Response

app = Flask(__name__)

@app.route("/")
def root_handler() -> str:
  return "<a href='/env'>env</a>"

@app.route("/env")
def env_handler() -> str:
  return render_template("env.html", env_vars=os.environ)

@app.route("/request")
def request_handler() -> Response:
  resp = make_response(
    render_template("request.html",
                    scheme=request.scheme,
                    method=request.method,
                    headers=request.headers,
                    cookies=request.cookies,
                    body=request.get_data(as_text=True)))
  resp.set_cookie("foo", "bar")
  return resp
