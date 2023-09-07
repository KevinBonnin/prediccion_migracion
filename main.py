import pandas as pd
from fastapi import FastAPI
import uvicorn
import joblib
#import mysql.connector

#conexion = mysql.connector.connect(user ='admin', password = 'migration2023', host = 'database-migration.cq1xp27nrjmz.us-east-2.rds.amazonaws.com', database = 'migration', port = '3306')

indicadores = pd.read_csv('indicadores.csv')

def obtener_predicciones_por_pais(df, modelo):
    predicciones_por_pais = pd.DataFrame()
    for index, fila in df.iterrows():
        variables_independientes = fila[["Crecimiento_PIB", "Tasa_desempleo", "Inflacion_PIB", "Control_Corrupcion", "Emisiones_CO2","Esperanza_vida"]].values.reshape(1, -1)
        prediccion = modelo.predict(variables_independientes)[0]
        pais = fila["Pais"]
        predicciones_por_pais = predicciones_por_pais.append({"País": pais, "Predicción": prediccion}, ignore_index=True)
    return predicciones_por_pais

modelo = joblib.load('modelo_migracion.pkl')

app = FastAPI()

@app.get("/modelo de prediccion")
def prediccion():
    predicciones = obtener_predicciones_por_pais(indicadores, modelo)
    return predicciones