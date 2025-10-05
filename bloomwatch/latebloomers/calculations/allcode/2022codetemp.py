import pandas

tem01_22=pandas.read_csv('Temperature data/2022temp/tavg-202201-cty-scaled.csv')
tem02_22=pandas.read_csv('Temperature data/2022temp/tavg-202202-cty-scaled.csv')
tem03_22=pandas.read_csv('Temperature data/2022temp/tavg-202203-cty-scaled.csv')
tem04_22=pandas.read_csv('Temperature data/2022temp/tavg-202204-cty-scaled.csv')
tem05_22=pandas.read_csv('Temperature data/2022temp/tavg-202205-cty-scaled.csv')
tem06_22=pandas.read_csv('Temperature data/2022temp/tavg-202206-cty-scaled.csv')
tem07_22=pandas.read_csv('Temperature data/2022temp/tavg-202207-cty-scaled.csv')
tem08_22=pandas.read_csv('Temperature data/2022temp/tavg-202208-cty-scaled.csv')
tem09_22=pandas.read_csv('Temperature data/2022temp/tavg-202209-cty-scaled.csv')
tem10_22=pandas.read_csv('Temperature data/2022temp/tavg-202210-cty-scaled.csv')
tem11_22=pandas.read_csv('Temperature data/2022temp/tavg-202211-cty-scaled.csv')
tem12_22=pandas.read_csv('Temperature data/2022temp/tavg-202212-cty-scaled.csv')

tem01_22=tem01_22.values.tolist()
tem02_22=tem02_22.values.tolist()
tem03_22=tem03_22.values.tolist()
tem04_22=tem04_22.values.tolist()
tem05_22=tem05_22.values.tolist()
tem06_22=tem06_22.values.tolist()
tem07_22=tem07_22.values.tolist()
tem08_22=tem08_22.values.tolist()
tem09_22=tem09_22.values.tolist()
tem10_22=tem10_22.values.tolist()
tem11_22=tem11_22.values.tolist()
tem12_22=tem12_22.values.tolist()

tem01_22_avg=[]
tem02_22_avg=[]
tem03_22_avg=[]
tem04_22_avg=[]
tem05_22_avg=[]
tem06_22_avg=[]
tem07_22_avg=[]
tem08_22_avg=[]
tem09_22_avg=[]
tem10_22_avg=[]
tem11_22_avg=[]
tem12_22_avg=[]


def avg(lst,lst2):
    for i in range(len(lst)):
        if 'CA: Kern County' == lst[i][2] or 'CA: Los Angeles County' == lst[i][2]:
            lst.append(lst[i][6:])
    del lst[0:3106]
    length=len(lst[0])
    for j in range(length):
        for i in range(len(lst)-1):
            lst2.append(round(((lst[i][j]+lst[i+1][j])/2),2))
    while -999.99 in lst2:
        lst2.remove(-999.99)
    return(lst2)

tem01_22_avg=avg(tem01_22,tem01_22_avg)
tem02_22_avg=avg(tem02_22,tem02_22_avg)
tem03_22_avg=avg(tem03_22,tem03_22_avg)
tem04_22_avg=avg(tem04_22,tem04_22_avg)
tem05_22_avg=avg(tem05_22,tem05_22_avg)
tem06_22_avg=avg(tem06_22,tem06_22_avg)
tem07_22_avg=avg(tem07_22,tem07_22_avg)
tem08_22_avg=avg(tem08_22,tem08_22_avg)
tem09_22_avg=avg(tem09_22,tem09_22_avg)
tem10_22_avg=avg(tem10_22,tem10_22_avg)
tem11_22_avg=avg(tem11_22,tem11_22_avg)
tem12_22_avg=avg(tem12_22,tem12_22_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

print(f'J {monthavg(tem01_22_avg)}')
print(f'F {monthavg(tem02_22_avg)}')
print(f'M {monthavg(tem03_22_avg)}')
print(f'A {monthavg(tem04_22_avg)}')
print(f'My {monthavg(tem05_22_avg)}')
print(f'J {monthavg(tem06_22_avg)}')
print(f'Jl {monthavg(tem07_22_avg)}')
print(f'Ag {monthavg(tem08_22_avg)}')
print(f'S {monthavg(tem09_22_avg)}')
print(f'O {monthavg(tem10_22_avg)}')
print(f'N {monthavg(tem11_22_avg)}')
print(f'D {monthavg(tem12_22_avg)}')