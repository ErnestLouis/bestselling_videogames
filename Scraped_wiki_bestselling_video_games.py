#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


#pandas package
import pandas as pd


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

# provides a response object of hopefullly 200
page = requests.get(url)

#page.text pulls info from url, html is the parser
soup = BeautifulSoup(page.text, 'html')


# In[4]:


print(soup)


# In[5]:


#retrieving the best-selling video game table using class name

table = soup.find('table', class_ = 'wikitable plainrowheaders sortable')


# In[6]:


print(table)


# In[7]:


#Retrieving all the table headers

game_titles = table.find_all('th')

game_titles


# In[10]:


#looping through game titles while cleaning data

game_table_titles = [title.text.strip() for title in game_titles[:7]]

print(game_table_titles)


# In[11]:


#remove [b] from string

game_table_titles[5] = game_table_titles[5].replace("[b]", "")
game_table_titles[6] = game_table_titles[6].replace("[b]", "")
print(game_table_titles)


# In[12]:


#this pulls the data (extract) titles and places it in the dataframe
df = pd.DataFrame(columns = game_table_titles)

df


# In[22]:


column_data = table.find_all('tr')

column_data


# In[26]:


#this loops through the data in each row,places each row data in a list, prints the individual row data
#looping through tr, column_data
#for row in column_data: to start on second row ignoring the empty first row
    #as we are looping through tr we are looking for td tags
    #for each of the data found we are taking out the text and striping it to clean that data
    #loc is location
    #this looks at the length of our current data frame
    #each row of that information placed into the next position


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data[:7]]
    length = len(df)
    df.loc[length] = individual_row_data


# In[24]:


print(individual_row_data)


# In[27]:


print(length)


# In[28]:


#to export df to csv file ignoring index

df.to_csv(r'C:\Users\Ernest\Documents\csv_exports\wiki_bestselling_video_games.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




