#  "tipoTreno": "PG",
#  "codiceCliente": 2,
# "numeroTreno": 5940,
#  "categoria": "REG",
# "origineZero": "PADOVA",
# "destinazioneZero": "BASSANO DEL GRAPPA",
#   "orarioPartenzaZero": 1499786160000,
#  "orarioArrivoZero": 1499790000000,

# fermate[0]["id"] fermate[len(lermate)-1]["id"]
# output
# 

import json
import sys
import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()

def epoch2time(epoch):
    return datetime.datetime.fromtimestamp(int(epoch) / 1000).strftime('%H:%M')
    
for line in sys.stdin:
    treno = json.loads(line)
    id = "%s-%s" % (treno["numeroTreno"], treno["fermate"][0]["id"])
    last = len(treno["fermate"]) - 1
    treno["oraPartenzaProgrammata"] = epoch2time(treno["fermate"][0]["programmata"])
    treno["oraPartenzaEffettiva"]   = epoch2time(treno["fermate"][0]["effettiva"])
    treno["oraArrivoProgrammata"]   = epoch2time(treno["fermate"][last]["programmata"])
    treno["oraArrivoEffettiva"]     = epoch2time(treno["fermate"][last]["effettiva"])
    es.index(index="grafo", doc_type=u"viaggiatreno_treno", id=id, body=treno)
        
