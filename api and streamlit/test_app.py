import pytest
from streamlit.testing.v1 import AppTest
import streamlit_main
def test_run_app():
    at = AppTest.from_file("streamlit_main.py")
    at.run()
    assert not at.exception

def test_title():
    at = AppTest.from_file("streamlit_main.py")
    at.run()
    assert at.title[0].value == 'Text translator in the Streamlit'
