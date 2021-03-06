from IModel import IModel
import sqlite3
from datetime import datetime


class AppModel(IModel):
    """
    course dict looks like this:
    {
        'course_name' : 'CS410 Internet and Cloud Systems', 
        'term' : 'Spring 2018',
        'time' : 'TR 14:00~15:50',
        'instructor' : 'Wu-chang Feng',
        'rating' : '4.5/5',
        'difficulty' : '4.5/5',
        'review' : 'Lots of works'
        'edit_time' : '2018-05-09 17:45:35'
    }
    """


    def __init__(self):
        # Make sure our database exists

        self.DB_FILE = 'entries.db'
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from courses")
        except sqlite3.OperationalError:
            cursor.execute("create table courses (course_name text, term text, time text, instructor text, rating int, difficulty int, review text, edit_time datetime)")
        cursor.close()
        #print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    
    def fetchall(self):
        """
        Gets all entries from the database
        """
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM courses ORDER BY edit_time DESC")
        return cursor.fetchall()



    def insert_course(self, values):
        """
        Inserts entry into database
        """
        params = {'course_name':values[0], 'term':values[1], 'time':values[2], 'instructor':values[3], 'rating':values[4], 'difficulty':values[5], 'review':values[6], 'edit_time':datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        connection = sqlite3.connect(self.DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into courses (course_name, term, time, instructor, rating, difficulty, review, edit_time) VALUES (:course_name, :term, :time, :instructor, :rating, :difficulty, :review, :edit_time)", params)
        connection.commit()
        cursor.close()


    # For uses' convinence, id starts from 1
    def delete_course(self, course_name, id):
        pass


    def add_review(self, values, id):
        pass
        

    def update_name(self, values, id):
        pass

    def update_term(self, values, id):
        pass


    def update_time(self, values, id):
        pass

    def update_instructor(self, values, id):
        pass


    def update_rating(self, values, id):
        pass


    def update_difficulty(self, values, id):
        pass


