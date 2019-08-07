import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
import numpy as np
import json, time, os, csv
import timestamp
from threading import Thread

def get_json_data():
	all_data = []
	path_to_json_files = str('./sample_data')
	files = sorted(os.listdir(path_to_json_files))

	print(files)

	for file in files:
		full_filename = "%s/%s" % (path_to_json_files, file)
		with open(full_filename, 'r') as json_file:
			data = json.load(json_file)
			all_data.append(data)
		json_file.close()
	return all_data

def get_timestamps():
	with open('timestamps.txt') as f:
		lines = f.read().splitlines()
	f.close()
	return lines

# timestamp.compose_datapoint()

item_id = '1731'

all_data = get_json_data()
timestamps = get_timestamps()
sell_quantity = [int(json.dumps(data[item_id]['sell_quantity'])) for data in all_data]
buy_quantity = [int(json.dumps(data[item_id]['buy_quantity'])) for data in all_data]

buy_average = [int(json.dumps(data[item_id]['buy_average'])) for data in all_data]
sell_average = [int(json.dumps(data[item_id]['sell_average'])) for data in all_data]

plt.figure(1)
plt.plot(timestamps, sell_quantity, '-bo', label='sell quantity')
plt.plot(timestamps, buy_quantity, '-ro', label='buy quantity')
# plt.legend(loc='upper left')
plt.gca().legend()
plt.title(json.dumps(all_data[0][item_id]['name']), fontsize=14)
plt.ylabel('Trade Quantity')
plt.xlabel('Timestamp')
plt.grid(True)

plt.figure(2)
plt.plot(timestamps, sell_average, '-bo', label='sell average')
plt.plot(timestamps, buy_average, '-ro', label='buy average')
# plt.legend(loc='upper left')
plt.gca().legend()
plt.title(json.dumps(all_data[0][item_id]['name']), fontsize=14)
plt.ylabel('Trade Price')
plt.xlabel('Timestamp')
plt.grid(True)
plt.show()
# Thread(target=plt.show)
# time.sleep(10)