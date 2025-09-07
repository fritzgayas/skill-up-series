# If you still don't have a venv, it is recommended to create venv using the command "python -m venv pytestenv"
# Activate venv with the command ".\pytestenv\Scripts\Activate"

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError
        #raise ZeroDivisionError("division by zero is not allowed")
    return a / b