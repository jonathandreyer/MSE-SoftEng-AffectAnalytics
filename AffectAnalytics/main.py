# -*- coding: utf-8 -*-

import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from werkzeug.utils import secure_filename

import resstrings as res
import github.github as github
# from github.emotions import Emotions


# Token file that's used to access Github
TOKEN = None

# The GitHub object
GITHUB = None

# TODO The User that is now logged in, may be able to check this in the session object


# Constants, paths, etc.
UPLOAD_FOLDER = './uploads'  # check to see where this is exactly
ALLOWED_EXTENSIONS = set(['token', 'tk'])

# Create the application instance
app = Flask(__name__)
# Load configuration from this file (main.py)
# app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load default config and override config from an environment variable
app.config.update(dict(
    # DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def show_entries():
    if session.get('logged_in'):
        if TOKEN:

            flash("You are logged in, decide the pull requests you want to evaluate")
            global GITHUB
            GITHUB = github.GitHub(TOKEN)


        else:
            print "Token does not exist"

        print "TOKEN = ", TOKEN

    # We will now use Templates to render html.
    # We should actually render the index.
    return render_template('show_entries.html')


@app.route('/repos', methods=['POST'])
def get_repos():
    if not session.get('logged_in'):
        abort(401)
    print "Coming soon"


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    # Don't use any database, just the browser's memory
    # db = get_db()
    # db.execute('insert into entries (title, text) values (?, ?)',
    #           [request.form['title'], request.form['text']])
    # db.commit()

    print request.form['title']
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/pullrequest')
def show_pull_request():
    return "Test page"


@app.route('/help')
def help():
    return "Help page"


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Don't use any database, just the browser's memory
    global TOKEN
    error = None
    valid_file = False

    if request.method == 'POST':

        # Check if the post request has the file part
        if 'tokenfile' not in request.files:
            flash(res.no_file)
            return redirect(request.url)

        token_file = request.files['tokenfile']

        # if user does not select file, browser also
        # submit a empty part without filename
        if token_file.filename == '':
            flash(res.no_file_selected)
            return redirect(request.url)

        # Check the file that was uploaded.
        if token_file and allowed_file(token_file.filename):
            # The file uploaded is valid.

            filename = secure_filename(token_file.filename)
            # Do we really want to save?
            token_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # We just want the value.

            TOKEN = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        else:
            flash(res.invalid_file)
            return redirect(request.url)

        username = request.form['username']
        session['logged_in'] = True
        flash(res.login_success(username))
        return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
