#importing modules
import requests,json, pprint
pp =pprint.PrettyPrinter(indent =4)

#type your API KEY Here.
api_key = "09d4916d61723eb6f4bd9b01105317c9"
base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="

#taking input "city name" from user
#city_name = input("Enter the city name: ")

#latitude/longitude
lat= -19.5665
long= 101.7068

#complete_url variable to store the complete_url address
complete_url = str(base_url + str(lat) + "&lon="+ str(long) +"&exclude={,minutely,hourly,alerts}&appid="+api_key)

#get methods of requests module retruns respons object
response = requests.get(complete_url)
code = response.status_code

#json method of response object convert json format data into python format data
x = response.json()
print (pp.pprint(x))
print (code)

#Now x contains list of nested dictionaries
#check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
if response.ok:
    #store the value of "main" key in variable y
    y = x["main"]

    #store the value coressponding to the "temp" key of y


    
    #store the value of "weather" key in variable z
    z= x["weather"]
    
    #store the value coressponding to the "description" key
    #at the 0th index of z
    weather_description = z[0]["description"]
    #print the following values  
    print(" Temperature(in kelvin unit)= " +
                       str(daily_weather) + 
                       "\n description = " +
                       str(weather_description))
else:
    print("City Not Found")                       