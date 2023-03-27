# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import random
import time

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('Spreadsheet-35ff12cf4e93.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Copia di Interrogazioni') #'https://docs.google.com/spreadsheets/d/1kM0bn3P42gLJb3AXiePLuONQyX8c6iJQ2bUxUId7eeo/')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

giorni = []
registro = ["Bagattoni", "Balisteri", "Bassi", "Bosi", "Biffi", "Bruschi", "Chiari", "Diessa",
            "Dini", "Dinu", "Favali", "Graziani", "Jarzabek", "Lelli", "Moretti", "Pretolani",
            "Ravaioli", "Rosati", "Serri", "Turchi", "Venturini", "Vespignani", "Viroli"]

materia = str(input("Inserire il nome della materia: "))

ngiorni = int(input("Inserire il numero dei giorni: "))
index = 0

giainterrogati = []

ninterrogati = int(input("Inserire il numero degli interrogati: "))
j = 2
k = 0

for index in range(ngiorni):
    giorno = str(input("inserire il giorno(formato dd/mm): "))
    giorni.append(giorno)

print(giorni[index])
for index in range(ngiorni):
    cell = sheet_instance.find(giorni[index])

    for S in range(ninterrogati):
        if S == 0:
            sheet_instance.update_cell(cell.row + j, cell.col, materia)
            #sheet_instance.format(cell, {'textFormat': {'bold': True}})
            j = j + 1
        i = random.randrange(0, len(registro))

        valueslist = sheet_instance.col_values(cell.col - 1)
        valueslist2 = sheet_instance.col_values(cell.col + 1)
        for k in range(len(valueslist)):
            if(valueslist[k]==registro[i]):
                i = random.randrange(0, len(registro))
                registro.pop(i)
            if(k<len(valueslist2)):
                if(valueslist2[k]==registro[i]):
                    i = random.randrange(0, len(registro))
                    registro.pop(i)


        sheet_instance.update_cell(cell.row + j, cell.col, registro[i])
        registro.pop(i) 
        j = j + 1


    j = 2