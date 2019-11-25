from App.ext import model


class Student(model.Model):
    id = model.Column(model.Integer, primary_key=True, autoincrement=True)
    s_name = model.Column(model.String(16))


