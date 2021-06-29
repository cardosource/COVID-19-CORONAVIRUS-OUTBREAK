import threading
import time
from queue import Queue
import requests
import json
import csv
def solicitacao(url):
  
    resp = json.loads(requests.get(url).text)
    outputFile = open('COVID-19 CORONAVIRUS OUTBREAK.csv',	'w',	newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(['Date', 'countrie', 'TotalDeaths', 'SeriousCases','TotalCases'])
    print("countrie   Total Cases")
    with conteudo:
        for elem in resp:
            print("%s    %s "%(elem['name'],elem['totalCases']))
            outputWriter.writerow([elem['updatedAt'],elem['name'],elem['totalCases'],elem['totalDeaths'],elem['seriousCases']])
        outputFile.close()

def gerenciador():

    while True:
        url_presente = fila.get()
        solicitacao(url_presente)
        fila.task_done()

quantidade_threads = 5
conteudo = threading.Lock()
fila = Queue()
url = "https://exchange.vcoud.com/coronavirus/latest"
for i in range(quantidade_threads):
     t = threading.Thread(target=gerenciador)
     t.daemon = True
     t.start()
     start = time.time()
     fila.put(url)
fila.join()
print((time.time() - start))
