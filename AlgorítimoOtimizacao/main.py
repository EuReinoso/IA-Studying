
def gen_data(path):
    data = {}
    for line in open(path):
        origin, destination, out_time, arrival_time, price = line.split(',')
        data.setdefault((origin, destination), [])
        data[(origin, destination)].append((out_time, arrival_time, int(price)))
    return data

def print_flights(schedule,data):
    index = -1
    total_price = 0
    for i in range(len(schedule)//2):
        name = people[i][0]
        origin = people[i][1]
        index += 1
        out = data[(origin,destination)][schedule[index]]
        total_price += out[2]
        index += 1
        come_back = data[(destination,origin)][schedule[index]]
        total_price += come_back[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' %(name,origin,out[0],out[1],out[2],
                                                    come_back[0],come_back[1],come_back[2]))
    print("Total Price:", total_price)

def fitness_function(schedule,data):
    index = -1
    total_price = 0
    for i in range(len(schedule)//2):
        origin = people[i][1]
        index += 1
        out = data[(origin,destination)][schedule[index]]
        total_price += out[2]
        index += 1
        come_back = data[(destination,origin)][schedule[index]]
        total_price += come_back[2]
    return total_price


people = [('Lisboa', 'LIS'),
        ('Madrid', 'MAD'),
        ('Paris', 'CDG'),
        ('Dublin', 'DUB'),
        ('Bruxelas', 'BRU'),
        ('Londres', 'LHR')]

flights_data = {}
flights_data = gen_data('AlgorítimoOtimizacao/flights.txt')
destination = 'FCO'
schedule = [1,0, 3,2, 7,1, 6,3, 2,4, 5,3]

# fitness =  mlrose.CustomFitness(fitness_function(schedule,flights_data))

# problem = mlrose.DiscretedOpt(lenght=12, fitness_fn=fitness, maximize=False, max_val=10)

# # best_solution, best_cost = mlrose.hill_climb(problem)

# print_flights(best_solution,flights_data)