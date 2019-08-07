for i in {1..10} 
do
	echo $i + "th run"
	python3 timestamp.py
	sleep 600s
done

# make run