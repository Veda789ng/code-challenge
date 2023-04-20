import os
import logging
import datetime
from .models import Weather
from sqlalchemy.sql import text
from . import db
from tqdm import tqdm

logging.basicConfig(filename="logs/record.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

def wx_data():
    wx_data_path = os.getcwd()+'/wx_data'
    weather_data = []
    for file in tqdm(os.listdir(wx_data_path)):
        if file.endswith('.txt'):
            with open(f'{wx_data_path}/{file}') as f:
                for line in f:
                    record=line.strip().split('\t')
                    w = Weather(
                        station=file[:-4],
                        date=int(record[0]),
                        maximum_temperature=int(record[1]),
                        minimum_temperature=int(record[2]),
                        precipitation=int(record[3])
                        )
                    weather_data.append(w)

    return weather_data

def ingest_wx_data():
    initial_time = datetime.datetime.now()
    print("data ingestion started")
    weather = wx_data()
    print("loading data to database.....")
    s = db.session
    s.bulk_save_objects(weather)
    s.commit()
    logger.info("weather data loaded..")
    completion_time = datetime.datetime.now()
    logger.info(
        f"Weather Data inserted in : {(completion_time-initial_time).total_seconds()} secs \t Total rows: {len(weather)}"
    )
    print("data inserted")

def generate_stats():

    query = """INSERT INTO stats(station,date,final_maximum_temperature,final_minimum_temperature,final_precipitation)
            SELECT station,date,avg(maximum_temperature),avg(minimum_temperature),sum(precipitation)
                from (
                    select * from weather
                    where maximum_temperature!=-9999
                    and minimum_temperature!=-9999
                    and precipitation!=-9999
                ) group by station , substring(date,1,4)"""
    s = db.session
    s.execute(text(query))
    s.commit()
    logger.info("stats data loaded")