#imports for precipitation data
from .month_2021 import monthavg, csv01_21_avg, csv02_21_avg, csv03_21_avg, csv04_21_avg, csv05_21_avg, csv06_21_avg, csv07_21_avg, csv08_21_avg, csv09_21_avg, csv10_21_avg, csv11_21_avg, csv12_21_avg
from .month_2022 import monthavg, csv01_22_avg, csv02_22_avg, csv03_22_avg, csv04_22_avg, csv05_22_avg, csv06_22_avg, csv07_22_avg, csv08_22_avg, csv09_22_avg, csv10_22_avg, csv11_22_avg, csv12_22_avg
from .month_2023 import monthavg, csv01_avg, csv02_avg, csv03_avg, csv04_avg, csv05_avg, csv06_avg, csv07_avg, csv08_avg, csv09_avg, csv10_avg, csv11_avg, csv12_avg

#precipitation averages 2022
prec_june_sept_22_avg = round(((monthavg(csv06_21_avg) + monthavg(csv07_21_avg) + monthavg(csv08_21_avg) + monthavg(csv09_21_avg))/4), 4)
prec_oct_feb_22_avg = round(((monthavg(csv10_21_avg) + monthavg(csv11_21_avg) + monthavg(csv12_21_avg) + monthavg(csv01_22_avg) + monthavg(csv02_22_avg))/5), 4)

#precipitation averages 2023
prec_june_sept_23_avg = round(((monthavg(csv06_22_avg) + monthavg(csv07_22_avg) + monthavg(csv08_22_avg) + monthavg(csv09_22_avg))/4), 4)
prec_oct_feb_23_avg = round(((monthavg(csv10_22_avg) + monthavg(csv11_22_avg) + monthavg(csv12_22_avg) + monthavg(csv01_avg) + monthavg(csv02_avg))/5), 4)

#imports for temperature data
from .codetemp_2021 import monthavg, tem01_21_avg, tem02_21_avg, tem03_21_avg, tem04_21_avg, tem05_21_avg, tem06_21_avg, tem07_21_avg, tem08_21_avg, tem09_21_avg, tem10_21_avg, tem11_21_avg, tem12_21_avg
from .codetemp_2022 import monthavg, tem01_22_avg, tem02_22_avg, tem03_22_avg, tem04_22_avg, tem05_22_avg, tem06_22_avg, tem07_22_avg, tem08_22_avg, tem09_22_avg, tem10_22_avg, tem11_22_avg, tem12_22_avg
from .codetemp_2023 import monthavg, tem01_avg, tem02_avg, tem03_avg, tem04_avg, tem05_avg, tem06_avg, tem07_avg, tem08_avg, tem09_avg, tem10_avg, tem11_avg, tem12_avg

#temperature average 2022
temp_oct_feb_22_avg = round(((monthavg(tem10_21_avg) + monthavg(tem11_21_avg) + monthavg(tem12_21_avg) + monthavg(tem01_22_avg) + monthavg(tem02_22_avg))/5), 4)

#temperature average 2023
temp_oct_feb_23_avg = round(((monthavg(tem10_22_avg) + monthavg(tem11_22_avg) + monthavg(tem12_22_avg) + monthavg(tem01_avg) + monthavg(tem02_avg))/5), 4)

#Temperature variations!!
temp_variation_22 = round(((monthavg(tem10_21_avg) - monthavg(tem11_22_avg))+(monthavg(tem11_21_avg) - monthavg(tem12_21_avg))+(monthavg(tem01_22_avg) - monthavg(tem12_21_avg))+(monthavg(tem02_22_avg)-monthavg(tem01_22_avg))), 4)
temp_variation_23 = round(((monthavg(tem10_22_avg) - monthavg(tem11_avg))+(monthavg(tem11_22_avg) - monthavg(tem12_22_avg))+(monthavg(tem01_avg) - monthavg(tem12_22_avg))+(monthavg(tem02_avg)-monthavg(tem01_avg))), 4)


print(f'2022 June-Sept Average Precipitation: {prec_june_sept_22_avg} inches')