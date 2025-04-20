import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from your_app import app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 3) == 2

    
