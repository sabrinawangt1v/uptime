from datetime import timedelta, datetime, date
import connect
import pandas as pd
import numpy as np

conn = connect.connect()


customer_devices={'Annie E Casey':['t1v-th-226','t1v-th-323','t1v-th-324','t1v-th-325','t1v-th-326'],
'AQR Global':['t1v-th-410'], 'Brandywine Global (Cenero)':['t1v-th-356','t1v-th-357','t1v-th-358'],
'Collins Aerospace - Charlotte':['t1v-th-567','t1v-th-568','t1v-th-569','t1v-th-570','t1v-th-573','t1v-th-574','t1v-th-575','t1v-th-576','t1v-th-577','t1v-th-579','t1v-th-580','t1v-th-581','t1v-th-750','t1v-th-751','t1v-th-754','t1v-th-756','t1v-th-757'],
'Comporium':['comp-table10','comp-table5','comp-table6','comp-table7','comp-table8','comp-table9','comp-wall1','comp-wall2','comp-wall3','comp-wall4','comp-wall5','comp-wall6'],
'Duke University':['dukealumni-connector','dukealumni-forlineswall1','dukealumni-vestibule1','dukealumni-vestibule2','dukealumni-welcomedesk'],
'IBM (HB Communications)':['t1v-th-538','t1v-th-539','t1v-th-539'],
'IBM (Intellicom)':['t1v-th-447'],
'IDEX':['t1v-th-280'],
'Makino (Bluewater)':['t1v-th-318','t1v-th-319','t1v-th-321','t1v-th-606'],
'MSP (Bluewater)':['t1v-th-294','t1v-th-295','t1v-th-296','t1v-th-297','t1v-th-298','t1v-th-299','t1v-th-300','t1v-th-301','t1v-th-455','t1v-th-460','t1v-th-699',],
'Moffitt (AVISPL)':['t1v-th-811'],
'Omnicell (Avidex)':['t1v-th-309','t1v-th-309'],
'Oshkosh':['ms-serv-oshkosh','t1v-th-611','t1v-th-612','t1v-th-613','t1v-th-614','t1v-th-615','t1v-th-616','t1v-th-617','t1v-th-618','t1v-th-619','t1v-th-620','t1v-th-621','t1v-th-622','t1v-th-623','t1v-th-624','t1v-th-625','t1v-th-626','t1v-th-627','t1v-th-628','t1v-th-629','t1v-th-630','t1v-th-631','t1v-th-632','t1v-th-633','t1v-th-634','t1v-th-638','t1v-th-639','t1v-th-658','t1v-th-659','t1v-th-660','t1v-th-661','t1v-th-662','t1v-th-663','t1v-th-664','t1v-th-665','t1v-th-666','t1v-th-668','t1v-th-669','t1v-th-671','t1v-th-673','t1v-th-674','t1v-th-675','t1v-th-676','t1v-th-677','t1v-th-678','t1v-th-679','t1v-th-680','t1v-th-681','t1v-th-683','t1v-th-684','t1v-th-686','t1v-th-688','t1v-th-689','t1v-th-691','t1v-th-693','t1v-th-694','t1v-th-695','t1v-th-696','t1v-th-706','t1v-th-787'],
'Queens University':['t1v-th-379'],
'Quinnipiac University':['t1v-th-232','t1v-th-233'],
'TAMU EEC (Avinext)':['t1v-th-654','zeec-t1v-124-fpd','zeec-t1v-130D-fpd','zeec-t1v-133-fpd','zeec-t1v-136-fpd','zeec-t1v-150-th','zeec-t1v-161-fpd','zeec-t1v-214-th','zeec-t1v-224-fpd','zeec-t1v-230-fpd','zeec-t1v-233-fpd','zeec-t1v-265-fpd','zeec-t1v-282m-th','zeec-t1v-324-fpd','zeec-t1v-330-fpd','zeec-t1v-333-fpd','zeec-t1v-354-fpd','zeec-t1v-382g-th','zeec-t1v-430-th','zeec-t1v-450f-th','zeec-t1v-500m-th','zeec-t1v-583-th','zeec-t1v-594-th','t1v-th-654','zeec-t1v-150-th','zeec-t1v-214-th','zeec-t1v-282m-th','zeec-t1v-382g-th','zeec-t1v-430-th','zeec-t1v-450f-th','zeec-t1v-500m-th','zeec-t1v-583-th','t1v-th-654','t1v-th-771'],
'UNCC':['uncc-wall2','unccfoundation-wall1'],
'University of St. Thomas':['t1v-th-143','t1v-th-144','t1v-th-145','t1v-th-146','t1v-th-147','t1v-th-148','t1v-th-149','t1v-th-151','t1v-th-152','t1v-th-153','t1v-th-154','t1v-th-155','t1v-th-156','t1v-th-157','t1v-th-158','t1v-th-169','t1v-th-204'],
'UW-Madison':['t1v-th-210','t1v-th-650','t1v-th-652','t1v-th-650','t1v-th-652','t1v-th-210'],
'Wells Fargo':['wellslab-wall1a','wellslab-wall2','wellslab-wall3','wellslab-wall4','wellslab-wall5']}

Customer_aliases=['AARP','Angelo-State University','Annie E Casey','AQR','Columbia U','Collins Aerospace - Charlotte','Comcast','Comporium','Duke University",''Eli Lilly','Florida Virtual Campus (UWF)','IBM NY', 'IBM Raleigh','IDEX','Kingsmen','Lifetime Fitness','Makino','Michigan State Police','Omnicell','Oshkosh','Queens University','Quinnipiac University','Texas A&M','Texas Tech University','UNCC','University of St. Thomas','University of Wisconsin','Wells Fargo']

# # of devices owned by each customer
number_devices={i:len(customer_devices[i]) for i in customer_devices}
# list of customers
Customers=[customer_devices]

# retrieve a flattened list of all devices owned by tier1 customers
devices=customer_devices.values()
All_devices=[]
def reemovNestings(l):
    for i in l:
            if type(i) == list:
                reemovNestings(i)
            else:
                All_devices.append(i)

reemovNestings(devices)
All_devices=tuple(All_devices)

# query to get 30 day average uptime below 99%; returns devices with low uptime and uptime percent
query2= """
select device, avg(uptime_percent) from
    (select device,
    (sum(cast(info->>'active_hours' as float))-(coalesce(sum(cast(info->>'diag_hang' as int)),0)*.5+coalesce(sum(cast(info->>'ttmenu_crashes' as int)),0)*2)/60)/sum(cast(info->>'active_hours' as float)) as uptime_percent
    from daily_device_summary where
    date between '2019-02-01' and '2019-02-29' and device in {}
    group by device
    order by 1) as derivedTable
    group by device
    having avg(uptime_percent)<0.99
    order by 1
"""
# having avg(uptime_percent)<0.99
# having (sum(cast(info->>'active_hours' as float))-(coalesce(sum(cast(info->>'diag_hang' as int)),0)*.5+coalesce(sum(cast(info->>'ttmenu_crashes' as int)), 0)*2)/60)/sum(cast(info->>'active_hours' as float)) < .995


#create dataframe for uptime_percent
query_uptime=query2.format(All_devices)
df_uptime1=(pd.read_sql(query_uptime,con=conn).fillna(0))

low_uptime_devices=df_uptime1['device'].tolist()
low_uptime_customer=[]

for i in low_uptime_devices:
    for j in customer_devices:
        if i in customer_devices[j]:
            low_uptime_customer.append(j)

# generate dataframe showing low uptime devices and their corresponding customers
# add customer column to low uptime dataframe
df_uptime1['low_uptime_customer']=low_uptime_customer
print(df_uptime1)

# count low uptime device owned by each tier-1 customer
low_uptime_count = {i:low_uptime_customer.count(i) for i in low_uptime_customer}


dict_report={}
for i in number_devices:
    if i in low_uptime_count:
        dict_report[i]=low_uptime_count[i]/number_devices[i]
    else:
        dict_report[i]=0

df_uptime_report=pd.DataFrame.from_dict(dict_report, orient='index')
df_uptime_report.to_csv('uptime_report.csv')
df_uptime1.to_csv('low_uptime_devices_customers.csv')
