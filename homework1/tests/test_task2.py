import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task2

def test_data_types():
    # check integer function
    assert isinstance(task2.get_integer(), int)    
    # check the float function 
    assert isinstance(task2.get_float(), float)   
    # check the string function
    assert isinstance(task2.get_string(), str)   
    # check the boolean function
    assert isinstance(task2.get_boolean(), bool)