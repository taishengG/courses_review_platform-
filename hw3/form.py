from wtforms import Form, StringField, TextAreaField, IntegerField, PasswordField, validators

#Course Form
class CourseForm(Form):
    course_name = StringField('Course name', [validators.Length(min=1,max=200)])
    term = StringField('Term', [validators.Length(min=1,max=200)])
    time = StringField('Time', [validators.Length(min=1,max=200)])
    instructor = StringField('Insturctor', [validators.Length(min=1,max=200)])
    rating = IntegerField('Rating', [validators.NumberRange(message='Between 1 and 5.',min=1, max=5)])
    difficulty = IntegerField('Difficulty', [validators.NumberRange(message='Between 1 and 5.', min=1, max=5)])
    review = TextAreaField('Review', [validators.Length(min=10)])
