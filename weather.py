#importing modules
import requests,json, pprint, datetime, pytz
from statistics import mode

def get_weather_data(latitude,longitude,api_key="09d4916d61723eb6f4bd9b01105317c9",base_url="https://api.openweathermap.org/data/2.5/onecall?lat="):
    #pp =pprint.PrettyPrinter(indent =4)

    #set latitude/longitude
    lat= latitude
    long= longitude

    #complete_url variable to store the complete_url address
    complete_url = str(base_url + str(lat) + "&lon="+ str(long) +"&exclude={,minutely,hourly,alerts}&appid="+api_key)

    #if the reponse is ok, then get and return the json file, if not return an error message
    try: 
        response = requests.get(complete_url)
        response.raise_for_status()
        
        #json method of response object convert json format data into python format data
        json_data = response.json()
        #print (pp.pprint(json_data))
    except:
        raise

    return json_data

        
def get_weather_mode(json_data):
    daily_weather_list = []
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
    latitude= -19.5665
    longitude= 101.7068
    get_weather_data (latitude, longitude)




