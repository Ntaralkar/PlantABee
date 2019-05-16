
# coding: utf-8

# In[1]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[2]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[3]:


cursor = conn.cursor()


# In[4]:


dlist = []
with open("compatible_plants.csv", encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[14]:


query = """INSERT INTO compatible_plants(rowid, Botanical_name, Common_name, Compatible_plants) VALUES (%s, %s, %s, %s)"""


# In[15]:


cursor.execute("""TRUNCATE TABLE compatible_plants""")

for i in range(1, len(dlist)):
    id = dlist[i][0]
    Botanical_name = dlist[i][1]
    Common_name = dlist[i][2]
    Compatible_plants = dlist[i][3]
    
    values = (id, Botanical_name, Common_name, Compatible_plants)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[16]:


del dlist[0]


# In[17]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

