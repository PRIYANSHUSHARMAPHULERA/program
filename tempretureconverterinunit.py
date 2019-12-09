a=input('Choose the temperature unit in which you want to change in °C(type C or c) or °F(type F or f)')
if(a.upper()=='F'):
    b=float(input('Enter temperature in Celsius:\t'))
    c=((b*9)/5)
    print('Fahrenheit temperature is:\t',(c+32))
elif(a.upper()=='C'):
    d=float(input('Enter temperature in Fahreheit:\t'))
    e=(d-32)
    print('Celsius temperature is:\t',(e*0.5556))
else:
    print('!!!!!!!........Enter valid input')
    
