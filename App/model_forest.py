from App.ext import model


class Forest_park(model.Model):
    num = model.Column(model.Integer, primary_key=True)
    Province = model.Column(model.Text)
    manager = model.Column(model.Text)
    name = model.Column(model.Text)
    name_short = model.Column(model.Text)
    time = model.Column(model.String)
    area_ha = model.Column(model.String)
    county = model.Column(model.Text)
    bd_lon = model.Column(model.String)
    bd_lat = model.Column(model.String)
    lon = model.Column(model.String)
    lat = model.Column(model.String)
