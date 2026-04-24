#Design and develop a distributed application to find the coolest/hottest year from the available
#weather data. Use weather data from the Internet and process it using MapReduce.

data = [
    (2001,30),(2001,32),
    (2002,28),(2002,29),
    (2003,35),(2003,36),
    (2004,25),(2004,27)
]

def mapper(data):
    mapped=[]
    for record in data:
        year,temp=record
        mapped.append((year,temp))
    return mapped

def shuffle_sort(mapped_data):
    grouped={}
    for year,temp in mapped_data:
        if year not in grouped :
            grouped[year]=[]
        grouped[year].append(temp)
    return grouped

def reducer(grouped_data):
    avg_temp={}
    for year,temps in grouped_data.items():
        avg_temp[year]=sum(temps)/len(temps)
    return avg_temp

mapped=mapper(data)
grouped=shuffle_sort(mapped)
result=reducer(grouped)

hottest_year = max(result,key=result.get)
coolest_year = min(result,key=result.get)
print('Average Temperature per Year :',result)
print('Hottest year :',hottest_year)
print('Coolest year :',coolest_year)
