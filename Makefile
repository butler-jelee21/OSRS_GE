all:
	@echo 'If this is the first time the application is being built:'
	@echo '	make skeleton'
	@echo '	make run'
	@echo 'Otherwise:'
	@echo '	make run'

run:
	python3 app.py

skeleton: clean
	touch timestamps.txt
	echo '0' >> data_version.txt
	mkdir sample_data

clean:
	- rm -rf sample_data 
	- rm -rf timestamps.txt 
	- rm -rf data_version.txt
