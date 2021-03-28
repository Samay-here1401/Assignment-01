from additional import car
from additional import city
from additional import path_plot

city_list = list()
car_list = list()

e12 = 12
e13 = 16
e23 = 17

B1= 100
M1= 100
C1= 1
S1= 1
D1= 1

B2= 100
M2= 100
C2= 1
S2= 1
D2= 1

B3= 100
M3= 100
C3= 1
S3= 1
D3= 1
V1 = city(0,C1,[0,e12,e13])
V2 = city(1,C2,[e12,0,e23])
V3 = city(2,C3,[e13,e23,0])

c1 = car(V1,V2,B1,D1,M1,S1)
c2 = car(V2,V3,B2,D2,M2,S2)
c3 = car(V3,V1,B3,D3,M3,S3)

city_list = [V1,V2,V3]
car_list = [c1,c2,c3]

for i in range(len(car_list)):
    path_plot(car_list[i],city_list).path.reverse()

print("Path : ")

for i in car_list:
    print(i.path)

print()
print("Time Taken : ")

min = 0

for i in car_list:
    if min < i.tot_time :
        min = i.tot_time
    print(i.tot_time)

print()
print("Tr : ")
print(min)
