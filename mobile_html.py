from csv import excel
from dataclasses import replace

import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

with open('mobiles.html','r',encoding='utf-8') as f:
    html_file = f.read()

soup = BeautifulSoup(html_file,'lxml')
phones = soup.find_all('div',class_='finder_snipet_wrap')

final = pd.DataFrame()
name = []
prices = []
battery = []
processor = []
processor2 = []
processor3 = []
display = []
camera = []
os = []
phone_score = []
over_all_comment = []

for i in phones:
  try:
    name.append(i.find('a',class_ = 'hover_blue_link name gaclick').text.strip())
  except:
    name.append(np.nan)
  try:
    prices.append(i.find('span',class_ = ['price price_padding','price price_float']).text.strip())
  except:
    prices.append(np.nan)
  try:
    b = i.find_all('div',class_ = 'a filter-list-text')[3]
    b_labels = b.find_all('label')
    b_text = ','.join(label.get_text(strip=True) for label in b_labels)
    battery.append(b_text)
  except:
    battery.append(np.nan)

  # df1 = i.find_all('div',class_ = 'a filter-list-text')[3]
  # df = df1.find_all('label')[0].text
  try:
    a = i.find_all('div', class_='a filter-list-text')[0]
    labels = a.find_all('label')
    text = ','.join(label.get_text(strip=True) for label in labels)
    processor.append(text)
  except:
    processor.append(np.nan)

  try:
    c = i.find_all('div',class_ = 'a filter-list-text')[1]
    d_label = c.find_all('label')
    d_text = ','.join(label.get_text(strip=True).replace(',','') for label in d_label)
    display.append(d_text)
  except:
    display.append(np.nan)
  try:
    d = i.find_all('div',class_ = 'a filter-list-text')[2]
    c_label = d.find_all('label')
    c_text = ','.join(label.get_text(strip=True) for label in c_label)
    camera.append(c_text)
  except:
    camera.append(np.nan)

  try:
    phone_score.append(i.find('div',class_ = ['rating_box_new_list spec_score_translated best_in_class','rating_box_new_list spec_score_translated excellent','rating_box_new_list spec_score_translated verygood']).text.strip())
  except:
    phone_score.append(np.nan)
  try:
      os.append(i.find('div',class_ = 'os_icon_cat').text.strip())
  except:
      os.append((np.nan))
  try:
      over_all_comment.append(i.find('div',class_ = 'featuretext').text.strip())
  except:
      over_all_comment.append((np.nan))


# print(card)
df = pd.DataFrame(
    {'Phone_Name': name, 'Price': prices, 'Battery_Info': battery, 'Processor_Info': processor, 'Display_Info': display,
     'Camera_Info': camera, 'OS_Info': os, 'Phone_Score':phone_score, 'Over_All_Comment':over_all_comment})

final = pd.concat([final, df], ignore_index=True)

final.to_csv('performance_Mobile_Dataset.csv',index=False,encoding='utf-8')