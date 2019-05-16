
# coding: utf-8

# In[82]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[83]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[84]:


cursor = conn.cursor()


# In[89]:


dlist = []
with open("flowering_season.csv", encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[90]:


query = """INSERT INTO flowering_season(rowid, Botanical_name, Flowering_Time) VALUES (%s, %s, %s)"""


# In[91]:


cursor.execute("""TRUNCATE TABLE flowering_season""")

for i in range(1, len(dlist)):
    id = dlist[i][0]
    Botanical_name = dlist[i][1]
    Flowering_Time = dlist[i][2]
    
    values = (id, Botanical_name, Flowering_Time)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[93]:


del dlist[0]


# In[94]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

