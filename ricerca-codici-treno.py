from pprint import pprint as pp
import datetime
import requests
import sys

stazione = sys.argv[1]

def partenze_arrivi(stazione, partenze_arrivi):
    dt = datetime.datetime.utcnow()
    url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/{partenze_arrivi}/{stazione}/{iso}"
    with requests.Session() as s:
        r = s.get(url.format(partenze_arrivi=partenze_arrivi,
                             stazione=stazione,
                             iso=dt.strftime("%a %b %d %Y %H:%M:%S GMT+000 (UTC)")))
    return r.json()

results1 = partenze_arrivi(stazione, "partenze")
results2 = partenze_arrivi(stazione, "arrivi")

for result in results1 +results2:
    print("%s,%s,%s,%s,%s" % (result["codOrigine"],
                            result["categoria"],
                            result["numeroTreno"],
                            result["orarioPartenza"],
                            result["orarioArrivo"],
                            ))
    
##pp(r.json())


