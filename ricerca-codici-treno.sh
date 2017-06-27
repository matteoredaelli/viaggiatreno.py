for stazione in S01700 S01701 S01645 S01642 S01820
do
	python3 ricerca-codici-treno.py $stazione >> data/codici-treno-full.csv
done
