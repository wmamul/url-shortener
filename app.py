import os
import string
import random
from flask import Flask, request, redirect, render_template, flash
import redis
import validators

application = Flask(__name__, template_folder='templates/')
application.config.update(SECRET_KEY=os.environ['FLASK_SECRET'])
r = redis.Redis()

def slug_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@application.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@application.route('/', methods=['POST'])
def shorten_url():
    if validators.url(request.form['url']):
        url = request.form['url']
        slug = slug_generator()
        r.set(slug, url)
        return render_template('index.html', slug=slug) 
    else:
        flash('Provided URL is invalid. Please enter a valid one.')
        return render_template('index.html')


@application.route('/<url_id>', methods=['GET'])
def go_to_url(url_id):
    url = r.get(url_id).decode('utf-8')
    return redirect(url)
