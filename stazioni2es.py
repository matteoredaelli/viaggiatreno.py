import json

import logging, sys
from elasticsearch import Elasticsearch

es = Elasticsearch()

regione = sys.argv[1]
azione = sys.argv[2]

stazionicsv = 'data/stazioni-%s.json'  % regione

with open(stazionicsv) as data_file:
  logging.warning("Opening file %s ..." % stazionicsv)

  data = json.load(data_file)
  for entry in data:
    id = entry["codStazione"]
    #entry["id"] = id
    logging.warning("stazione %s - %s" % (id, entry["localita"]["nomeLungo"]))
    if azione == "es":
      es.index(index="grafo", doc_type=u"viaggiatreno_stazione", id=id, body=entry)
    else:
        print("%s,%s,%s" % (entry["codReg"],
                                entry["codStazione"],
                                entry["localita"]["nomeLungo"]))
        

