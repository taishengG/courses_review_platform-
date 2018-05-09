from flask import session, logging, request
from passlib.hash import sha256_crypt
from functools import wraps

from view_header import Route, PresentView, Flash, MSG_TYPE



class Presenter:

    def __init__(self, model):
        self.model = model


    def index(self):
        return 'index.html'
    def base(self):
        return 'base.html'
    def course(self):
        courses = self.model.fetchall(self.model)
        if courses[0]:
            args = {'courses':courses}
            route = Route(False, 'course.html', args)
            return PresentView(route)
        else:
            msg = 'No Course Found'
            args = {'msg':msg}
            route = Route(False, 'course.html', args)
            return PresentView(route)

    def add_course(self, can_add, form):
        if can_add:
            course_name = form.course_name.data
            term = form.term.data
            time = form.time.data
            instructor = form.instructor.data
            rating = form.rating.data
            difficulty = form.difficulty.data
            review = form.review.data

            '''self.model.add_art((title, body, session['username'], link))'''
            flash = Flash('Course created', MSG_TYPE.SUCCESS)
            route = Route(True, 'course')
            return PresentView(route, flash)
        args = {'form':form}
        route = Route(False, 'add_course.html', args)
        return PresentView(route)
