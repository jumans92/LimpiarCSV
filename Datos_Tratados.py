# -*- coding: utf-8 -*-
import os, errno, pandas as pd
import csv, datetime, re

path = "C:\\Users\\67801134\\Desktop\\CSV_DATA\\"
#voy a path donde tengo la carpeta CSV DATA con los CSV's a tratar

dirs = os.listdir(path)
#en dirs lista de todos los CSV a tratar

#Si no existe la carpeta para meter los archivos tratados la creo
try:
    os.mkdir(os.getcwd()+"\\OUTPUT_CSV")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

#imprimimos tods los csv del directorio CSV DATA, y los abro con codificacion utf-8
#Cambio el nombre de los archivos quito espacios y le doy codificacion utf-8
#para cada archivo lo abro y lo leo, si empieza por #, salto de linea o SUM o Average no hago nada sigo leyendo,
#si empieza por Índice termino y salgo delif y si no se dan esos casos escribo las lineas correctas
for file in dirs:
    #print(file)
    f = open(path+file,"r",encoding="utf8")
    #f = pd.read_csv(path+file, encoding = 'utf8')
    f2 = open(os.getcwd()+"\\OUTPUT_CSV\\"+file.replace(' ','_'),'w',encoding="utf8")
    for line in f:
        if line.startswith('#') or line == '\n' or line.startswith(',') or line.startswith('"Sums') or line.startswith('"Averages') or line.startswith('Sums') or line.startswith('Averages'):
            continue
        elif line.startswith('Índice'):
            break
        else:
            f2.write(line)

    f2.close()
    f.close()

#ya tengo los CSVs con el nombre cambiado y los datos limpios.
#print ("\nCurrent working dir : %s" % os.getcwd())
#dirs2 = os.listdir(os.getcwd()+"\\OUTPUT_CSV\\"+file)
path2 = "C:\\Users\\67801134\\.spyder-py3\\OUTPUT_CSV\\"
dirs2 = os.listdir(path2)

for file in dirs2:
    #if re.search("[0-9].csv$",file):
    if re.search("\d{8,}.csv$",file):
        cadena1, cadena2 = file.split("-")
        fecha, extension = cadena2.split(".")
        fecha = datetime.datetime.strptime(fecha,"%Y%m%d").date().isoformat()
        #guardamos en fecha la fecha del csv dado en el nombre del archivo
        #print ("Meto esta fecha: " + fecha + " en una columna nueva del archivo: " + file)
        df = pd.read_csv("C:\\Users\\67801134\\.spyder-py3\\OUTPUT_CSV\\" + file)
        df['fecha'] = fecha
        df.to_csv("C:\\Users\\67801134\\.spyder-py3\\OUTPUT_CSV\\" + file, index = False)
