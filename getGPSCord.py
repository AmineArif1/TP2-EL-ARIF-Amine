import csv
import struct

frame_struct = struct.Struct('<26sii15s')

with open('13caaf25c97e29c8b45ae2e4f9f8ac3b_T0_2e526', 'rb') as file:
    file.seek(0x248)
    trames_bin = file.read()
    trames_size = len(trames_bin)
    trames_count = trames_size // frame_struct.size
    trames = [frame_struct.unpack(trames_bin[i*frame_struct.size:(i+1)*frame_struct.size]) for i in range(trames_count)]

with open('gpsFile.csv', 'w', newline='') as csvfile:
    fieldnames = ['Latitude', 'Longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for trame in trames:
        latitude =  '{:.6f}'.format(trame[1] / 10000000)
        longitude = '{:.6f}'.format(trame[2] / 10000000)
        
        writer.writerow({'Latitude': latitude, 'Longitude': longitude})

print("i have written the data to gpsFile.csv file for you boss.")

