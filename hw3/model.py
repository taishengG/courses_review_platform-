from IModel import IModel
import sqlite3

class AppModel(IModel):
    """
    course dict looks like this:
    {
        'id' : 1,
        'course_name' : 'CS410 Internet and Cloud Systems', 
        'term' : 'Spring 2018',
        'time' : 'TR 14:00~15:50',
        'instructor' : 'Wu-chang Feng',
        'rating' : '4.5/5',
        'difficulty' : '4.5/5',
        'review' : 'Lots of works'
    }
    """

    DB_FILE = 'entries.db'

    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from courses")
        except sqlite3.OperationalError:
            cursor.execute("courses table courses (id int, course_name text, term text, time text, instructor text, rating int, difficulty int, review text)")
        cursor.close()

    
    def fetchall(self):
        """
        Gets all entries from the database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()



    def insert_course(self, values):
        """
        Inserts entry into database
        """
        params = {'id':values[0], 'course_name':values[1], 'term':values[2], 'time':values[3], 'insturctor':values[4]. 'rating':values[5], 'difficulty':values[6], 'review':values[7]}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into courses (id, course_name, term, time, instructor, rating, difficulty, review) VALUES (:id, :course_name, :term, :time, :instructor, :rating, :difficulty, :review)", params)

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


