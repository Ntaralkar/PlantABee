
# coding: utf-8

# In[2]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[3]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[4]:


cursor = conn.cursor()


# In[5]:


dlist = []
with open("Beeplants_final_data.csv", encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[17]:


query = """INSERT INTO bee_friendly_plants(rowid,Botanical_name,Common_name,Plant_type,Height,Width,Flower_colour,Flowering_Time,Pollinator,Information,Uses,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,December,Climate,Rainfall,Aspect,Soil) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"""


# In[18]:


cursor.execute("""TRUNCATE TABLE bee_friendly_plants""")

for i in range(1, len(dlist)):
    rowid = dlist[i][0]
    Botanical_name = dlist[i][1]
    Common_name = dlist[i][2]
    Plant_type = dlist[i][3]
    Height = dlist[i][4]
    Width = dlist[i][5]
    Flower_colour = dlist[i][6]
    Flowering_Time = dlist[i][7]
    Pollinator = dlist[i][8]
    Information = dlist[i][9]
    Uses = dlist[i][10]
    Jan = dlist[i][11]
    Feb = dlist[i][12]
    Mar = dlist[i][13]
    Apr = dlist[i][14]
    May = dlist[i][15]
    Jun = dlist[i][16]
    Jul = dlist[i][17]
    Aug = dlist[i][18]
    Sep = dlist[i][19]
    Oct = dlist[i][20]
    Nov = dlist[i][21]
    December = dlist[i][22]
    Climate = dlist[i][23]
    Rainfall = dlist[i][24]
    Aspect = dlist[i][25]
    Soil = dlist[i][26]
    
    values = (rowid,Botanical_name,Common_name,Plant_type,Height,Width,Flower_colour,Flowering_Time,Pollinator,Information,Uses,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,December,Climate,Rainfall,Aspect,Soil)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[19]:


del dlist[0]


# In[20]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

