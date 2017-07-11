#!/usr/bin/env bash

DATE=`date +%Y-%m-%d`
dir=data/andamento-treni/$DATE

mkdir -p $dir
cut -f2 -d'|' data/codici-treno.txt | while read line
do
  treno=$(echo $line|cut -f1 -d'-')
  stazione=$(echo $line|cut -f2 -d'-')
  python andamento-treno.py $stazione $treno $dir/$stazione-$treno.json
done
