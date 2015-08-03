from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Make, Model, Specs
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///car.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/index')
def main():
    make = session.query(Make)
    return render_template('index.html', make=make)


@app.route('/make/<int:make_id>/')
def showModels(make_id):
    model = session.query(Model).filter_by(make_id=make_id)
    return render_template('model.html', make_id=make_id, model=model)


@app.route('/make/<int:make_id>/new/', methods=['GET', 'POST'])
def newModel(make_id):
    if request.method == 'POST':
        new_model = Model(name=request.form["model"], picture_url=request.form[
                          "image_url"], make_id=make_id)

        entries = session.query(Model).count()
        car_id = entries + 1
        new_specs = Specs(price=request.form["price"],
                          hp=request.form["hp"], mpg=request.form["mpg"],
                          make_id=make_id, car_id=car_id)

        session.add(new_model)
        session.commit()
        session.add(new_specs)
        session.commit()
        return redirect(url_for('showModels', make_id=make_id))
    else:
        return render_template('new_model.html', make_id=make_id)


@app.route('/make/<int:make_id>/specs/<int:car_id>/edit',
           methods=['GET', 'POST'])
def editModel(make_id, car_id):
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
def deleteModel(make_id, car_id):
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
def showSpecs(make_id, car_id):
    model = session.query(Model).filter_by(id=car_id).one()
    specs = session.query(Specs).filter_by(car_id=car_id)
    return render_template('spec.html', specs=specs, model=model)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
