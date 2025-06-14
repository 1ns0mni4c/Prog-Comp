from datetime import datetime, timedelta

def calculate_offset(time, offset):
    dt = datetime.combine(datetime.today(), time)
    offset_dt = dt - timedelta(seconds=offset)
    
    return offset_dt.time()

def parse_data(data):
    lines = data.strip().split("\n")
    num_times = int(lines[0])
    times = []

    for i in range(1, num_times + 1):
        times.append(lines[i])
    
    countries = {}
    for i in range(num_times + 1, len(lines)):
        parts = lines[i].rsplit(" ", 1)
        country = parts[0]
        offset = int(parts[1])
        countries[country] = offset
    
    return times, countries

data = """""" #Input data goes here
times, countries = parse_data(data)

for index, time in enumerate(times):
    time_obj = datetime.strptime(time, "%H:%M:%S").time()
    times[index] = time_obj

offsets = {}
sorted_countries = []

for time in times:
    current_offsets = {}

    for country, offset in countries.items():
        offset_time = calculate_offset(time, offset)
        current_offsets[country] = offset_time.strftime("%H:%M:%S")
    
    for country1, time1 in current_offsets.items():
        for country2, time2 in offsets.items():
            if time1 == time2:
                if country2 not in sorted_countries:
                    sorted_countries.append(country2)
                
                sorted_countries.append(country1)

    offsets = current_offsets

if sorted_countries:
    print(sorted_countries)
else:
    print("Impossible")