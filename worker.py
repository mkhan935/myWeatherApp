import  requests, psycopg2,logging
import psycopg2.extras
from datetime import datetime



def fetch_data(zipcode):
    api_token='ur API KEY'
    url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/'+zipcode+'.json'
    #url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/CA/San_Francisco.json'
    r=requests.get(url).json()
    data=r['current_observation']

    location=data['observation_location']['full']

    weather=data['weather']

    wind_str=data['wind_string']

    temp=data['temp_f']

    humidity=data['relative_humidity']

    precip=data['precip_today_string']

    icon_url=data['icon_url']

    observation_time=data['observation_time']

    try:
        conn = psycopg2.connect(dbname,user,
                                host,
                                password)
        print('DB OPENED')
    except:
        print(datetime.now(),"Unable to Connect")
        logging.exception("Unable to connect Logged")
        return
    else:
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    #write To DB
    cur.execute("""INSERT INTO station_reading(location,weather,wind_str,temp,humidity,precip,icon_url,observation_time)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(location,weather,wind_str,temp,humidity,precip,icon_url,observation_time))

    conn.commit()
    cur.close()
    conn.close()

    print("Data Written: ",datetime.now())
#fetch_data()
