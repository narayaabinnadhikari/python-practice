
# 1. literal assignment
first = "Nabin"
last = "Adhikari"

# to check the data types use following
print(type(first))
print(type(first) == str)
print(isinstance(first, str))


# 2. constructor function
pizza = str("Pepperoni")

# 3. Concatenation
fullname = first + " " + last
print(fullname)

fullname += " are you!!"
print(fullname)

# 4. Casting a Number to a String
decade = str(1970)
print(type(decade))
print(decade)

statement = "I like movies from the " + decade + "s." 
print(statement)

# 5. Multiple Lines
multiline = """
 Hey, how are you ?   

 I was just checking in.  
                        All good ?

"""
print(multiline)

# 6. Escaping special characters
sentence = "I\'m back at work!\tHey!\n\nWhere\'s this at\\located?"
print(sentence)

