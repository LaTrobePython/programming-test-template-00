import pytest
import submission

def test_calculate_total_cost_default_tax():
    assert round(submission.calculate_total_cost(10, 3), 2) == 33.0

def test_calculate_total_cost_custom_tax():
    assert round(submission.calculate_total_cost(10, 3, 0.155), 2) == 34.65

def test_celsius_to_fahrenheit_freezing():
    assert round(submission.celsius_to_fahrenheit(0), 2) == 32.0

def test_celsius_to_fahrenheit_boiling():
    assert round(submission.celsius_to_fahrenheit(100), 2) == 212.0

def test_student_class_initialization():
    student = submission.Student("Test", "ID123")
    assert student.name == "Test"
    assert student.student_id == "ID123"
    assert student.grades == []

def test_student_add_grade():
    student = submission.Student("Test", "ID123")
    student.add_grade(75)
    assert student.grades == [75]

def test_student_get_average():
    student = submission.Student("Test", "ID123")
    student.add_grade(65)
    student.add_grade(70)
    student.add_grade(85)
    assert round(student.get_average(), 2) == 73.33

def test_student_is_passing_fail():
    student = submission.Student("Test", "ID123")
    student.add_grade(40)
    student.add_grade(45)
    assert student.is_passing() == False

def test_student_is_passing_pass():
    student = submission.Student("Test", "ID123")
    student.add_grade(40)
    student.add_grade(45)
    student.add_grade(75)
    assert student.is_passing() == True
