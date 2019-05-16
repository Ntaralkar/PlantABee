
# coding: utf-8

# In[3]:


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pymysql
import MySQLdb
import csv


# In[4]:


conn = MySQLdb.connect(host='www.plantabee.tk',
                             user='root',
                             password='Plantabee@monash',
                             db='plantabee')


# In[5]:


cursor = conn.cursor()


# In[6]:


dlist = []
with open("Incompatible_plants.csv", encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        dlist.append(row)


# In[8]:


query = """INSERT INTO Incompatible_plants(rowid, Botanical_name, Common_name, Incompatible_plants) VALUES (%s, %s, %s, %s)"""


# In[9]:


cursor.execute("""TRUNCATE TABLE Incompatible_plants""")

for i in range(1, len(dlist)):
    id = dlist[i][0]
    Botanical_name = dlist[i][1]
    Common_name = dlist[i][2]
    Incompatible_plants = dlist[i][3]
    
    values = (id, Botanical_name, Common_name, Incompatible_plants)
    
    cursor.execute(query, values)
    
cursor.close()

conn.commit()


# In[10]:


del dlist[0]


# In[11]:


print("Total" + " " + str(len(dlist[0])) + " columns and " + str(len(dlist))+ " rows were imported successfully")

