cut -f2 -d'|' data/codici-treno.txt | while read line
do
  treno=$(echo $line|cut -f1 -d'-')
  stazione=$(echo $line|cut -f2 -d'-')
  echo "python andamento-treno.py $stazione $treno > data/andamento-treni/andamento.json"
done
