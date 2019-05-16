
# coding: utf-8

# In[16]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[17]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[18]:


cursor = conn.cursor()


# In[19]:


dlist = []
with open("companion_planting.csv", encoding='latin') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[26]:



for i in range(0, len(dlist)):
    print(dlist[i][1])
    print("")


# In[27]:


query = """INSERT INTO companion_planting(rowid,Sciencetific_name,PLANT,Plant_type,Description,Links,Sowing_Instructions,Space_bet_plants,harvestInstructions,Compatible,Avoid_Instructions,Height,Width,Soil,Maintenance,Aspect,Jan,Feb,Mar,Apr,May,Jun,July,Aug,Sep,Oct,Nov,December) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s)"""


# In[28]:


cursor.execute("""TRUNCATE TABLE companion_planting""")

for i in range(1, len(dlist)):
    rowid = dlist[i][0]
    Sciencetific_name =dlist[i][1] 
    PLANT = dlist[i][2]
    Plant_type = dlist[i][3]
    Description = dlist[i][4]
    Links = dlist[i][5]
    Sowing_Instructions = dlist[i][6]
    Space_bet_plants = dlist[i][7]
    harvestInstructions = dlist[i][8]
    Compatible = dlist[i][9]
    Avoid_Instructions = dlist[i][10]
    Height = dlist[i][11]
    Width = dlist[i][12]
    Soil = dlist[i][13]
    Maintenance = dlist[i][14]
    Aspect = dlist[i][15]
    Jan = dlist[i][16]
    Feb = dlist[i][17]
    Mar = dlist[i][18]
    Apr = dlist[i][19]
    May = dlist[i][20]
    Jun = dlist[i][21]
    July = dlist[i][22]
    Aug = dlist[i][23]
    Sep = dlist[i][24]
    Oct = dlist[i][25]
    Nov = dlist[i][26]
    December = dlist[i][27]

    
    values = (rowid,Sciencetific_name,PLANT,Plant_type,Description,Links,Sowing_Instructions,Space_bet_plants,harvestInstructions,Compatible,Avoid_Instructions,Height,Width,Soil,Maintenance,Aspect,Jan,Feb,Mar,Apr,May,Jun,July,Aug,Sep,Oct,Nov,December)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[29]:


del dlist[0]


# In[30]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

