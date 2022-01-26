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

#get the daily weather        
def get_weather_mode(location_name,json_data):
    daily_weather_list = []
    loc_name = location_name
    for index in range (0, 8):
        local_time = datetime.datetime.fromtimestamp( json_data['daily'][index]['dt'] , tz=pytz.timezone('America/Chicago'))
        #str_time = local_time.strftime( '%Y-%m-%d %a' )
        #print (str_time)
        daily_weather = json_data['daily'][index]['weather'][0]['description']
        daily_weather_list.append(daily_weather)
        #print( f" Day [+{index}] {str_time} = {daily_weather} " )

    #print (daily_weather_list)
    mode_daily_weather = mode (daily_weather_list)
    print (loc_name, "-",mode_daily_weather)
   

#actually create the list
if __name__ == "__main__":
    location = {
    "Mexico Michcocan":(-19.5665,101.7068), 
    "Mexico Sinaloa": (25.0, -107.499998), 
    "USA New York": (40.730610,-73.935242),
    "Canada Ontario": (50.000000, -85.000000),
    "Mexico Puebla" :(19.05083313, -98.217332464),
    "Mexico Jalisco": (20.33333, -103.66667),
    "Mexico Nayarit": (21.739663708, -105.223665772),
    "Mexico San Luis Potosi": (22.14982, -100.97916),
    "Mexico Sonora": (29.66667, -110.5),
    "Mexico Colima": (19.5075646364, -103.617130865),
    "USA Michigan": (44.182205, -84.506836),
    "Mexico Queretaro": (20.835996656, -99.85082993)
    }
    for key in location:
        location_name = key
        latitude= location[key][0]
        longitude= location[key][1]
        
        json_data=get_weather_data (latitude, longitude)
        get_weather_mode(location_name,json_data)




