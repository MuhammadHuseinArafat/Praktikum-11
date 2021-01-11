from datetime import *

def diffDate(x):
    sekarang = datetime.date(datetime.now())
    x = x.split('-')
    x = date(int(x[0]),int(x[1]),int(x[2]))
    result = x - sekarang
    result = result.days
    print (result)

diffDate('2021-01-20')
