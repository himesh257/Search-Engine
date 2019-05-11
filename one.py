import datetime

now = datetime.datetime.now()

date = []
a = [1,2,4,4]
b = ["h","i","m", "e"]

    
with open('history.txt') as f:
    i = 0
    x = f.read().splitlines()
    while i < 2:
        print("--------------------")
        print(i)
        print(x[i])
        i += 1
        
print(date)
    
    
