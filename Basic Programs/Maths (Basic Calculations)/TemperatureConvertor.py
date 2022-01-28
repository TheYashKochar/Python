# Converting to Fahrenheit to Celcius and Kelvin
print('Welcome to the Temperature Convertor!')
temp=input('Enter the Temperature in Fahrenheit : ')
celc=round(((float(temp)-32)*5)/9,4)
print('Temperature in Fahrenheit : '+ str(temp))
print('Temperature in Celcius : '+ str(celc))
print('Temperature in Kelvin : '+ str(celc+273.15))