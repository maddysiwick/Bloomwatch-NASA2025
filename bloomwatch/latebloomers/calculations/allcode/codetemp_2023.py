import pandas

tem01=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202301-cty-scaled.csv')
tem02=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202302-cty-scaled.csv')
tem03=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202303-cty-scaled.csv')
tem04=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202304-cty-scaled.csv')
tem05=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202305-cty-scaled.csv')
tem06=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202306-cty-scaled.csv')
tem07=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202307-cty-scaled.csv')
tem08=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202308-cty-scaled.csv')
tem09=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202309-cty-scaled.csv')
tem10=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202310-cty-scaled.csv')
tem11=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202311-cty-scaled.csv')
tem12=pandas.read_csv('latebloomers/calculations/Temperature data/2023temp/tavg-202312-cty-scaled.csv')

tem01=tem01.values.tolist()
tem02=tem02.values.tolist()
tem03=tem03.values.tolist()
tem04=tem04.values.tolist()
tem05=tem05.values.tolist()
tem06=tem06.values.tolist()
tem07=tem07.values.tolist()
tem08=tem08.values.tolist()
tem09=tem09.values.tolist()
tem10=tem10.values.tolist()
tem11=tem11.values.tolist()
tem12=tem12.values.tolist()

tem01_avg=[]
tem02_avg=[]
tem03_avg=[]
tem04_avg=[]
tem05_avg=[]
tem06_avg=[]
tem07_avg=[]
tem08_avg=[]
tem09_avg=[]
tem10_avg=[]
tem11_avg=[]
tem12_avg=[]


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

tem01_avg=avg(tem01,tem01_avg)
tem02_avg=avg(tem02,tem02_avg)
tem03_avg=avg(tem03,tem03_avg)
tem04_avg=avg(tem04,tem04_avg)
tem05_avg=avg(tem05,tem05_avg)
tem06_avg=avg(tem06,tem06_avg)
tem07_avg=avg(tem07,tem07_avg)
tem08_avg=avg(tem08,tem08_avg)
tem09_avg=avg(tem09,tem09_avg)
tem10_avg=avg(tem10,tem10_avg)
tem11_avg=avg(tem11,tem11_avg)
tem12_avg=avg(tem12,tem12_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

print(f'J {monthavg(tem01_avg)}')
print(f'F {monthavg(tem02_avg)}')
print(f'M {monthavg(tem03_avg)}')
print(f'A {monthavg(tem04_avg)}')
print(f'My {monthavg(tem05_avg)}')
print(f'J {monthavg(tem06_avg)}')
print(f'Jl {monthavg(tem07_avg)}')
print(f'Ag {monthavg(tem08_avg)}')
print(f'S {monthavg(tem09_avg)}')
print(f'O {monthavg(tem10_avg)}')
print(f'N {monthavg(tem11_avg)}')
print(f'D {monthavg(tem12_avg)}')