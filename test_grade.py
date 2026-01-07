import subprocess
import sys

# UNIT TESTS FOR calculate_grade

def test_grade_A():
    from student import calculate_grade
    assert calculate_grade(95) == "A"


def test_grade_B():
    from student import calculate_grade
    assert calculate_grade(85) == "B"


def test_grade_C():
    from student import calculate_grade
    assert calculate_grade(70) == "C"


def test_grade_D():
    from student import calculate_grade
    assert calculate_grade(60) == "D"


def test_grade_F():
    from student import calculate_grade
    assert calculate_grade(45) == "F"


# INTEGRATION TEST (FULL SCRIPT RUN)

def test_student_program():
    result = subprocess.run(
        [
            sys.executable,
            "student.py"
        ],
        input="Pallavi Patil\n"
              "Sanjana Kulkarni\n"
              "78\n"
              "92\n"
              "45\n",
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Pallavi Patil" in result.stdout
    assert "Sanjana Kulkarni" in result.stdout
    assert "Grade B" in result.stdout
    assert "Grade A" in result.stdout
    assert "Grade F" in result.stdout