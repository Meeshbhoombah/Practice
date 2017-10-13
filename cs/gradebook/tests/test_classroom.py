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

def create_new_students:
    student = Student(first_name: "John", last_name: "Micheal")
    assert student.fullname        === "John Micheal"
    assert bool(student.schedule)  == False
    assert bool(student.classes)   == False

