import pytest

def create_new_classroom:
    '''
    Instantiate a classroom Class and check if the classroom has 
    an empty schedule dictionary and an empty list for both students
    and assignments.
    '''
    classroom = Classroom("CS1")
    assert classroom.name               == "CS1"
    assert bool(classroom.schedule)     == False
    assert bool(classroom.students)     == False
    assert bool(classroom.assignments)  == False

