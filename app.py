import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
import numpy as np
import json, time, os, csv
import timestamp

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

def gen_high_margin(dataset, free=False, margin_filter=None):
	high_margins = []
	for data in dataset:	# goes through the dataset of the day
		data = dataset[38]
		for item in data.items():	# goes through each item for each particular data
			item_obj = item[1]
			if item_obj['members'] != free:	# f2p checker
				continue
			item_id = item_obj['id']
			item_name = item_obj['name']
			item_buy = item_obj['buy_average']
			item_sell = item_obj['sell_average']
			item_bquant = item_obj['buy_quantity']
			item_squant = item_obj['sell_quantity']
			zero = item_squant == 0
			item_trade_ratio = 0 if zero else (float(item_bquant) / float(item_squant))
			item_margin = int(item_buy) - int(item_sell)
			if item_margin > 10:
				high_margin_item = (item_id, item_name, item_margin, item_trade_ratio, item_buy, item_sell)
				high_margins.append(high_margin_item)
			# print(item_id, item_name, item_margin, item_trade_ratio)
			# break
		break
	high_margins.sort(key=lambda high_margins : high_margins[2], reverse=True)
	for i in high_margins:
		print(i)

# timestamp.compose_datapoint()

# item_id = '1731'
# item_id = '3483'
# item_id = '1079'
# item_id = '1275'
item_id = '2568'

all_data = get_json_data()
timestamps = get_timestamps()

sell_quantity = [int(json.dumps(data[item_id]['sell_quantity'])) for data in all_data]
buy_quantity = [int(json.dumps(data[item_id]['buy_quantity'])) for data in all_data]

buy_average = [int(json.dumps(data[item_id]['buy_average'])) for data in all_data]
sell_average = [int(json.dumps(data[item_id]['sell_average'])) for data in all_data]

gen_high_margin(all_data)

plt.figure(1)
plt.plot(timestamps, sell_quantity, '-bo', label='sell quantity')
plt.plot(timestamps, buy_quantity, '-ro', label='buy quantity')
plt.gca().legend()
plt.title(json.dumps(all_data[0][item_id]['name']), fontsize=14)
plt.ylabel('Trade Quantity')
plt.xlabel('Timestamp')
plt.grid(True)

plt.figure(2)
plt.plot(timestamps, sell_average, '-bo', label='sell average')
plt.plot(timestamps, buy_average, '-ro', label='buy average')
plt.gca().legend()
plt.title(json.dumps(all_data[0][item_id]['name']), fontsize=14)
plt.ylabel('Trade Price')
plt.xlabel('Timestamp')
plt.grid(True)
plt.show()