import csv
import numpy as np
import matplotlib.pyplot as plt

# file = str(input('Filename: '))
file = str('speed.csv')
file_name = file.split('.')[0]


def time_dif(rows):
    begin, end = rows[0], rows[-1]
    begin_h, begin_m, begin_s = int(begin[3]), int(begin[4]), int(begin[5])
    end_h, end_m, end_s =int(end[3]), int(end[4]), int(end[5])
    begin = np.array((begin_h, begin_m, begin_s), dtype=int)
    end = np.array((end_h, end_m, end_s), dtype=int)
    dif = end - begin
    if dif[2] < 0:
        dif[1] -= 1
        dif[2] += 60
    if dif[1] < 0:
        dif[0] -= 1
        dif[1] += 60
    seconds = dif[0] * 3600 + dif[1] * 60 + dif[2]
    return dif, seconds


with open(file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    lines = list(csv_reader)
    elapsed_time, elapsed_time_s = time_dif(lines)
    elapsed_time_s = int(elapsed_time_s)
    data = lines[1:-1]
    length_data = len(data)
    for i in range(len(data)):
        data[i] = float(data[i][0].split("'")[1])
    raw_data = np.array(data, dtype=float)
    filtered_data = np.delete(data, np.where(raw_data == 0.0))
    print("Max speed: {} km/h".format(np.amax(filtered_data)))
    print(length_data, elapsed_time_s)

plt.ylabel("Velocity (in km/h)")
plt.plot(filtered_data)
plt.savefig('{}_filtered_data.png'.format(file_name))

plt.show()
# speed.csv
