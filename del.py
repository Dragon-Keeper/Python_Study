def fahrenheit_converter(C):
     fahrenheit = C * 9/5 + 32
     return int(fahrenheit)

b = fahrenheit_converter(20)
print(fahrenheit_converter(5))
print(b)
a = fahrenheit_converter(5)
print(type(b))
