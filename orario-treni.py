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

def epoch2time(epoch):
    return datetime.datetime.fromtimestamp(int(epoch) / 1000).strftime('%H:%M')
    
for line in sys.stdin:
    treno = json.loads(line)
    #print(treno["fermate"][0])
    last = len(treno["fermate"]) - 1
    row = [treno["tipoTreno"],
               treno["numeroTreno"],
               treno["categoria"],
               treno["fermate"][0]["stazione"],
               treno["fermate"][0]["id"],
               epoch2time(treno["fermate"][0]["programmata"]),
               epoch2time(treno["fermate"][0]["effettiva"]),
               treno["fermate"][0]["ritardo"],
               treno["fermate"][last]["stazione"],
               treno["fermate"][last]["id"],
               epoch2time(treno["fermate"][last]["programmata"]),
               epoch2time(treno["fermate"][last]["effettiva"]),
               treno["fermate"][last]["ritardo"]
               ]
    print(",".join(map(str,row)))
        
