# cloud-debug

Containerized webserver with misc admin tools.

## Development quickstart

```Shell
# Create venv to contain dependencies
$ python3 -m venv cloud-debug-venv
$ source cloud-debug-venv/bin/activate

# Clone repo and install required packages
$ git clone https://github.com/misterwilliam/cloud-debug.git
$ cd cloud-debug
$ pip install -r requirements.txt

# Run server locally
$ flask --app server run

# Update requirements
$ pip freeze > requirements.txt

# Run typechecker
$ mypy server.py
```
