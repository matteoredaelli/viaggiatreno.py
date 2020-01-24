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

azione = sys.argv[1]

for line in sys.stdin:
    treno_stazione = line.strip().split("|")[1]
    treno = treno_stazione.split("-")[0]
    stazione= treno_stazione.split("-")[1]
    if azione == "pl":
      print("treno(\"%s\",\"%s\")." % (treno, stazione))

        
