
d = int(input()) #distance
tank_size = int(input()) #tank size
n = int(input()) #n fueling stations
stations = list(map(int, input().split()))

def next_station(stations,tank_size):
    if not stations:
        return -1
    for ix,station in enumerate(stations):
        if station > tank_size:
            return ix - 1
    return ix

nstops = 0
while d > tank_size:
    #print(d)
    #print(stations)
    ix = next_station(stations,tank_size)
    if ix < 0:
        print(-1)
        quit()
    d = d - stations[ix]
    stations = [stations[i] - stations[ix] for i in range(len(stations))]
    del stations[0:ix+1]
    nstops += 1
print(nstops)
