from flask import Blueprint, render_template
from App.ext import model
from App.model_forest import Forest_park

blue = Blueprint('first_blue', __name__)


def init_first_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/add/')
def add_liu():
    res4 = model.session.query(Forest_park).order_by('area_ha').filter_by(Province="山东").all()
    model.session.commit()
    print(res4[0].Province)
    return render_template('pie.html', res4=res4)


@blue.route('/get')
def get_data():
    res = model.session.query(Forest_park).filter_by(Province='山东').all()
    model.session.commit()
    return render_template('index.html', res=res)


@blue.route('/get_min')
def get_min():
    res2 = model.session.query(Forest_park).filter_by(Province="山东").order_by(Forest_park.area_ha).limit(5)
    model.session.commit()
    res3 = model.session.query(Forest_park).filter_by(Province="山东").order_by(Forest_park.area_ha.desc()).limit(5)
    model.session.commit()
    print(res2)
    return render_template('line.html', res2=res2, res3=res3)
