'''
-> None is a predefined value from None data type like True, False.
-> None is nothing but no value.
-> This category contains name as "NoneType".
-> None is a keyword in python and it is having some predefined value for None type data type. Hence "None" cannot be used as variabl.
    Example: None=20----> Here we get an error because None is keyword in python and there is one rule in python for creating variables
    like keywords must not be used as variables.
-> An object of None type cannot be created since it is a value.
-> The value is not False, space, empty.
-> None is used to create a variable without assaign a value to a variable.
-> None is used to nullify the object, means we are assigning the "None" value to the varible indicates the variable is not more in use
and treated as unused oject and it is removed from the main memory space by the garbage collector.
'''

a=55.0
print(a,type(a),id(a))
a=None
print(a,type(a),id(a))
