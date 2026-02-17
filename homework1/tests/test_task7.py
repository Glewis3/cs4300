import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task7

def test_website_status():
    # google should always return 200 
    status = task7.check_website_status("https://www.google.com")
    assert status == 200

def test_invalid_url():
    # an invalid URL should handle the exception correctly
    status = task7.check_website_status("https://tdefejfnde.com")
    assert status is None