for regione in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 22 ; do
  wget -O data/stazioni-$regione.json http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/elencoStazioni/$regione
  #python3 stazioni2es.py $regione es
  python3 stazioni2es.py $regione output > data/stazioni-$regione.csv
done
