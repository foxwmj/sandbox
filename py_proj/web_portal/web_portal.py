# -*- coding: utf-8 -*-
"""
    Flaskr

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack, send_from_directory 
import datetime

import myLog
log = None

try:
    # this is how you would normally import
    from flask.ext.cors import *
except:
    # support local usage without installed package
    from flask_cors import *

import json
from collections import namedtuple
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)



#################
# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'resume_2016.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    UPLOAD_FOLDER=os.path.join(app.root_path, "upload_temp")
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
#################


#=====================================================
#
#            WEB PORTAL Begin
#
#====================================================
from conf import COMPOSITED_FOLDER as out_folder

@app.route('/test')
def test():
    # send_static_file will guess the correct MIME type
    return app.send_static_file('test.html')

@app.route('/test2')
def test2():
    #db = get_db()
    #cur = db.execute('select infoHash, resumeHash, link, name, jobDesc, school, lastJob, workYears, time, resume, dbInsertTime from resume order by id desc')
    #entries = cur.fetchall()
    return render_template('show_latest.html', entries=entries)

@app.route('/composited/<path:name>')
def composited(name):
    log.debug("Enter")
    return send_from_directory("composited",name)


#----------------------------------  PIC UPLOAD -------------------------
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import image_process

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/pic', methods=['POST'])
def pic():
    log.info("Enter upload_file")

    if request.method == 'POST':
        log.debug("-- Post")
        # check if the post request has the file part
        if 'file' not in request.files:
            log.error("3")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            log.error("4")
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            log.info("5 normal path!")

            filename = secure_filename(file.filename)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filePath)

            outFilePath = image_process.composeStyle_0(filePath, request.form['Main_Title'], request.form["Sub_Title"])

            #return "OK"
            return redirect(url_for("composited", name=outFilePath))

    log.error("6")

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

#=====================================================
#
#            WEB PORTAL End
#
#====================================================

def get_db_internal():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DATABASE'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db

    return top.sqlite_db

def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db_internal()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    if not os.path.isfile(app.config['DATABASE']):
        init_db()

    return get_db_internal()

@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()



import traceback
import sys

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))










@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/latest')
def show_latest():
    db = get_db()
    cur = db.execute('select infoHash, resumeHash, link, name, jobDesc, school, lastJob, workYears, time, resume, dbInsertTime from resume order by id desc')
    entries = cur.fetchall()
    return render_template('show_latest.html', entries=entries)


@app.route('/name')
def show_user():
    db = get_db()
    cur = db.execute('select name, uin from vip')
    entries = cur.fetchall()
    return render_template('show_user.html', entries=entries)

import os
@app.route('/resume.js')
def resume_js():
    # send_static_file will guess the correct MIME type
    return app.send_static_file('resume.js')


@app.route('/post', methods=['GET','POST'])
@cross_origin(headers=['Content-Type'])
def post_data():
    try:
        #insert_db()
        #test_db()
        #return "Good"

        j = request.json
        for person in j:
            try:
                infoHash, resumeHash, infoArray, resume = person[0],person[1],person[2],person[3]
                print "=" * 40
                print infoHash
                print resumeHash

                link, name, jobDesc, school, lastJob, workYears, location, time = infoArray[0], infoArray[1], infoArray[2], infoArray[3], infoArray[4], infoArray[5], infoArray[6], infoArray[7]
                print link
                print "\t%s\n\t%s\n\t%s\n\t%s\n\t%s\n\t%s\n\t%s" % (name, jobDesc, school, lastJob, workYears, location, time)
                print "-" * 20
                #print resume

                db = get_db()


                personExists = False
                cur = db.cursor()
                cur.execute("select * from resume where infoHash == ? AND resumeHash == ?", (infoHash, resumeHash))
                queryRes = cur.fetchall()
                personExists = len(queryRes) != 0

                if not personExists:
                    #addPerson()
                    currentTimeStr = str(datetime.datetime.now())
                    db.execute('insert into resume (infoHash, resumeHash, link, name, jobDesc, school, lastJob, workYears, time, resume, dbInsertTime) values (?,?,?,?,?,?,?,?,?,?,?)',
                        [infoHash, resumeHash, link, name, jobDesc, school, lastJob, workYears, time, resume, currentTimeStr])
                    db.commit()

                    #notify()
                #if personSimilar():
                    #notifySimilar()

            except Exception, err:
                print traceback.format_exc()
                print sys.exc_info()[0]

    except Exception, err:
        print traceback.format_exc()
        print sys.exc_info()[0]

    return "Good"

if __name__ == '__main__':
    #init_db()
    #app.run()

    log = myLog.init(app.root_path)
    #FORMAT = "[%(asctime)s | %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    #logging.basicConfig(format=FORMAT)
    #log = logging.getlog('werkzeug')
    #log.setLevel(logging.DEBUG) #INFO #WARNING 
    #logging.basicConfig(format='%(asctime)s %(message)s')
    #handler = logging.FileHandler(os.path.join(app.root_path, 'access.log'))
    #log.addHandler(handler)

    app.run(host='0.0.0.0')
