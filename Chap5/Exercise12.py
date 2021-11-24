def celsius_to_fahrenheit(celsius_float):
   """ COnvert Celsius to Fahrenheit."""
   return celsius_float * 1.8 + 32

print("COnvert Celsius to Fahrenheit.")
celsius_float = float(input("Enter a Celsius temp: "))
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
print(celsius_float," convert to ",fahrenheit_float," Fahrenheit")
