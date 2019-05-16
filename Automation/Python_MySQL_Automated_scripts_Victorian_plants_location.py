
# coding: utf-8

# In[23]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[24]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[25]:


cursor = conn.cursor()


# In[29]:


dlist = []
with open("Victoria_plants.csv", encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[30]:


query = """INSERT INTO vic_plants_locations(Scientific_Name_Original,Common_name,Scientific_Name,Latitude,Longitude,rowid) VALUES (%s, %s, %s, %s,%s, %s)"""


# In[31]:


cursor.execute("""TRUNCATE TABLE vic_plants_locations""")

for i in range(1, len(dlist)):
    Scientific_Name_Original = dlist[i][0]
    Common_name = dlist[i][1]
    Scientific_Name = dlist[i][2]
    Latitude = dlist[i][3]
    Longitude = dlist[i][4]
    rowid = dlist[i][5]
    
    values = (Scientific_Name_Original,Common_name,Scientific_Name,Latitude,Longitude,rowid)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[32]:


del dlist[0]


# In[33]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

