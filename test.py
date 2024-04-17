# test.py
from easypy import execute

code = """
class Person:
    def greet(self):
        print("Hello, world!")

person = Person()
person.greet() * 3
"""
execute(code)
