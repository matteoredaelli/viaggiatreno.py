# -*- coding: utf-8 -*-
# encoding=utf8
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

stazione = sys.argv[1]
codice = sys.argv[2]
#filename = sys.argv[3]

url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/andamentoTreno/{stazione}/{codice}"
with requests.Session() as s:
    r = s.get(url.format(stazione=stazione, codice=codice))
    #with open(filename, "w") as myfile:
    text = r.text.replace("\n", "") #+ "\n"
    #myfile.write(text)
    print(text)
