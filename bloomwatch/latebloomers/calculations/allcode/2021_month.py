import pandas

csv01_21=pandas.read_csv('Rainfall data/cnty/prcp-202301-cty-scaled.csv')
csv02_21=pandas.read_csv('Rainfall data/cnty/prcp-202302-cty-scaled.csv')
csv03_21=pandas.read_csv('Rainfall data/cnty/prcp-202303-cty-scaled.csv')
csv04_21=pandas.read_csv('Rainfall data/cnty/prcp-202304-cty-scaled.csv')
csv05_21=pandas.read_csv('Rainfall data/cnty/prcp-202305-cty-scaled.csv')
csv06_21=pandas.read_csv('Rainfall data/cnty/prcp-202306-cty-scaled.csv')
csv07_21=pandas.read_csv('Rainfall data/cnty/prcp-202307-cty-scaled.csv')
csv08_21=pandas.read_csv('Rainfall data/cnty/prcp-202308-cty-scaled.csv')
csv09_21=pandas.read_csv('Rainfall data/cnty/prcp-202309-cty-scaled.csv')
csv10_21=pandas.read_csv('Rainfall data/cnty/prcp-202310-cty-scaled.csv')
csv11_21=pandas.read_csv('Rainfall data/cnty/prcp-202311-cty-scaled.csv')
csv12_21=pandas.read_csv('Rainfall data/cnty/prcp-202312-cty-scaled.csv')

csv01_21=csv01_21.values.tolist()
csv02_21=csv02_21.values.tolist()
csv03_21=csv03_21.values.tolist()
csv04_21=csv04_21.values.tolist()
csv05_21=csv05_21.values.tolist()
csv06_21=csv06_21.values.tolist()
csv07_21=csv07_21.values.tolist()
csv08_21=csv08_21.values.tolist()
csv09_21=csv09_21.values.tolist()
csv10_21=csv10_21.values.tolist()
csv11_21=csv11_21.values.tolist()
csv12_21=csv12_21.values.tolist()

csv01_21_avg=[]
csv02_21_avg=[]
csv03_21_avg=[]
csv04_21_avg=[]
csv05_21_avg=[]
csv06_21_avg=[]
csv07_21_avg=[]
csv08_21_avg=[]
csv09_21_avg=[]
csv10_21_avg=[]
csv11_21_avg=[]
csv12_21_avg=[]


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

csv01_21_avg=avg(csv01_21,csv01_21_avg)
csv02_21_avg=avg(csv02_21,csv02_21_avg)
csv03_21_avg=avg(csv03_21,csv03_21_avg)
csv04_21_avg=avg(csv04_21,csv04_21_avg)
csv05_21_avg=avg(csv05_21,csv05_21_avg)
csv06_21_avg=avg(csv06_21,csv06_21_avg)
csv07_21_avg=avg(csv07_21,csv07_21_avg)
csv08_21_avg=avg(csv08_21,csv08_21_avg)
csv09_21_avg=avg(csv09_21,csv09_21_avg)
csv10_21_avg=avg(csv10_21,csv10_21_avg)
csv11_21_avg=avg(csv11_21,csv11_21_avg)
csv12_21_avg=avg(csv12_21,csv12_21_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

print(f'J {monthavg(csv01_21_avg)}')
print(f'F {monthavg(csv02_21_avg)}')
print(f'M {monthavg(csv03_21_avg)}')
print(f'A {monthavg(csv04_21_avg)}')
print(f'My {monthavg(csv05_21_avg)}')
print(f'J {monthavg(csv06_21_avg)}')
print(f'Jl {monthavg(csv07_21_avg)}')
print(f'Ag {monthavg(csv08_21_avg)}')
print(f'S {monthavg(csv09_21_avg)}')
print(f'O {monthavg(csv10_21_avg)}')
print(f'N {monthavg(csv11_21_avg)}')
print(f'D {monthavg(csv12_21_avg)}')

