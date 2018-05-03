from abc import ABC, abstractmethod

class IModel(ABC):

    """
    Fetch all of the on the entries in the the database.
    return dictionary, all entries in the system
    """
    @abstractmethod
    def fetchall(self):
        pass


    """
    Insert a course.
    @params values all the require fields requred to insert a course
    return True if course was created, False otherwise
    """
    @abstractmethod
    def insert_course(self, values):
        pass

    """
    Delete course user reviewed.
    @params course_name name of the course
    @params id the unique id for the post course user wanted to delete
    return True if the post is deleted
    """
    @abstractmethod
    def delete_course(self, course_name, id):
        pass


    """
    Add review into a specific course.
    @params values all the field need for adding an review
    @params id the unique id for the post course user wanted to add review to
    return True if the review was added
    """
    @abstractmethod
    def add_review(self, values, id):
        pass

    """
    Edit the course name user wrote.
    @params values the field needed to update the name
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_name(self, values, id):
        pass

    """
    Edit the term user wrote.
    @params values the field needed to update the term
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_term(self, values, id):
        pass


    """
    Edit the time user wrote.
    @params values the field needed to update the time
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_time(self, values, id):
        pass

    """
    Edit the instructor user wrote.
    @params values the field needed to update the instructor
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_instructor(self, values, id):
        pass


    """
    Edit the rating user wrote.
    @params values the field needed to update the rating
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_rating(self, values, id):
        pass


    """
    Edit the difficulty user wrote.
    @params values the field needed to update the difficulty
    @params id the unique id for the post course user wanted to edit
    return True if updated in the database
    """
    @abstractmethod
    def update_difficulty(self, values, id):
        pass


