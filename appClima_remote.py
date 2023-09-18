import requests
import psycopg2
# API Key obtained from OpenWeatherMap
api_key = "325d97a8229e1bd9d897d2a18a24ba22"

# database connection parameters
db_params = {
    "host": "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com",
    "port": "5439",
    "database": "data-engineer-database",
    "user": "samucor_coderhouse",
    "password": "eC6j47uSGT"
}

def get_weather_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error obtaining weather data. Status code:", response.status_code)
        return None

def save_data_in_db(data):
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Insert data into the table
    cur.execute("""
        INSERT INTO samucor_coderhouse.weather_info (lon, lat, temp, feels_like, temp_min, temp_max, pressure, humidity, wind_speed,
                               wind_deg, visibility, clouds, city_id, city_name, weather_id, weather_main,
                               weather_description, weather_icon, dt, country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data['coord']['lon'],
        data['coord']['lat'],
        data['main']['temp'],
        data['main']['feels_like'],
        data['main']['temp_min'],
        data['main']['temp_max'],
        data['main']['pressure'],
        data['main']['humidity'],
        data['wind']['speed'],
        data['wind']['deg'],
        data['visibility'],
        data['clouds']['all'],
        data['id'],
        data['name'],
        data['weather'][0]['id'],
        data['weather'][0]['main'],
        data['weather'][0]['description'],
        data['weather'][0]['icon'],
        data['dt'],
        data['sys']['country']
    ))

    conn.commit()
    conn.close()

    
cities =['La Plata','San Fernando del Valle de Catamarca','Resistencia','Rawson','Córdoba','Corrientes','Paraná','Formosa','San Salvador de Jujuy','Santa Rosa','La Rioja','Mendoza','Posadas','Neuquén','Viedma','Salta','San Juan','San Luis','Río Gallegos','Santa Fe','Santiago del Estero','Ushuaia','San Miguel de Tucumán']
for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},ar&appid={api_key}"
    weather_data= get_weather_data()
    if weather_data:
        save_data_in_db(weather_data)
        print("Data successfully saved to database.")


