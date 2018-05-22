from IModel import IModel

class AppModel(IModel):
    """
    dataBase is a list of course
    dataBase = [<course1>, <course2>, <course3> ...]


    course dict looks like this:
    {
        'course_name' : 'CS410 Internet and Cloud Systems', 
        'term' : 'Spring 2018',
        'time' : 'TR 14:00~15:50',
        'instructor' : 'Wu-chang Feng',
        'rating' : '4.5/5',
        'difficulty' : '4.5/5',
        'review' : 'Lots of works'
    }
    """
    
    dataBase = []
    def fetchall(self):
        return self.dataBase



    def insert_course(self, values):
        course_dict = {
            'course_name' : values[0], 
            'term' : values[1],
            'time' : values[2],
            'instructor' : values[3],
            'rating' : values[4],
            'difficulty' : values[5],
            'review' : values[6]
        }
        self.dataBase.append(course_dict)
        return True


    # For uses' convinence, id starts from 1
    # id-1 is the index of the course in dataBase
    def delete_course(self, course_name, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            if self.dataBase[id-1]['course_name'] == course_name:
                del self.dataBase[id-1]
                return True
        return False


    def add_review(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['review'].append(values)
            return True
        return False
        

    def update_name(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['name'] = values
            return True
        return False

    def update_term(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['term'] = values
            return True
        return False


    def update_time(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['time'] = values
            return True
        return False

    def update_instructor(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['instructor'] = values
            return True
        return False


    def update_rating(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['rating'] = values
            return True
        return False


    def update_difficulty(self, values, id):
        if id-1 >= 0 and id-1<len(self.dataBase):
            self.dataBase[id-1]['difficulty'] = values
            return True
        return False


