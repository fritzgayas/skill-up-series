"""
Pytest tests for the Classroom system (Mapúa University — Computer Engineering).

This file uses:
 - fixtures for reusable setup
 - parametrize for testing multiple inputs
 - raises to check exception behavior
 - a marked integration test
"""

import pytest
from source.university import Classroom, Teacher, Student, TooManyStudents

# Fixtures (setup helpers)
@pytest.fixture
def default_teacher():
    """Return a themed teacher instance for Mapúa CpE."""
    return Teacher("Engr. Dela Cruz - Mapúa University, CpE Department")


@pytest.fixture
def initial_students():
    """Return 5 initial students (a small CpE group)."""
    return [Student(f"CpE Student {i}") for i in range(1, 6)]


@pytest.fixture
def classroom(default_teacher, initial_students):
    """Create a Classroom with teacher + 5 students + a course title."""
    return Classroom(default_teacher, initial_students, "CPE101 - Computer Engineering as a Discipline")

# Tests
def test_initial_setup(classroom, default_teacher, initial_students):
    """Verify classroom starts with the correct teacher, students, and title."""
    assert classroom.teacher == default_teacher
    assert classroom.students == initial_students
    assert classroom.course_title == "CPE101 - Computer Engineering as a Discipline"

@pytest.mark.parametrize("student_name", ["Juan Dela Cruz", "Maria Clara", "Jose Rizal"])
def test_add_student_under_limit(classroom, student_name):
    """Adding students while under capacity should succeed."""
    new_student = Student(student_name)
    classroom.add_student(new_student)
    assert new_student in classroom.students

def test_add_student_over_limit(classroom):
    """
    Fill the classroom up to capacity (10). Then adding one more should raise.
    NOTE: we use '< 10' to fill to exactly 10 students (0..9 allowed additions).
    """
    # Fill until we have 10 students in total
    while len(classroom.students) < 10:
        classroom.add_student(Student(f"CpE Student {len(classroom.students) + 1}"))

    assert len(classroom.students) == 10  # now full

    # The next add should raise
    with pytest.raises(TooManyStudents, match="limit reached"):
        classroom.add_student(Student("Overloaded Student"))


def test_remove_student(classroom):
    """Removing a student by name should remove that student object from the list."""
    student_to_remove = classroom.students[0]
    classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in classroom.students


def test_change_teacher(classroom):
    """Changing the teacher should update the teacher attribute."""
    new_teacher = Teacher("Dr. Reyes - Mapúa CpE Department")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher


@pytest.mark.integration
def test_classroom_flow(default_teacher):
    """
    Integration-style test:
    1) Create a class with exactly 10 students (capacity).
    2) Confirm adding the 11th student raises TooManyStudents.
    3) Remove one student and add a replacement successfully.
    """
    students = [Student(f"Batch 2021 CpE Student {i}") for i in range(1, 11)]
    classroom = Classroom(default_teacher, students, "CPE108 - Microprocessors")
    assert len(classroom.students) == 10

    # Adding an 11th should now raise (capacity enforced to 10).
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Extra Student"))

    # Remove one and add a replacement
    classroom.remove_student("Batch 2021 CpE Student 5")
    replacement = Student("Late Enrollee")
    classroom.add_student(replacement)
    assert replacement in classroom.students