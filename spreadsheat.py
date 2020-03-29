import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope =  ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("testing").sheet1
##sheet.update_cell(1,1, "Hey there")

import datetime
import schedule
import time
import codecs
import string
import glob
import os

row = 2
minute = 2

def job():



	'''
	Find latest file in folder

	'''


	list_of_files = glob.glob('C:/Users/Shane/Desktop/sort/*') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	#print (latest_file)
	latest_file_open = open(latest_file, "r")
	#print(opened.read())
	contents = latest_file_open.read()
	#print(contents)
	latest_file_open.close()


	'''

	split file into list


	'''

	contents1 = contents.split(",")
	li = []
	for i in contents1:
		li.append(str(i))

	'''

	Set Variables

	'''

	global minute 

	if minute == 2:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[61])[1::2])
		catalyst = ((li[62])[1::2])
		methanol_1 = ((li[63])[1::2])
		methanol_2 = ((li[64])[1::2])
		reclaimed_methanol = ((li[65])[1::2])
		dump_tank = ((li[66])[1::2])
		dump_tank_flow_meter = ((li[67])[1::2])
		tank_1 = ((li[68])[1::2])
		tank_2 = ((li[69])[1::2])
		tank_3 = ((li[70])[1::2])
		disc_1_feed = ((li[71])[1::2])
		disc_1_out = ((li[72])[1::2])
		yg_offload_1 = ((li[73])[1::2])
		yg_offload_2 = ((li[74])[1::2])
		yg_15k_1 = ((li[75])[1::2])
		yg_15k_2 = ((li[76])[1::2])
		disc_2_feed = ((li[77])[1::2])
		disc_2_out = ((li[78])[1::2])
		wet_oil = ((li[79])[1::2])
		waste = ((li[80])[1::2])
		yg = ((li[81])[1::2])
		bio_1 = ((li[82])[1::2])
		bio_2 = ((li[83])[1::2])
		bio_3 = ((li[84])[1::2])
		glycerin = ((li[85])[1::2])
		day_tank = ((li[86])[1::2])
		backup_day_tank_5k = ((li[87])[1::2])
		reclaimed_methanol_totalizer = ((li[88])[1::2])
		feed_stock_totalizer = ((li[89])[1::2])
		b100_temp = ((li[90])[1::2])
		b100_temp_modified = b100_temp[0:8]
		print('row 2')
		print(time)
		minute += 1

	elif minute == 3:
		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[331])[1::2])
		catalyst = ((li[332])[1::2])
		methanol_1 = ((li[333])[1::2])
		methanol_2 = ((li[334])[1::2])
		reclaimed_methanol = ((li[335])[1::2])
		dump_tank = ((li[336])[1::2])
		dump_tank_flow_meter = ((li[337])[1::2])
		tank_1 = ((li[338])[1::2])
		tank_2 = ((li[339])[1::2])
		tank_3 = ((li[340])[1::2])
		disc_1_feed = ((li[341])[1::2])
		disc_1_out = ((li[342])[1::2])
		yg_offload_1 = ((li[343])[1::2])
		yg_offload_2 = ((li[344])[1::2])
		yg_15k_1 = ((li[345])[1::2])
		yg_15k_2 = ((li[346])[1::2])
		disc_2_feed = ((li[347])[1::2])
		disc_2_out = ((li[348])[1::2])
		wet_oil = ((li[349])[1::2])
		waste = ((li[350])[1::2])
		yg = ((li[351])[1::2])
		bio_1 = ((li[352])[1::2])
		bio_2 = ((li[353])[1::2])
		bio_3 = ((li[354])[1::2])
		glycerin = ((li[355])[1::2])
		day_tank = ((li[356])[1::2])
		backup_day_tank_5k = ((li[357])[1::2])
		reclaimed_methanol_totalizer = ((li[358])[1::2])
		feed_stock_totalizer = ((li[359])[1::2])
		b100_temp = ((li[360])[1::2])
		b100_temp_modified = b100_temp[0:8]


		print('row 3')
		print(time)
		minute += 1

	elif minute == 4:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[661])[1::2])
		catalyst = ((li[662])[1::2])
		methanol_1 = ((li[663])[1::2])
		methanol_2 = ((li[664])[1::2])
		reclaimed_methanol = ((li[665])[1::2])
		dump_tank = ((li[666])[1::2])
		dump_tank_flow_meter = ((li[667])[1::2])
		tank_1 = ((li[668])[1::2])
		tank_2 = ((li[669])[1::2])
		tank_3 = ((li[670])[1::2])
		disc_1_feed = ((li[671])[1::2])
		disc_1_out = ((li[672])[1::2])
		yg_offload_1 = ((li[673])[1::2])
		yg_offload_2 = ((li[674])[1::2])
		yg_15k_1 = ((li[675])[1::2])
		yg_15k_2 = ((li[676])[1::2])
		disc_2_feed = ((li[677])[1::2])
		disc_2_out = ((li[678])[1::2])
		wet_oil = ((li[679])[1::2])
		waste = ((li[680])[1::2])
		yg = ((li[681])[1::2])
		bio_1 = ((li[682])[1::2])
		bio_2 = ((li[683])[1::2])
		bio_3 = ((li[684])[1::2])
		glycerin = ((li[685])[1::2])
		day_tank = ((li[686])[1::2])
		backup_day_tank_5k = ((li[687])[1::2])
		reclaimed_methanol_totalizer = ((li[688])[1::2])
		feed_stock_totalizer = ((li[689])[1::2])
		b100_temp = ((li[690])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 4')
		print(time)
		minute += 1

	elif minute == 5:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[931])[1::2])
		catalyst = ((li[932])[1::2])
		methanol_1 = ((li[933])[1::2])
		methanol_2 = ((li[934])[1::2])
		reclaimed_methanol = ((li[935])[1::2])
		dump_tank = ((li[936])[1::2])
		dump_tank_flow_meter = ((li[937])[1::2])
		tank_1 = ((li[938])[1::2])
		tank_2 = ((li[939])[1::2])
		tank_3 = ((li[940])[1::2])
		disc_1_feed = ((li[941])[1::2])
		disc_1_out = ((li[942])[1::2])
		yg_offload_1 = ((li[943])[1::2])
		yg_offload_2 = ((li[944])[1::2])
		yg_15k_1 = ((li[945])[1::2])
		yg_15k_2 = ((li[946])[1::2])
		disc_2_feed = ((li[947])[1::2])
		disc_2_out = ((li[948])[1::2])
		wet_oil = ((li[949])[1::2])
		waste = ((li[950])[1::2])
		yg = ((li[951])[1::2])
		bio_1 = ((li[952])[1::2])
		bio_2 = ((li[953])[1::2])
		bio_3 = ((li[954])[1::2])
		glycerin = ((li[955])[1::2])
		day_tank = ((li[956])[1::2])
		backup_day_tank_5k = ((li[957])[1::2])
		reclaimed_methanol_totalizer = ((li[958])[1::2])
		feed_stock_totalizer = ((li[959])[1::2])
		b100_temp = ((li[960])[1::2]) 
		b100_temp_modified = b100_temp[0:8]

		print ('row 5')
		print(time)
		minute += 1

	elif minute == 6:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[931])[1::2])
		catalyst = ((li[932])[1::2])
		methanol_1 = ((li[933])[1::2])
		methanol_2 = ((li[934])[1::2])
		reclaimed_methanol = ((li[935])[1::2])
		dump_tank = ((li[936])[1::2])
		dump_tank_flow_meter = ((li[937])[1::2])
		tank_1 = ((li[938])[1::2])
		tank_2 = ((li[939])[1::2])
		tank_3 = ((li[940])[1::2])
		disc_1_feed = ((li[941])[1::2])
		disc_1_out = ((li[942])[1::2])
		yg_offload_1 = ((li[943])[1::2])
		yg_offload_2 = ((li[944])[1::2])
		yg_15k_1 = ((li[945])[1::2])
		yg_15k_2 = ((li[946])[1::2])
		disc_2_feed = ((li[947])[1::2])
		disc_2_out = ((li[948])[1::2])
		wet_oil = ((li[949])[1::2])
		waste = ((li[950])[1::2])
		yg = ((li[951])[1::2])
		bio_1 = ((li[952])[1::2])
		bio_2 = ((li[953])[1::2])
		bio_3 = ((li[954])[1::2])
		glycerin = ((li[955])[1::2])
		day_tank = ((li[956])[1::2])
		backup_day_tank_5k = ((li[957])[1::2])
		reclaimed_methanol_totalizer = ((li[958])[1::2])
		feed_stock_totalizer = ((li[959])[1::2])
		b100_temp = ((li[960])[1::2]) 
		b100_temp_modified = b100_temp[0:8]

		print ('row 5')
		print(time)
		minute += 1

	elif minute == 7:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[1201])[1::2])
		catalyst = ((li[1202])[1::2])
		methanol_1 = ((li[1203])[1::2])
		methanol_2 = ((li[1204])[1::2])
		reclaimed_methanol = ((li[1205])[1::2])
		dump_tank = ((li[1206])[1::2])
		dump_tank_flow_meter = ((li[1207])[1::2])
		tank_1 = ((li[1208])[1::2])
		tank_2 = ((li[1209])[1::2])
		tank_3 = ((li[1210])[1::2])
		disc_1_feed = ((li[1211])[1::2])
		disc_1_out = ((li[1212])[1::2])
		yg_offload_1 = ((li[1213])[1::2])
		yg_offload_2 = ((li[1214])[1::2])
		yg_15k_1 = ((li[1215])[1::2])
		yg_15k_2 = ((li[1216])[1::2])
		disc_2_feed = ((li[1217])[1::2])
		disc_2_out = ((li[1218])[1::2])
		wet_oil = ((li[1219])[1::2])
		waste = ((li[1220])[1::2])
		yg = ((li[1221])[1::2])
		bio_1 = ((li[1222])[1::2])
		bio_2 = ((li[1223])[1::2])
		bio_3 = ((li[1224])[1::2])
		glycerin = ((li[1225])[1::2])
		day_tank = ((li[1226])[1::2])
		backup_day_tank_5k = ((li[1227])[1::2])
		reclaimed_methanol_totalizer = ((li[1228])[1::2])
		feed_stock_totalizer = ((li[1229])[1::2])
		b100_temp = ((li[1230])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 7')
		print(time)
		minute += 1

	elif minute == 8:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[1861])[1::2])
		catalyst = ((li[1862])[1::2])
		methanol_1 = ((li[1863])[1::2])
		methanol_2 = ((li[1864])[1::2])
		reclaimed_methanol = ((li[1865])[1::2])
		dump_tank = ((li[1866])[1::2])
		dump_tank_flow_meter = ((li[1867])[1::2])
		tank_1 = ((li[1868])[1::2])
		tank_2 = ((li[1869])[1::2])
		tank_3 = ((li[1870])[1::2])
		disc_1_feed = ((li[1871])[1::2])
		disc_1_out = ((li[1872])[1::2])
		yg_offload_1 = ((li[1873])[1::2])
		yg_offload_2 = ((li[1874])[1::2])
		yg_15k_1 = ((li[1875])[1::2])
		yg_15k_2 = ((li[1876])[1::2])
		disc_2_feed = ((li[1877])[1::2])
		disc_2_out = ((li[1878])[1::2])
		wet_oil = ((li[1879])[1::2])
		waste = ((li[1880])[1::2])
		yg = ((li[1881])[1::2])
		bio_1 = ((li[1882])[1::2])
		bio_2 = ((li[1883])[1::2])
		bio_3 = ((li[1884])[1::2])
		glycerin = ((li[1885])[1::2])
		day_tank = ((li[1886])[1::2])
		backup_day_tank_5k = ((li[1887])[1::2])
		reclaimed_methanol_totalizer = ((li[1888])[1::2])
		feed_stock_totalizer = ((li[1889])[1::2])
		b100_temp = ((li[1890])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 8')
		print(time)
		minute += 1

	elif minute == 9:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[2071])[1::2])
		catalyst = ((li[2072])[1::2])
		methanol_1 = ((li[2073])[1::2])
		methanol_2 = ((li[2074])[1::2])
		reclaimed_methanol = ((li[2075])[1::2])
		dump_tank = ((li[2076])[1::2])
		dump_tank_flow_meter = ((li[2077])[1::2])
		tank_1 = ((li[2078])[1::2])
		tank_2 = ((li[2079])[1::2])
		tank_3 = ((li[2080])[1::2])
		disc_1_feed = ((li[2081])[1::2])
		disc_1_out = ((li[2082])[1::2])
		yg_offload_1 = ((li[2083])[1::2])
		yg_offload_2 = ((li[2084])[1::2])
		yg_15k_1 = ((li[2085])[1::2])
		yg_15k_2 = ((li[2086])[1::2])
		disc_2_feed = ((li[2087])[1::2])
		disc_2_out = ((li[2088])[1::2])
		wet_oil = ((li[2089])[1::2])
		waste = ((li[2090])[1::2])
		yg = ((li[2091])[1::2])
		bio_1 = ((li[2092])[1::2])
		bio_2 = ((li[2093])[1::2])
		bio_3 = ((li[2094])[1::2])
		glycerin = ((li[2095])[1::2])
		day_tank = ((li[2096])[1::2])
		backup_day_tank_5k = ((li[2097])[1::2])
		reclaimed_methanol_totalizer = ((li[2098])[1::2])
		feed_stock_totalizer = ((li[2099])[1::2])
		b100_temp = ((li[2100])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 9')
		print(time)
		minute += 1

	elif minute == 10:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[2431])[1::2])
		catalyst = ((li[2432])[1::2])
		methanol_1 = ((li[2433])[1::2])
		methanol_2 = ((li[2434])[1::2])
		reclaimed_methanol = ((li[2435])[1::2])
		dump_tank = ((li[2436])[1::2])
		dump_tank_flow_meter = ((li[2437])[1::2])
		tank_1 = ((li[2438])[1::2])
		tank_2 = ((li[2439])[1::2])
		tank_3 = ((li[2440])[1::2])
		disc_1_feed = ((li[2441])[1::2])
		disc_1_out = ((li[2442])[1::2])
		yg_offload_1 = ((li[2443])[1::2])
		yg_offload_2 = ((li[2444])[1::2])
		yg_15k_1 = ((li[2445])[1::2])
		yg_15k_2 = ((li[2446])[1::2])
		disc_2_feed = ((li[2447])[1::2])
		disc_2_out = ((li[2448])[1::2])
		wet_oil = ((li[2449])[1::2])
		waste = ((li[2450])[1::2])
		yg = ((li[2451])[1::2])
		bio_1 = ((li[2452])[1::2])
		bio_2 = ((li[2453])[1::2])
		bio_3 = ((li[2454])[1::2])
		glycerin = ((li[2455])[1::2])
		day_tank = ((li[2456])[1::2])
		backup_day_tank_5k = ((li[2457])[1::2])
		reclaimed_methanol_totalizer = ((li[2458])[1::2])
		feed_stock_totalizer = ((li[2459])[1::2])
		b100_temp = ((li[2460])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 10')
		print (time)
		minute += 1

	elif minute == 11:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[2761])[1::2])
		catalyst = ((li[2762])[1::2])
		methanol_1 = ((li[2763])[1::2])
		methanol_2 = ((li[2764])[1::2])
		reclaimed_methanol = ((li[2765])[1::2])
		dump_tank = ((li[2766])[1::2])
		dump_tank_flow_meter = ((li[2767])[1::2])
		tank_1 = ((li[2768])[1::2])
		tank_2 = ((li[2769])[1::2])
		tank_3 = ((li[2770])[1::2])
		disc_1_feed = ((li[2771])[1::2])
		disc_1_out = ((li[2772])[1::2])
		yg_offload_1 = ((li[2773])[1::2])
		yg_offload_2 = ((li[2774])[1::2])
		yg_15k_1 = ((li[2775])[1::2])
		yg_15k_2 = ((li[2776])[1::2])
		disc_2_feed = ((li[2777])[1::2])
		disc_2_out = ((li[2778])[1::2])
		wet_oil = ((li[2779])[1::2])
		waste = ((li[2780])[1::2])
		yg = ((li[2781])[1::2])
		bio_1 = ((li[2782])[1::2])
		bio_2 = ((li[2783])[1::2])
		bio_3 = ((li[2784])[1::2])
		glycerin = ((li[2785])[1::2])
		day_tank = ((li[2786])[1::2])
		backup_day_tank_5k = ((li[2787])[1::2])
		reclaimed_methanol_totalizer = ((li[2788])[1::2])
		feed_stock_totalizer = ((li[2789])[1::2])
		b100_temp = ((li[2790])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 11')
		print (time)
		minute += 1

	elif minute == 12:

		date = ((li[30])[1::2])
		date_modified = (date[11:30])
		time = ((li[3031])[1::2])
		catalyst = ((li[3032])[1::2])
		methanol_1 = ((li[3033])[1::2])
		methanol_2 = ((li[3034])[1::2])
		reclaimed_methanol = ((li[3035])[1::2])
		dump_tank = ((li[3036])[1::2])
		dump_tank_flow_meter = ((li[3037])[1::2])
		tank_1 = ((li[3038])[1::2])
		tank_2 = ((li[3039])[1::2])
		tank_3 = ((li[3040])[1::2])
		disc_1_feed = ((li[3041])[1::2])
		disc_1_out = ((li[3042])[1::2])
		yg_offload_1 = ((li[3043])[1::2])
		yg_offload_2 = ((li[3044])[1::2])
		yg_15k_1 = ((li[3045])[1::2])
		yg_15k_2 = ((li[3046])[1::2])
		disc_2_feed = ((li[3047])[1::2])
		disc_2_out = ((li[3048])[1::2])
		wet_oil = ((li[3049])[1::2])
		waste = ((li[3050])[1::2])
		yg = ((li[3051])[1::2])
		bio_1 = ((li[3052])[1::2])
		bio_2 = ((li[3053])[1::2])
		bio_3 = ((li[3054])[1::2])
		glycerin = ((li[3055])[1::2])
		day_tank = ((li[3056])[1::2])
		backup_day_tank_5k = ((li[3057])[1::2])
		reclaimed_methanol_totalizer = ((li[3058])[1::2])
		feed_stock_totalizer = ((li[3059])[1::2])
		b100_temp = ((li[3060])[1::2])
		b100_temp_modified = b100_temp[0:8]

		print ('row 12')
		print (time)
		minute += 1

	
	else:
		print('something didnt work')

	if minute > 12:
		minute = 2

	'''
	

	update sheets


	'''
	global row

	sheet.update_cell(row, 1, date_modified)
	sheet.update_cell(row, 2, time)
	sheet.update_cell(row, 3, catalyst)
	sheet.update_cell(row, 4, methanol_1)
	sheet.update_cell(row, 5, methanol_2)
	sheet.update_cell(row, 6, reclaimed_methanol)
	sheet.update_cell(row, 7, dump_tank)
	sheet.update_cell(row, 8, dump_tank_flow_meter)
	sheet.update_cell(row, 9, tank_1)
	sheet.update_cell(row, 10, tank_2)
	sheet.update_cell(row, 11, tank_3)
	sheet.update_cell(row, 12, disc_1_feed)
	sheet.update_cell(row, 13, disc_1_out)
	sheet.update_cell(row, 14, yg_offload_1)
	sheet.update_cell(row, 15, yg_offload_2)
	sheet.update_cell(row, 16, yg_15k_1)
	sheet.update_cell(row, 17, yg_15k_2)
	sheet.update_cell(row, 18, disc_2_feed)
	sheet.update_cell(row, 19, disc_2_out)
	sheet.update_cell(row, 20, wet_oil)
	sheet.update_cell(row, 21, waste)
	sheet.update_cell(row, 22, yg)
	sheet.update_cell(row, 23, bio_1)
	sheet.update_cell(row, 24, bio_2)
	sheet.update_cell(row, 25, bio_3)
	sheet.update_cell(row, 26, glycerin)
	sheet.update_cell(row, 27, day_tank)
	sheet.update_cell(row, 28, backup_day_tank_5k)
	sheet.update_cell(row, 29, reclaimed_methanol_totalizer)
	sheet.update_cell(row, 30, feed_stock_totalizer)
	sheet.update_cell(row, 31, b100_temp_modified)

	print('job ran')
	row += 1

	return




def running():
	while True:
		print("Program is Running..." )
		print((datetime.datetime.now().time()))
		time.sleep(60)
	return

'''
schedule.every().day.at("15:29").do(job)
#schedule.every().day.at("13:02").do(job)

while True:
	schedule.run_pending()
	time.sleep(60)

'''

if __name__ == '__main__':

	start_time = time.time()

	while True: 
		job()
		time.sleep(30.0 - ((time.time()-start_time) % 30.0 ))


