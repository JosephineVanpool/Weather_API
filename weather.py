#importing modules
import requests,json

#type your API KEY Here.
api_key = "09d4916d61723eb6f4bd9b01105317c9"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

#taking input "city name" from user
city_name = input("Enter the city name: ")
#complete_url variable to store the complete_url address
complete_url = str(base_url + city_name + "&appid=" + api_key)

#get methods of requests module retruns respons object
response = requests.get(complete_url)

#json method of response object convert json format data into python format data
x = response.json()

#Now x contains list of nested dictionaries
#check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
if x["cod"] != "404":
    #store the value of "main" key in variable y
    y = x["main"]

    #store the value coressponding to the "temp" key of y
    current_temperature = y["temp"]

    #store the value coressponding to the "pressure" key of y
    current_pressure =y["pressure"]
    
    #store the value coressponding to the "humidity" key of y
    current_humidity =y["humidity"]
    #store the value of "weather" key in variable z
    z= x["weather"]
    
    #store the value coressponding to the "description" key
    #at the 0th index of z
    weather_description = z[0]["description"]
    #print the following values  
    print(" Temperature(in kelvin unit)= " +
                       str(current_temperature) + 
                       "\n atmospheric pressure (in hPa unit) = " +
                       str(current_pressure) +
                       "\n humidity (in percantage) = " +
                       str(current_humidity) +
                       "\n description = " +
                       str(weather_description))
else:
    print("City Not Found")                       
