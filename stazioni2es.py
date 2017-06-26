import json

import logging, sys
from elasticsearch import Elasticsearch

es = Elasticsearch()

regione = sys.argv[1]

stazionicsv = 'data/stazioni-%s.json'  % regione

with open(stazionicsv) as data_file:
  logging.warning("Opening file %s ..." % stazionicsv)

  data = json.load(data_file)
  for entry in data:
    id = "%s-%s" % (entry["codReg"],entry["codStazione"])
    #entry["id"] = id
    logging.warning("Indexing %s - %s" % (id, entry["localita"]["nomeLungo"]))
    es.index(index="grafo", doc_type=u"trenitalia_stazione", id=id, body=entry)

