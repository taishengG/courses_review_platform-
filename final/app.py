from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from functools import wraps
import requests



from presenter import Presenter
from model import AppModel

import argparse
import sys

from google.cloud import language #Google sentiment analysis API, used by Taisheng Guo
from google.cloud import translate #Goole Translate API, used by Baiwei Yu
from google.cloud.language import enums
from google.cloud.language import types
import six

#--------- Sentiment analysis API, by Taisheng Guo's --------
def sentiment_text(text):
    """Detects sentiment in the text."""
    client = language.LanguageServiceClient()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    # [START migration_document_text]
    # [START migration_analyze_sentiment]
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # [END migration_document_text]

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    sentiment = client.analyze_sentiment(document).document_sentiment

    #print('Score: {}'.format(sentiment.score))
    #print('Magnitude: {}'.format(sentiment.magnitude))
    if sentiment.score > 0.5:
        return 'Good'
    elif sentiment.score == 0.5:
        return 'Normal'
    elif sentiment.score < 0.5 and sentiment.score > 0:
        return 'Not Very Well'
    else:
        return 'Bad'
    # [END migration_analyze_sentiment]
# ------------------- End of sentiment API  ----------------


#------- Google Translate API, by Baiwei Yu ----------------
def translate_text(target, text):
    # [START translate_translate_text]
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)

    return result['translatedText']
    #print(u'Text: {}'.format(result['input']))
    #print(u'Translation: {}'.format(result['translatedText']))
    #print(u'Detected source language: {}'.format(
        #result['detectedSourceLanguage']))
    # [END translate_translate_text]
#---------------- End of Google Tranlate API ----------------    


app = Flask(__name__)
model = AppModel()
trans_model = AppModel() #conent translated in Chinese


value1 = ('CS410 Web Security', 'Winter 2018', 'TR 14:00~15:50', 'Wu-chang Feng', '4.5/5', '3.5/5', "Web Security was fun and I learned a ton! This should be a required class. Wu Chang does and excellent job teaching it as well and is very helpful in and out of class. Not a tough grader and lenient if you talk to him about missing classes. There is a ton of work though for this class, so be prepared to put in the time! I'm happy I took this class!")

value2 = ('CS201', 'Fall 2014', 'MW 10:00~11:50', 'Wu-chang Feng', '3/5', '3/5', "Professor Feng was a great professor. He is extremely knowledgeable, welcomes questions, and loves his material. The CTF homework makes the class enjoyable and was a good learning tool. Be prepared to spend a lot of time looking at assembly code.")

value3 = ('CS202', 'Fall 2018', '13:00~15:50', 'Karla Fant', '5/5', '4/5', "Took 163 and 202. Excellent teacher. Very engaging, in depth lectures. Love the fact that she put in labs, helps me practice what I learned in class. Responsive to emails! But if you fail ONE assignment, exam, or demo tho you insta fail. However I've graders are pretty lenient for programs-as long it works it basically passes. But exams are hard!")

value4 = ('CS999', 'Fall 2028', '7:00~8:50', 'Unknow', '1/5', '1/5', "This class is very horrible. Tons of hw and exams, won't ever take it again!!!")

#------ Implement of sentiment analysis API, by Taisheng Guo ------
value1 = value1 + (sentiment_text(value1[6]),)
value2 = value2 + (sentiment_text(value2[6]),)
value3 = value3 + (sentiment_text(value3[6]),)
value4 = value4 + (sentiment_text(value4[6]),)
#------------------------------- end ------------------------------

#------ Implement of Google Translate API, by Baiwei Yu -----------
trans_value1 = ()
trans_value2 = ()
trans_value3 = ()
trans_value4 = ()

for x in value1:
	trans_value1 = trans_value1 +  (translate_text('zh', x),)
for x in value2:
	trans_value2 = trans_value2 +  (translate_text('zh', x),)
for x in value3:
	trans_value3 = trans_value3 +  (translate_text('zh', x),)
for x in value4:
	trans_value4 = trans_value4 +  (translate_text('zh', x),)
#------------------------------ end -------------------------------


model.insert_course(value1)
model.insert_course(value2)
model.insert_course(value3)
model.insert_course(value4)

#--- Add translated content to new model,by Baiwei Yu ----
trans_model.insert_course(trans_value1)
trans_model.insert_course(trans_value2)
trans_model.insert_course(trans_value3)
trans_model.insert_course(trans_value4)
#---------------------------------------------------------

'''
model.insert_course(model, value1)
model.insert_course(model, value2)
model.insert_course(model, value3)
'''
presenter = Presenter(model, trans_model) #presenter is modified to accepting two models. by Taisheng Guo

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

#----- Translated content is passed to course_2.html. by Taisheng Guo----
@app.route('/course_2')
def course_2():
    return render_view(presenter.course_2())
#-------- end----------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


