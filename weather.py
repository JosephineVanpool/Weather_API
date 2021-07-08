#importing modules
import requests,json, pprint, datetime, pytz
from statistics import mode

from requests.api import get

def get_weather_data(latitude,longitude,api_key="09d4916d61723eb6f4bd9b01105317c9",base_url="https://api.openweathermap.org/data/2.5/onecall?lat="):
    #pp =pprint.PrettyPrinter(indent =4)

    #set location name, latitude/longitude for the location
    lat= latitude
    long= longitude

    #complete_url variable to store the complete_url address
    complete_url = str(base_url + str(lat) + "&lon="+ str(long) +"&exclude={,minutely,hourly,alerts}&appid="+api_key)

    #if the reponse is ok, then get and return the json file, if not return an error message
    try: 
        response = requests.get(complete_url)
        response.raise_for_status()

        json_data = response.json()
        #print (pp.pprint(json_data))
    except:
        raise

    return json_data

        
def get_weather_mode(location_name,json_data):
    daily_weather_list = []
    loc_name = location_name
    print (loc_name)
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
   

if __name__ == "__main__":
    location = {"Mexico Michcocan":(-19.5665,101.7068)}
    for key in location:
        location_name = key
        latitude= location[key][0]
        longitude= location[key][1]
        
        json_data=get_weather_data (latitude, longitude)
        get_weather_mode(location_name,json_data)

#next step is to determine how to break mode, or how to handle when there is no mode in the list
#also need the complete list of locations and lat/long coordinates to add to the location list in the main function
#will want to create a seperate dict with location name and the mode (or the list of daily weather if no mode exists)



