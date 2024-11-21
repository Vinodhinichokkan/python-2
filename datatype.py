#string data type

# literal assignment

first_name = "vino"
last_name = "abi"

print(type(first_name))            #<class 'str>
print(type(first_name) == str)     #true
print(isinstance(first_name,str))  #true    


#concatenation

full_name = first_name + " " + last_name
print(full_name)