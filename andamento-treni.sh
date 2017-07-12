#!/usr/bin/env bash

Ym=`date +%Y/%m`
DAY=`date +%d`
dir=data/andamento-treni/$Ym

mkdir -p $dir
rm  $dir/$DAY.json
cut -f2 -d'|' data/codici-treno.txt | while read line
do
  treno=$(echo $line|cut -f1 -d'-')
  stazione=$(echo $line|cut -f2 -d'-')
  python andamento-treno.py $stazione $treno >> $dir/$DAY.json
done
