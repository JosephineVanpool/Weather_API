#importing modules
import requests,json, pprint, datetime, pytz
from statistics import mode


#pp =pprint.PrettyPrinter(indent =4)

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
json_data = response.json()
print (pp.pprint(json_data))
print (code)

daily_weather_list = []
#Now x contains list of nested dictionaries
#check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
if response.ok:
    for index in range (0, 8):
        local_time = datetime.datetime.fromtimestamp( json_data['daily'][index]['dt'] , tz=pytz.timezone('America/Chicago'))
        str_time = local_time.strftime( '%Y-%m-%d %a' )
        print (str_time)
        daily_weather = json_data['daily'][index]['weather'][0]['description']
        daily_weather_list.append(daily_weather)
        print( f" Day [+{index}] {str_time} = {daily_weather} " )

    print (daily_weather_list)
    mode_daily_weather = mode (daily_weather_list)
    print (mode_daily_weather)

else:
    print("City Not Found")                       
