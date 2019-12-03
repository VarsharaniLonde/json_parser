from question import CustomJsonParser
import json


class TestCustomJsonParser:
    """
    The test case will run against your CustomJsonParser.
    You can run this file to check if your code is working correct.
    DONT MODIFY THIS FILE.
    """
    inputs = [
    """{
        "simple2":                  false
    }""",

    """{
        "simple1" : [1, 2]
        }""", 
    """
    {
	"simpleWithTabNoSpace": null
    }
    """,
    """{
"name" : "John Doe",
"age" : 32,
"address" : ["#619","Koramangala 1st block","bangalore - 512082"],
"married" : false,
"preferences":{
    "food" : "veg",
    "beverages" : ["coffee", "fanta"],
    "cuisine" : "chinese",
    "smoking" : false
},
"working": true
}"""
    ]

    def __init__(self):
    	for string in self.inputs:
    		loaded_json = json.loads(string)
            

    		try:
    			assert CustomJsonParser(string).parse() == loaded_json
    		except AssertionError:
    			print("The string parsing for the following string is wrong")
    			print("*"*40)
    			print(string)
    			print("\n"*3)
    			print("Your answer: \n")
    			print(CustomJsonParser(string).parse())
    			print("\n"*3)
    			print("Expected: \n")
    			print(loaded_json)
    			break
    		print("Passed :%s "% loaded_json)


TestCustomJsonParser()