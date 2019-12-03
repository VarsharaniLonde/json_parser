class CustomJsonParser:
    """
    Should take a string when initializing the class, convert it to json and
    return the json object on CustomJsonParser(jsonString).parse()
    """

    def __init__(self, jsonString):
        self.jsonString = jsonString
        self.jsonParsed = dict()
        """
        Write your code here
        """
        pass


    def parse_value(self, value):
        """
        This function accepts a string value and parses it to its typecasts type
        """
        
        if type(value) == type([]) or type(value) == type({}):
            value1 = value
        else:
            strip_value = value.strip().strip('"')
            
            if strip_value.isdigit() is True:
                value1 = int(strip_value)

            elif strip_value.lower() == "false":
                value1 = False
            elif strip_value.lower() == "true":
                value1 = True
            elif strip_value.lower() == "null":
                value1 = None
            else:
                value1 = strip_value
        return value1

    def parse_list_data(self, index):
        """
        This function parses a list value
        """
        value_array = []
        parsed_value_array = []
        array_element = ""
        for i in range(index+1, len(self.jsonString)):
            # ',' implies key value pair completion hence value is added into the list
            if self.jsonString[i] == ',':
                array_element1 = self.parse_value(array_element)
                value_array.append(array_element1)
                array_element = ""
                continue
            # if ']' is encountered then its the completion of the list and hence list value is returned
            elif self.jsonString[i] == ']':
                array_element1 = self.parse_value(array_element)
                value_array.append(array_element1)
                # for item in range(0, len(array_element)):
                #     parsed_value_array.append(self.parse_value(item))
                return value_array, i+1     

            else:
                # if none of the above cases then it's a list element
                array_element += self.jsonString[i]

    def parse_string_data(self, i=0):
        
        """
        This function accepts an index 'i' which is 0 by default and parses the string starting from index 'i'
        and converts it into a json
        """

        jsonParsed = dict()
        bracket_count = 0
        key, value = "", ""
        kFlag, vFlag = False, False
        
        
        while i < len(self.jsonString):
            
            if self.jsonString[i] == '"' or self.jsonString[i] == '\n':
                i+=1
                continue
            elif self.jsonString[i] == '{':
                bracket_count += 1 
                kFlag, vFlag = True, False
                
                if bracket_count > 1:
                    
                    value, i = self.parse_string_data(i)  
                i+=1
                continue
            elif self.jsonString[i] == '[':
                # function call to parse a list as the value
                value, index = self.parse_list_data(i)
                value = self.parse_value(value) 
                i=index
                continue
            
            
            elif self.jsonString[i] == ':':
                # if two colons then the input is faulty so exit
                if vFlag is True:
                    print("INVALID JSON")
                    exit()
                vFlag, kFlag = True, False 
                i+=1
                continue
            
            elif self.jsonString[i] == ',' or self.jsonString[i] == '}':
                key1 = key.strip()
                value1 = self.parse_value(value)
                
                jsonParsed[key1] = value1
                kFlag, vFlag = True, False
                if self.jsonString[i] == '}':
                    return jsonParsed,i
                key, value = "", "" 
                i+=1
                continue

                # if a character is none of the above special characters, 
                # then it is a part of a key or value, hence the else block
            else:
                
                if kFlag is True:
                    key+=self.jsonString[i]
                    
                elif vFlag is True:
                    if type(value) == type([]):
                        i+=1
                        continue

                    value+=self.jsonString[i]
                    
                i+=1

        
        print("INVALID JSON")
        

    def parse(self):
        # This function returns the parsed json
        self.jsonParsed, i = self.parse_string_data()

        """
        Dont touch the return statement, your code will be evaluated by the return value of this function
        """
        return self.jsonParsed
        



