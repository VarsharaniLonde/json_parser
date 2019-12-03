# JsonParser.
* Given a string, convert it to json without using any third party library.
* Assume a simple JSON with basic data types: int, string, boolean and array - (no nested JSON inside array)


Sample input :
"""{
"name" : "John Doe",
"age" : 32,
"address" : ["#619, Koramangala 1st block","bangalore - 512082"],
"married" : false,
"preferences":{
    "food" : "veg",
    "beverages" : ["coffee", "fanta"]
    "cuisine" : "chinese",
    "smoking" : False,
}
}"""


The basic test cases are provided in the same directory. 

to run the test cases , use the following command

> python test.py

* Use python 3
* Your solution must build+run on Linux
* Test cases should pass.
* If you use any third party library, make sure you include it in the requirements.txt
=======
# json_parser
A parser to parse a string into a valid json without using any external libraries

