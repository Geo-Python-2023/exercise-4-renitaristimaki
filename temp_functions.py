#Fahrenheit to Celsius converter

def fahr_to_celsius(temp_fahrenheit):
    '''
Convert fahrenheit to celsius

Parameter: temp_fahrenheit(float), temperature in Fahrenheits
Returns: temperature converted to degrees Celsius
    '''
    return (temp_fahrenheit - 32) /1.8

#Reclassifying into integer classes 0-3 based on temperature

def temp_classifier (temp_celsius):
    
    '''Reclassifyes the temperature value in an integer class 0-3 based on following criteria:
0 Temperatures below -2 degrees Celsius
1 Temperatures equal or warmer than -2, but less than +2 degrees Celsius
2 Temperatures equal or warmer than +2, but less than +15 degrees Celsius
3 Temperatures equal or warmer than +15 degrees Celsius

Parameter: temp_celsius(float), temperature in Celsius degrees

Returns: integer class from 0-3
    '''

    if temp_celsius < -2:
        return 0
    if temp_celsius >= -2 and temp_celsius < 2:
        return 1
    if temp_celsius >= 2 and temp_celsius < 15:
        return 2
    if temp_celsius >= 15:
        return 3