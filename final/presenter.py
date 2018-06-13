from flask import session, logging, request
from passlib.hash import sha256_crypt
from functools import wraps

from view_header import Route, PresentView, Flash, MSG_TYPE



class Presenter:

#----- model is in English, trans_mode is in Chinese ------
    def __init__(self, model, trans_model):
        self.model = model
        self.trans_model = trans_model
#---------------------- end ------------------------


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
            args = {'courses':courses[:4]}
            route = Route(False, 'course.html', args)
            return PresentView(route)
        else:
            msg = 'No Course Found'
            args = {'msg':msg}
            route = Route(False, 'course.html', args)
            return PresentView(route)

#-------- This is prepared for course_2.html -----------
    def course_2(self):
        '''courses = self.model.fetchall(self.model)'''
        courses_2 = self.trans_model.fetchall()

        if courses_2[0]:
            args = {'courses':courses_2[4:]}
            route = Route(False, 'course_2.html', args)
            return PresentView(route)
        else:
            msg = 'No Course Found'
            args = {'msg':msg}
            route = Route(False, 'course_2.html', args)
            return PresentView(route)
#---------------------- end ----------------------------
