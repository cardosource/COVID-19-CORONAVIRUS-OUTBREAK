import requests
import json
import csv
import threading

def coronavirus():
    dic = json.loads(requests.get("https://exchange.vcoud.com/coronavirus/latest").text)
    outputFile = open('COVID-19 CORONAVIRUS OUTBREAK.csv',	'w',	newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['Date', 'Pais', 'TotalDeaths', 'SeriousCases','TotalCases'])
    print("Pais   Toral Cases")
    for elem in dic:
        print("%s    %s "%(elem['name'],elem['totalCases']))
        outputWriter.writerow([elem['updatedAt'],elem['name'],elem['totalCases'],elem['totalDeaths'],elem['seriousCases']])
    outputFile.close()
threadObj = threading.Thread(target=coronavirus)
threadObj.start()
