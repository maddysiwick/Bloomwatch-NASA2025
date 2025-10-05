import pandas

tem01_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202101-cty-scaled.csv')
tem02_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202102-cty-scaled.csv')
tem03_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202103-cty-scaled.csv')
tem04_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202104-cty-scaled.csv')
tem05_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202105-cty-scaled.csv')
tem06_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202106-cty-scaled.csv')
tem07_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202107-cty-scaled.csv')
tem08_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202108-cty-scaled.csv')
tem09_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202109-cty-scaled.csv')
tem10_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202110-cty-scaled.csv')
tem11_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202111-cty-scaled.csv')
tem12_21=pandas.read_csv('bloomwatch/latebloomers/calculations/Temperature data/2021temp/tavg-202112-cty-scaled.csv')

tem01_21=tem01_21.values.tolist()
tem02_21=tem02_21.values.tolist()
tem03_21=tem03_21.values.tolist()
tem04_21=tem04_21.values.tolist()
tem05_21=tem05_21.values.tolist()
tem06_21=tem06_21.values.tolist()
tem07_21=tem07_21.values.tolist()
tem08_21=tem08_21.values.tolist()
tem09_21=tem09_21.values.tolist()
tem10_21=tem10_21.values.tolist()
tem11_21=tem11_21.values.tolist()
tem12_21=tem12_21.values.tolist()

tem01_21_avg=[]
tem02_21_avg=[]
tem03_21_avg=[]
tem04_21_avg=[]
tem05_21_avg=[]
tem06_21_avg=[]
tem07_21_avg=[]
tem08_21_avg=[]
tem09_21_avg=[]
tem10_21_avg=[]
tem11_21_avg=[]
tem12_21_avg=[]


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

tem01_21_avg=avg(tem01_21,tem01_21_avg)
tem02_21_avg=avg(tem02_21,tem02_21_avg)
tem03_21_avg=avg(tem03_21,tem03_21_avg)
tem04_21_avg=avg(tem04_21,tem04_21_avg)
tem05_21_avg=avg(tem05_21,tem05_21_avg)
tem06_21_avg=avg(tem06_21,tem06_21_avg)
tem07_21_avg=avg(tem07_21,tem07_21_avg)
tem08_21_avg=avg(tem08_21,tem08_21_avg)
tem09_21_avg=avg(tem09_21,tem09_21_avg)
tem10_21_avg=avg(tem10_21,tem10_21_avg)
tem11_21_avg=avg(tem11_21,tem11_21_avg)
tem12_21_avg=avg(tem12_21,tem12_21_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

print(f'J {monthavg(tem01_21_avg)}')
print(f'F {monthavg(tem02_21_avg)}')
print(f'M {monthavg(tem03_21_avg)}')
print(f'A {monthavg(tem04_21_avg)}')
print(f'My {monthavg(tem05_21_avg)}')
print(f'J {monthavg(tem06_21_avg)}')
print(f'Jl {monthavg(tem07_21_avg)}')
print(f'Ag {monthavg(tem08_21_avg)}')
print(f'S {monthavg(tem09_21_avg)}')
print(f'O {monthavg(tem10_21_avg)}')
print(f'N {monthavg(tem11_21_avg)}')
print(f'D {monthavg(tem12_21_avg)}')