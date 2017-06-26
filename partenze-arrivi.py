from pprint import pprint as pp
import requests
import datetime

station = "S01514"
dt = datetime.datetime.utcnow()
partenze_arrivi="arrivi";

url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/{partenze_arrivi}/{station}/{iso}"
with requests.Session() as s:
    r = s.get(url.format(partenze_arrivi=partenze_arrivi,
                             station=station,
                             iso=dt.strftime("%a %b %d %Y %H:%M:%S GMT+000 (UTC)")))
    pp(r.json())


