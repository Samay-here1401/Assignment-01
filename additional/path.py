from additional import car
from additional import city

def path_plot(car_s: car, city_list):
    class node:
        def __init__(self, cty: city, pred = None, h_cost = None, t_cost = None):
            self.cty = cty
            self.pred = pred
            self.h_cost = h_cost
            self.t_cost = t_cost
            self.f_cost = None
    node_list = list()
    for i in city_list:
        x = node(i)
        node_list.append(x)


    # supply heuristic value #
    op = list()
    op.append(car_s.dest.num)
    node_list[car_s.dest.num].h_cost = 0
    while(len(op) != 0):
        i = op.pop(0)
        for j in range(len(city_list[i].dist)):
            if city_list[i].dist[j] is not None:
                if node_list[j].h_cost is None:
                    node_list[j].h_cost = city_list[i].dist[j] + node_list[i].h_cost
                    op.append(j)
                elif node_list[j].h_cost > (city_list[i].dist[j] + node_list[i].h_cost):
                    node_list[j].h_cost = city_list[i].dist[j] + node_list[i].h_cost
                    op.append(j)
    #heuristic calculation done... #


    # A* algorithm search #
    closed = list()
    opent = list()
    opent.append(car_s.src.num)
    node_list[car_s.src.num].t_cost = 0
    node_list[car_s.src.num].f_cost = node_list[car_s.src.num].h_cost
    while(len(opent) != 0):
        i = opent.pop(0)
        if i == car_s.dest.num:
            #terminate
            break
        for j in range(len(city_list[i].dist)):
            if city_list[i].dist[j] is not None and city_list[i].dist[j] != 0 and city_list[i].dist[j] <= ((car_s.max_cap * car_s.avg_speed)/car_s.discrg_rate):
                cost = (city_list[i].dist[j]/car_s.avg_speed)*(1 + (car_s.discrg_rate/city_list[i].crg_rate))
                g = cost + (node_list[j].h_cost/car_s.avg_speed)
                if j not in opent and j not in closed:
                    node_list[j].t_cost = cost + node_list[i].t_cost
                    node_list[j].f_cost = node_list[i].t_cost + g
                    node_list[j].pred = i
                    opent.append(j)
                elif j in opent:
                    if node_list[j].t_cost > cost + node_list[i].t_cost:
                        node_list[j].t_cost = cost + node_list[i].t_cost
                        node_list[j].f_cost = node_list[i].t_cost + g
                        node_list[j].pred = i

    # A* search completed... optimal path found #

    # charge time optimisation #
    path = [car_s.src.num]
    i = car_s.dest.num
    while i == car_s.src.num:
        path.insert(0,i)
        i = node_list[i].pred
    path.insert(0,i)
    crg_list = [0]*len(path)
    min_crg = 0
    curr_crg = car_s.init_chrg
    rate = [0]*len(path)
    for i in range(len(path)):
        rate[i] = city_list[i].crg_rate
    for i in range(len(path)-1):
        di = city_list[path[i]].dist[path[i+1]]
        cost_crg = (di/car_s.avg_speed)*car_s.discrg_rate
        min_crg += cost_crg
        while min_crg > curr_crg:
            rt = rate[:i+1]
            k = rt.index(min(rt))
            if (min_crg - curr_crg) > (car_s.max_cap - crg_list[k]):
                min_crg = min_crg - (car_s.max_cap - crg_list[k])
                rate[k] = 0
                crg_list[k] = car_s.max_cap
            else:
                crg_list[k] += min_crg - curr_crg
                min_crg = curr_crg
    # optimised crg_list obtained
    car_s.path = path
    # creating time stamp for each stop
    curr_time = 0
    for i in range(len(path) - 1):
        crg_time = crg_list[i] * city_list[path[i]].crg_rate
        car_s.crg_time_stamp.append([curr_time, crg_time])
        curr_time += crg_time
        curr_time += city_list[path[i]].dist[path[i+1]] / car_s.avg_speed

    car_s.tot_time = curr_time
    # time of travel obtained

    return car_s
