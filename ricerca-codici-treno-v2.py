import requests

url = "http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/cercaNumeroTrenoTrenoAutocomplete/{codice}"
with open("data/codici-treno.txt", "w") as myfile:
   for codice in range(1,14000):
     with requests.Session() as s:
      r = s.get(url.format(codice=codice))
      myfile.write(r.text)
