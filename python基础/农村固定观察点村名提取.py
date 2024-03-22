import pandas as pd
import jionlp as jio

data = pd.read_excel("C:\\Users\\CYH10\\Desktop\\村名.xlsx")
df = pd.DataFrame(data)
for i in range(len(data['村名'])):
    res = jio.parse_location(data['村名'][i])
    if res != "":
        df.loc[i, '县名'] = res['county']
    if res == "":
        df.loc[i, '县名'] =
df.to_excel("C:\\Users\\CYH10\\Desktop\\村名_adj.xlsx")