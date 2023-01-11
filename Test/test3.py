def timeConversion(string):
    time_hour = int(string[:2]) # GET HOUR VALUE IN NUMBER FORMAT
    time_minsecs = string[2:8] # GET MINUTES AND SECONDS VALUE
    time_format = string[8:] # GET TIME FORMAT
    
    if time_format == 'AM':
        if time_hour == 12:
            time_hour = 0
    elif time_format == 'PM':
        if time_hour < 12:
            time_hour += 12
            
    if time_hour < 10:
        time_hour = '0'+str(time_hour) # Add 0 if time hour is one digit
        
    print(str(time_hour)+time_minsecs) # Combine the hour value with minutes and seconds value

str1 = '07:05:45PM'
str2 = '12:00:01AM' # 00:00:00
str3 = '12:05:00PM' # 12:00:00
print(str1)
timeConversion(str1)