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
    def contact(self):
        return 'contact.html'
    def course(self):
        '''courses = self.model.fetchall(self.model)'''
        courses = self.model.fetchall()

        if courses[0]:
            args = {'courses':courses}
            route = Route(False, 'course.html', args)
            return PresentView(route)
        else:
            msg = 'No Course Found'
            args = {'msg':msg}
            route = Route(False, 'course.html', args)
            return PresentView(route)

