#!/usr/bin/env python
# coding: utf-8

# In[8]:


import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


# In[39]:


# scope of the application
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "cred.json", scope)


# In[40]:


client = gspread.authorize(credentials)
# Open the spreadhseet
sheet = client.open("Interface_data").worksheet("Sheet1")


# In[41]:


# Get a list of all records
data = sheet.get_all_records()
# pprint(data)


# In[42]:


import streamlit as st


# In[43]:


st.title("Try Appending")


# In[44]:


t1 = st.text_input("Input 1", key = 1)
t2 = st.text_input("Input 2", key = 2)
t3 = st.text_input("Input 3", key = 3)
t4 = st.text_input("Input 4", key = 4)
t5 = st.text_input("Input 5", key = 5)
t6 = st.text_input("Input 6", key = 6)


# In[45]:


if st.button("Append GSheet",key=7):
    l = []
    l.append(t1)
    l.append(t2)
    l.append(t3)
    l.append(t4)
    l.append(t5)
    l.append(t6)
    sheet.insert_row(l,len(sheet.get_all_records()))
    st.write("Check Sheet!")

