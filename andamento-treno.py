# -*- coding: utf-8 -*-
import requests, sys

stazione = sys.argv[1]
codice = sys.argv[2]

url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/{stazione}/{codice}"
with requests.Session() as s:
    r = s.get(url.format(stazione=stazione, codice=codice))
    print(unicode(r.text))
