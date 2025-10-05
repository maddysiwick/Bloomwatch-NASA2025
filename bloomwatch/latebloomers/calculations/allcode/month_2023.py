import pandas

csv01=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202301-cty-scaled.csv')
csv02=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202302-cty-scaled.csv')
csv03=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202303-cty-scaled.csv')
csv04=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202304-cty-scaled.csv')
csv05=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202305-cty-scaled.csv')
csv06=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202306-cty-scaled.csv')
csv07=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202307-cty-scaled.csv')
csv08=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202308-cty-scaled.csv')
csv09=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202309-cty-scaled.csv')
csv10=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202310-cty-scaled.csv')
csv11=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202311-cty-scaled.csv')
csv12=pandas.read_csv('bloomwatch/latebloomers/calculations/Rainfall data/cnty/prcp-202312-cty-scaled.csv')

csv01=csv01.values.tolist()
csv02=csv02.values.tolist()
csv03=csv03.values.tolist()
csv04=csv04.values.tolist()
csv05=csv05.values.tolist()
csv06=csv06.values.tolist()
csv07=csv07.values.tolist()
csv08=csv08.values.tolist()
csv09=csv09.values.tolist()
csv10=csv10.values.tolist()
csv11=csv11.values.tolist()
csv12=csv12.values.tolist()

csv01_avg=[]
csv02_avg=[]
csv03_avg=[]
csv04_avg=[]
csv05_avg=[]
csv06_avg=[]
csv07_avg=[]
csv08_avg=[]
csv09_avg=[]
csv10_avg=[]
csv11_avg=[]
csv12_avg=[]


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

csv01_avg=avg(csv01,csv01_avg)
csv02_avg=avg(csv02,csv02_avg)
csv03_avg=avg(csv03,csv03_avg)
csv04_avg=avg(csv04,csv04_avg)
csv05_avg=avg(csv05,csv05_avg)
csv06_avg=avg(csv06,csv06_avg)
csv07_avg=avg(csv07,csv07_avg)
csv08_avg=avg(csv08,csv08_avg)
csv09_avg=avg(csv09,csv09_avg)
csv10_avg=avg(csv10,csv10_avg)
csv11_avg=avg(csv11,csv11_avg)
csv12_avg=avg(csv12,csv12_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

print(f'J {monthavg(csv01_avg)}')
print(f'F {monthavg(csv02_avg)}')
print(f'M {monthavg(csv03_avg)}')
print(f'A {monthavg(csv04_avg)}')
print(f'My {monthavg(csv05_avg)}')
print(f'J {monthavg(csv06_avg)}')
print(f'Jl {monthavg(csv07_avg)}')
print(f'Ag {monthavg(csv08_avg)}')
print(f'S {monthavg(csv09_avg)}')
print(f'O {monthavg(csv10_avg)}')
print(f'N {monthavg(csv11_avg)}')
print(f'D {monthavg(csv12_avg)}')

