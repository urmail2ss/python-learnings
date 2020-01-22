# Strings
# 

# String can be using either inside single quotes or double quotes
print('Using String in single quotes');
print('----------------------------------');
print("Using String in double quotes");
print('----------------------------------');

# String can be used in multiline split using ''' (triple quotes)
print(''' 

Printing 

long strings using 

triple quoted 

on multiple lines in codes

''');
print('----------------------------------');
#String Escape
print("Hi, I am excaping double quotes \" char ");

print('----------------------------------');
# String Formattings

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

print('----------------------------------');
# String concatenation
# Can done only with other string not with other datatype
# If want to concatenate need cast to string
first_name = 'Shan'
last_name = 'Nat'
print('Example of String concatenation ' + first_name + " " + last_name);


print('----------------------------------');
print('String concatenation only with string not with other data type ' + first_name + " " + last_name + 'age ' + 10);


