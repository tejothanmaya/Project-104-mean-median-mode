from collections import Counter
import csv
with open('height-weight.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

data = Counter(new_data)
mode_data = {
    "75-100":0,
    "100-125":0,
    "125-150":0,
    "150-175":0,
}

for weight,occurence in data.items():
    if 75<float(weight)<100:
        mode_data["75-100"]+=occurence
    elif 100<float(weight)<125:
        mode_data["100-125"]+=occurence
    elif 125<float(weight)<150:
        mode_data["125-150"]+=occurence
    elif 150<float(weight)<175:
        mode_data["150-175"]+=occurence
mode_range,mode_occurence=0,0
for range,occurence in mode_data.items():
    if occurence>mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0]+mode_range[1])/2)
print(f"{mode:2f}")
