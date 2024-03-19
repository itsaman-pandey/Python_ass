# Write two functions named celsiusToFahrenheit and fahrenheitToCelsius to convert between Celsius and Fahrenheit.

# Use the functions to convert a given temperature.

def c_to_f( c):
    f = (c * 9/5) + 32
    return f
def f_to_c(f):
    c = (f-32)*5/9
    return c

