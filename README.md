# URL Shortener #

URL Shortener written in Python using Flask and Redis.

### How to run? ###
Set up a `FLASK_SECRET` enviroment variable before running, like:<br/>
`export FLASK_SECRET=$(python -c 'import os; print(os.urandom(16))')`<br/>
Run `app.py` with a WSGI HTTP server, like `gunicorn` and open up the webpage.
