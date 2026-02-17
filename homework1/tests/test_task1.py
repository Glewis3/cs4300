import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task1

def test_hello_world(capsys):
    # run the main function from task1
    task1.main()
    
    # capture the output straight from the console
    captured = capsys.readouterr()
    
    # verify that it matches exactly 
    assert captured.out == "Hello, World!\n"