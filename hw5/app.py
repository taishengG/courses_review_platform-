from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functools import wraps
import requests



from presenter import Presenter
from model import AppModel


app = Flask(__name__)
model = AppModel()
value1 = ('CS410 Web Security', 'Winter 2018', 'TR 14:00~15:50', 'Wu-chang Feng', '4.5/5', '3.5/5', "Web Security was fun and I learned a ton! This should be a required class. Wu Chang does and excellent job teaching it as well and is very helpful in and out of class. Not a tough grader and lenient if you talk to him about missing classes. There is a ton of work though for this class, so be prepared to put in the time! I'm happy I took this class!")

value2 = ('CS201', 'Fall 2014', 'MW 10:00~11:50', 'Wu-chang Feng', '3/5', '3/5', "Professor Feng was a great professor. He is extremely knowledgeable, welcomes questions, and loves his material. The CTF homework makes the class enjoyable and was a good learning tool. Be prepared to spend a lot of time looking at assembly code.")

value3 = ('CS202', 'Fall 2018', '13:00~15:50', 'Karla Fant', '5/5', '4/5', "Took 163 and 202. Excellent teacher. Very engaging, in depth lectures. Love the fact that she put in labs, helps me practice what I learned in class. Responsive to emails! But if you fail ONE assignment, exam, or demo tho you insta fail. However I've graders are pretty lenient for programs-as long it works it basically passes. But exams are hard!")

model.insert_course(value1)
model.insert_course(value2)
model.insert_course(value3)

'''
model.insert_course(model, value1)
model.insert_course(model, value2)
model.insert_course(model, value3)
'''
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
