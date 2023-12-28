def calc_armstrong_numbers():
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                if x*100 + y*10 + z == x**3 + y**3 + z**3:
                    print(x, y, z)

def calc_armstrong_numbers1():
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                if x*100 + y*10 + z == x**3 + y**3 + z**3:
                    print("Case 1")
                    print(x, y, z)
                if x*100 + y*10 + z == x**1 + y**2 + z**3:
                    print("Case 2")
                    print(x, y, z)   
                if x*100 + y*10 + z == x**3 + y**2 + z**1:
                    print("Case 3")
                    print(x, y, z)                 

calc_armstrong_numbers1()