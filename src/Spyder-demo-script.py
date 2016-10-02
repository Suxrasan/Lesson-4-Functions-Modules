
def celisius_to_farh(temp_c):
#Function to convert Celsius temperature to Fahrenheit. 
	return 9/5 * temp_c + 32 

def kelvin_to_celsius(temp_k):
#Function to convert Kelvin temperature to Celsius.
	return temp_k - 273.15

def kelvin_to_farhenheit(temp_k):
#Function to convert Kelvin temperature to Fahrenheit. 
	#Kelvin in celsius
	temp_c = kelvin_to_celsius(temp_k)
	#Celsius in Fahrenheit
	temp_f = celsius_to_fahr(temp_c)
	#Return the result
	return temp_f

def celsius_to_kelvin(temp_c): 
	#Kelvin = Celsius - 273.15 
	temp_k = temp_c + 273.15
	return temp_k

def fahr_to_celsius(temp_f):
	#Celsius = (Fahrenheit - 32) * 5/9
	temp_c = (temp_f - 32) * 5/9 
	return temp_c

def fahr_to_kelvin(temp_f):
	# Kelvin = (Fahrenheit - 459.67) * 5/9
	temp_k = (temp_f + 459.67) * 5/9
	return temp_k


print('32 Fahrenheits is in Celsius:', fahr_to_celsius(32))
print('100 Celsius is in Kelvin:', celsius_to_kelvin(temp_c=100))
print('50 Fahrenheits is in Kelvin:', fahr_to_kelvin(temp_f=50))
