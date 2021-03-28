class city:
    def __init__(self, num: int, crg_rate: float, dist_arr: list):
        self.num = num
        self.crg_rate = crg_rate #charging rate
        self.dist = dist_arr #dist_mat[num] #distance from other cities (list)

class car:
    def __init__(self, source: city, dest: city, Bat_in: float, discrg_rate: float, max_cap: float, avg_speed: float):
        self.src = source
        self.dest = dest #destination city
        self.init_chrg = Bat_in #initial charge in the battery
        self.discrg_rate = discrg_rate #discharge rate
        self.max_cap = max_cap #maximum charge in battery
        self.avg_speed = avg_speed
        self.crg_time_stamp = list()
        self.tot_time = None
        self.path = list()
