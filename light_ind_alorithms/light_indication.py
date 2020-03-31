import pandas as pd



df_zones= pd.read_csv('traffic_light_algo_data.csv',header=None) 

time_start=df_zones[df_zones[0]==df_zones[0].min()].iloc[0][0]
time_end=df_zones[df_zones[0]==df_zones[0].max()].iloc[0][0]
array=[]
for i in range(time_start,time_end+1):
    array.append([i,'r'])




df_zones_12=df_zones[((df_zones[2]==1) | (df_zones[2]==2)) & (df_zones[1]==2)]

print(df_zones_12.head(10))

differencedf=pd.DataFrame()
differencedf['Timedifference']=df_zones_12.diff()[0]

differencedf['Time']=df_zones_12[0]
differencedf['mode']=df_zones_12[1]
differencedf['zone']=df_zones_12[2]
differencedf.drop(differencedf.index[0])
differencedf15=differencedf[differencedf['Timedifference']>15]


for index, row in differencedf15.iterrows():
    print(row)
    for index in range(0,len(array)):
        if ((array[index][0] <=row[1]) and (array[index][0]  >=row[1]-row[0])):
            array[index][1] = 'green'
            print('greeen',array[index][0])
        
            # # array[index][1] = 'red'
            # print('red',array[index][0])
pd.DataFrame(array).to_csv('traffic_light_results.csv')          


#time , density, and zone
