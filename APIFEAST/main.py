import pandas as pd
import numpy as np
import mysql.connector
from fastapi import FastAPI

app = FastAPI()

@app.get("/process_data")
async def process_data():
    # Load data from folder
    df = pd.read_excel('./cars.xlsx')
    print(df)
    df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
    # Split data into three new dataframes
    n = len(df)
    train = df

    # Connect to MySQL database
    db = mysql.connector.connect(
        host="dbfeast",
        user="root",
        password="123456",
        database="dbfeast"
    )
    cursor = db.cursor()

    # Delete existing data from tables
    cursor.execute("DELETE FROM train_table")


    data = []
    for i, row in train.iterrows():
        data.append({
            'mpg': row['mpg'],
            'cylinders': row['cylinders'],
            'displacement': row['displacement'],
            'horsepower': row['horsepower'],
            'weight': row['weight'],
            'acceleration': row['acceleration'],
            'model_year': row['model_year'],
            'origin': row['origin'],
            'car_name': row['car_name']
        })
    query = "INSERT INTO train_table (mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, car_name) VALUES (%(mpg)s, %(cylinders)s, %(displacement)s, %(horsepower)s, %(weight)s, %(acceleration)s, %(model_year)s, %(origin)s, %(car_name)s)"
    cursor.executemany(query, data)

    # Commit changes and close database connection
    db.commit()
    db.close()

    return {"message": "Información procesada en base de datos dbfeast!"}

@app.get("/")
async def show_data():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="dbfeast",
        user="root",
        password="123456",
        database="dbfeast"
    )
    cursor = db.cursor()

    query = "SELECT * FROM train_table"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    # Close database connection
    db.close()

    return {"message": result}