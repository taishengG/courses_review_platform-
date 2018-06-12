from model import AppModel
from ML import Ml

'''
model = AppModel()
print(model.fetchall())
value = ('CS410', 'spring 2018', '1:00~2:00', 'me', '5/5', '2/5', 'very good')
model.insert_course(value)
print(model.fetchall())
model.update_difficulty('200', 1)
print(model.fetchall())
'''
ml = Ml()
temp = 'i am good'
ml.sentiment_text(temp)
ml.sentiment_text('I am good')
