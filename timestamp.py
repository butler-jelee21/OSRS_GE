import time
import requests
import json

def get_version():
	with open ('data_version.txt', 'r') as dv:
		version = dv.read()
	dv.close()
	return version

# Update version takes version as integer, persists version,
# and returns a string version in the form [0-9][0-9][0-9].
def update_version():
	version = int(get_version()) + 1
	str_version = str(version)
	write_data(str_version, 'data_version.txt')
	if version < 10:
		return '00' + str_version
	elif version > 9 and version < 100:
		return '0' + str_version
	elif version > 99:
		return str_version
	else:
		print('Error: update_version')

def write_time():
	with open('timestamps.txt', 'a') as time_file:
		timestamp = str(time.strftime('%H:%M\n'))
		time_file.write(timestamp)
	time_file.close()

def write_data(data, filename):
	with open(filename, 'w') as file:
		file.write(data)
	file.close()

def request_data(version):
	url = 'https://rsbuddy.com/exchange/summary.json'
	save_file = 'sample_data/' + str(update_version()) + '.json'
	try:
		r = requests.get(url)
		data = r.json()
		write_data(json.dumps(data), save_file)
	except:
		print('ERROR: In request_data\nStatus Code: ' + str(r.status_code))

def compose_datapoint():
	request_data(get_version())
	write_time()

if __name__ == '__main__':
	compose_datapoint()
