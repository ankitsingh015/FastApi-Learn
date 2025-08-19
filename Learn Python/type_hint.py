# A type hint in Python is a way to indicate the expected data type of 
            # a variable, 
            # function argument, or 
            # return value. 
# It is not enforced at runtime, but serves as documentation for developers.


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e



# generic types with type parameters allow you to specify the type of elements 
# inside collections like lists, dictionaries, sets, etc. 
# This is done using the typing module.

from typing import List, Dict, Tuple
def process_items(items: List[str]):
    for item in items:
        print(item)

# Modern Syntax (Python 3.9+)

def process_items(items: list[str]):
    for item in items:
        print(item)
        
# You can declare that a variable can be any of several types, 
# for example, an int or a str. 
# for that you can use the Union type from the typing module 
# or the | operator in Python 3.10+.

def process_item(item: int | str):
    print(item)
    
# Possibly None
# declare that a value could have a type, like str, but that it could also be None.

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
        
        
# Classes as types

class User:
    def __init__(self, name: str):
        self.name = name


def create_user(one_person : User) -> User: 
    # you can declare a variable to be of type Person
    # Notice that this means "one_person is an instance of the class User".
    # It doesn't mean "one_person is the class called User".
    return one_person.name

# Type Hints with Metadata Annotations
# Python also has a feature that allows putting additional metadata in these type hints using Annotated

from typing_extensions import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
    

