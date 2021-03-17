
people = [('Lisboa','LIS'),
        ('Madrid','MAD'),
        ('Paris','CDG'),
        ('Dublin','DUB'),
        ('Bruxelas','BRU'),
        ('Londres','LHR')]

flights_data = {}
def gen_data(data,path):
    for line in open(path):
        origin,destination,out_time,arrival_time,price = line.split(',')
        data.setdefault((origin,destination),[])
        data[(origin,destination)].append((out_time,arrival_time,int(price)))
    
gen_data(flights_data,'AlgorítimoOtimizacao/flights.txt')

print(flights_data)