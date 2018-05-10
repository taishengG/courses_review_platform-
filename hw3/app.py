from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functools import wraps
import requests



from model import AppModel
from presenter import Presenter
from form import CourseForm


app = Flask(__name__)
model = AppModel()
presenter = Presenter(model)

def create_template(route):
    route_name = route.get_name()

    if route.is_redirect():
        return redirect(url_for(route_name))
    else:
        route_arg = route.get_args()
        if (route_arg == None):                                                                              
            return render_template(route_name)
        return render_template(route_name, **(route_arg))

def present_flash(f):
    if (not (f == None)):
        flash(f.get_msg(), f.get_msg_type().value)

def render_view(view):
    present_flash(view.get_flash())
    return create_template(view.get_route())


@app.route('/')
def base():
    return render_template(presenter.base())

@app.route('/course')
def course():
    return render_view(presenter.course())

@app.route('/add_course', methods = ['POST', 'GET'])
def add_course():
    form = CourseForm(request.form)
    can_add = request.method == 'POST' and form.validate()
    return render_view(presenter.add_course(can_add, form))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=8000, debug=True)
