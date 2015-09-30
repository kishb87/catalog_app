from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Make, Model, Specs
import requests

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

# Connect to Database and create database session
engine = create_engine('sqlite:///car.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'),
                                            200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;"\
    "-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = login_session.get('credentials')
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
@app.route('/index')
def main():
    make = session.query(Make)
    return render_template('index.html', make=make)


@app.route('/make/<int:make_id>/')
# Displays all Models for a Make based on make ID
def showModels(make_id):
    model = session.query(Model).filter_by(make_id=make_id)
    return render_template('model.html', make_id=make_id, model=model)


@app.route('/make/<int:make_id>/new/', methods=['GET', 'POST'])
# Allows user to create new models for each make
def newModel(make_id):
    if "username" not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        new_model = Model(name=request.form["model"], picture_url=request.form[
                          "image_url"], make_id=make_id)

        session.add(new_model)
        session.commit()

        # This query retreives the model that was just inserted
        car = session.query(Model).order_by(Model.id.desc()).first()

        # Inserts specs into Specs table for new model based on it's ID
        new_specs = Specs(price=request.form["price"],
                          hp=request.form["hp"], mpg=request.form["mpg"],
                          make_id=make_id, car_id=car.id)

        session.add(new_specs)
        session.commit()
        return redirect(url_for('showModels', make_id=make_id))
    else:
        return render_template('new_model.html', make_id=make_id)


@app.route('/make/<int:make_id>/specs/<int:car_id>/edit',
           methods=['GET', 'POST'])
# Allow user to edit model data
def editModel(make_id, car_id):
    if "username" not in login_session:
        return redirect('/login')
    model = session.query(Model).filter_by(id=car_id).one()
    specs = session.query(Specs).filter_by(make_id=make_id,
                                           car_id=car_id).one()
    if request.method == 'POST':
        if request.form['model']:
            model.name = request.form['model']
        if request.form['image_url']:
            model.picture_url = request.form['image_url']
        if request.form['price']:
            specs.price = request.form['price']
        if request.form['mpg']:
            specs.mpg = request.form['mpg']
        if request.form['hp']:
            specs.hp = request.form['hp']
        session.add(model)
        session.commit()
        session.add(specs)
        session.commit()
        return redirect(url_for('showModels', make_id=make_id))
    else:
        return render_template(
            'edit_model.html', make_id=make_id, car_id=car_id,
            model=model, specs=specs)


@app.route('/make/<int:make_id>/specs/<int:car_id>/delete',
           methods=['GET', 'POST'])
# Allow user to delete model
def deleteModel(make_id, car_id):
    if "username" not in login_session:
        return redirect('/login')
    model = session.query(Model).filter_by(id=car_id).one()
    specs = session.query(Specs).filter_by(make_id=make_id,
                                           car_id=car_id).one()
    if request.method == 'POST':
        session.query(Model).filter_by(id=car_id).delete()
        session.commit()
        session.query(Specs).filter_by(make_id=make_id,
                                       car_id=car_id).delete()
        session.commit()

        return redirect(url_for('showModels', make_id=make_id))
    else:
        return render_template(
            'delete_model.html', make_id=make_id, car_id=car_id,
            model=model, specs=specs)


@app.route('/make/<int:make_id>/specs/<int:car_id>/')
# Displays specs for each model
def showSpecs(make_id, car_id):
    model = session.query(Model).filter_by(id=car_id).one()
    specs = session.query(Specs).filter_by(car_id=car_id)
    return render_template('spec.html', specs=specs, model=model)


@app.route('/make/<int:make_id>/JSON')
# Create JSON displayig each model based on make ID
def showModelsJSON(make_id):
    items = session.query(Model).filter_by(make_id=make_id).all()
    return jsonify(Models=[i.serialize for i in items])


@app.route('/make/<int:make_id>/specs/<int:car_id>/JSON')
# Create JSON displaying specs for each model based on make ID and car ID
def showSpecsJSON(make_id, car_id):
    model = session.query(Model).filter_by(id=car_id).one()
    items = session.query(Specs).filter_by(car_id=car_id).all()
    return jsonify(Specs=[i.serialize for i in items])


@app.route('/clearSession')
# Clears user session
def clearSession():
    login_session.clear()
    return "Session cleared"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
