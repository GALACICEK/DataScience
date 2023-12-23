
""" 
import pandas as pd #top level code

df = pd.DataFrame([1,2])

print("this is my module") #top level code
print(__name__)
print(pd.__name__)


from datetime import timezone
import datetime  

print(timezone.__name__)
print(datetime.__name__)

"""


def my_function():
    print("Hello")

def call_api(request):
    pass

if __name__ == "main":
    my_function()
    request = ""
    call_api(request)