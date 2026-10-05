from library.hello import get_greeting

def say_hello():
    response = get_greeting()
    return f"The Python library says: '{response}'"

print(say_hello())
# making trivial edit to touch app main.py
# another touch to see it kick in... should only test app this time.