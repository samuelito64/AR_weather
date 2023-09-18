-- Crear la tabla para almacenar la información del clima en el esquema 'argentina'
CREATE TABLE samucor_coderhouse.weather_info (
    id INT IDENTITY(1,1) PRIMARY KEY,
    lon FLOAT,
    lat FLOAT,
    temp FLOAT,
    feels_like FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    pressure INT,
    humidity INT,
    wind_speed FLOAT,
    wind_deg INT,
    visibility INT,
    clouds INT,
    city_id INT,
    city_name VARCHAR(255),
    weather_id INT,
    weather_main VARCHAR(50),
    weather_description VARCHAR(255),
    weather_icon VARCHAR(10),
    dt INT,
    country VARCHAR(5)
);
