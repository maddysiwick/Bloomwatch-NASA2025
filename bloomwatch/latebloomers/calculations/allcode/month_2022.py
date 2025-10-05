import pandas

csv01_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202201-cty-scaled.csv')
csv02_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202202-cty-scaled.csv')
csv03_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202203-cty-scaled.csv')
csv04_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202204-cty-scaled.csv')
csv05_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202205-cty-scaled.csv')
csv06_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202206-cty-scaled.csv')
csv07_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202207-cty-scaled.csv')
csv08_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202208-cty-scaled.csv')
csv09_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202209-cty-scaled.csv')
csv10_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202210-cty-scaled.csv')
csv11_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202211-cty-scaled.csv')
csv12_22=pandas.read_csv('latebloomers/calculations/Rainfall data/cnty/2022/prcp-202212-cty-scaled.csv')

csv01_22=csv01_22.values.tolist()
csv02_22=csv02_22.values.tolist()
csv03_22=csv03_22.values.tolist()
csv04_22=csv04_22.values.tolist()
csv05_22=csv05_22.values.tolist()
csv06_22=csv06_22.values.tolist()
csv07_22=csv07_22.values.tolist()
csv08_22=csv08_22.values.tolist()
csv09_22=csv09_22.values.tolist()
csv10_22=csv10_22.values.tolist()
csv11_22=csv11_22.values.tolist()
csv12_22=csv12_22.values.tolist()

csv01_22_avg=[]
csv02_22_avg=[]
csv03_22_avg=[]
csv04_22_avg=[]
csv05_22_avg=[]
csv06_22_avg=[]
csv07_22_avg=[]
csv08_22_avg=[]
csv09_22_avg=[]
csv10_22_avg=[]
csv11_22_avg=[]
csv12_22_avg=[]


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

csv01_avg=avg(csv01_22,csv01_22_avg)
csv02_avg=avg(csv02_22,csv02_22_avg)
csv03_avg=avg(csv03_22,csv03_22_avg)
csv04_avg=avg(csv04_22,csv04_22_avg)
csv05_avg=avg(csv05_22,csv05_22_avg)
csv06_avg=avg(csv06_22,csv06_22_avg)
csv07_avg=avg(csv07_22,csv07_22_avg)
csv08_avg=avg(csv08_22,csv08_22_avg)
csv09_avg=avg(csv09_22,csv09_22_avg)
csv10_avg=avg(csv10_22,csv10_22_avg)
csv11_avg=avg(csv11_22,csv11_22_avg)
csv12_avg=avg(csv12_22,csv12_22_avg)

def monthavg(lst3):
    monthly_rain=(sum(lst3))/(len(lst3))
    return(round(monthly_rain,2))

