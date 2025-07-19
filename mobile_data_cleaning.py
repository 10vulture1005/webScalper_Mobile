import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

df = pd.read_csv('/content/Mobiel_Dataset.csv')

#1 Filling Missing Value With Zero in Price
df['Price'] = df['Price'].fillna(0)
df[df['Price'].isna()]

#2 Replace Rs and ","
df['Price']=df['Price'].str.replace(",","").str.replace("Rs.",'')

#3 Coverting Price To Int
df['Price'] = df['Price'].astype(int)

#4 Adding Index so easier to iterate.
df['Index'] = df.index

#5 Fixing Values
#5a
df.loc[df['Index']==48,'Battery_Info'] = df.loc[df['Index']==48,'Camera_Info']
df.loc[df['Index']==48,'Camera_Info'] = np.nan
#5b
df.loc[df['Index']==83,'Battery_Info'] = df.loc[df['Index']==83,'Camera_Info']
df.loc[df['Index']==83,'Camera_Info'] = np.nan
#5c
df.loc[df['Index']==130,'Battery_Info'] = df.loc[df['Index']==130,'Display_Info']
df.loc[df['Index']==130,'Display_Info'] = np.nan
#5d
df.loc[df['Index']==270,'Battery_Info'] = df.loc[df['Index']==270,'Display_Info']
df.loc[df['Index']==270,'Display_Info'] = np.nan
#6 Still one NaN left so fillinf it with some value.
df['Battery_Info'] = df['Battery_Info'].fillna('No Info Available')

#7 Moving Camera Info From Display Column To Camera Column
df.loc[df['Index']==83,'Camera_Info'] = df.loc[df['Index']==83,'Display_Info']
df.loc[df['Index']==83,'Display_Info'] = np.nan

#8 Replacing Display Info Which Is In Processor To Actual Display Column
df.loc[df['Index']==83,'Display_Info'] = df.loc[df['Index']==83,'Processor_Info']
df.loc[df['Index']==83,'Processor_Info'] = np.nan

df.loc[df['Index']==130,'Display_Info'] = df.loc[df['Index']==130,'Processor_Info']
df.loc[df['Index']==130,'Processor_Info'] = np.nan

df.loc[df['Index']==270,'Display_Info'] = df.loc[df['Index']==270,'Processor_Info']
df.loc[df['Index']==270,'Processor_Info'] = np.nan

df.loc[df['Index']==146,'Display_Info'] = df.loc[df['Index']==146,'Processor_Info']
df.loc[df['Index']==146,'Processor_Info'] = np.nan

#9 Filling NaN to No Info Avaiable
df['Processor_Info'] = df['Processor_Info'].fillna('No Info Available')

#10 Filling NaN to No Info Available
df['Camera_Info'] = df['Camera_Info'].fillna('No Info Available')

#11 Fillinf NaN values
df['OS_Info'] = df['OS_Info'].fillna('No Info Available')

#12 Adding New Column to Check OS Upgradable Or Not
df['Upgradable'] = df['OS_Info'].apply(lambda row : 'Yes' if 'upgrad' in row.lower() else 'No')

#13 Filling NaN in Score With 0 and replacing % to '' and conveting to integer.
df['Phone_Score'] = df['Phone_Score'].str.replace('%','')
df['Phone_Score'] = df['Phone_Score'].fillna(0)
df['Phone_Score'] = df['Phone_Score'].astype(int)

#14 Converint NaN to No Comment and " to ''
df['Over_All_Comment'] = df['Over_All_Comment'].str.replace('"','')
df['Over_All_Comment'] = df['Over_All_Comment'].fillna('No Info Available')

#15 Splitting Battery Column
battery_parts = df['Battery_Info'].str.split(',', expand=True)
df['Battery_Size'] = battery_parts[0]
df['Charging_Spee'] = battery_parts[1]
df['USB_Type'] = battery_parts[2]
df.drop(columns = 'Battery_Info',inplace=True)

#16 Splitting Display Column
Processor_parts = df['Display_Info'].str.split(',', expand=True)
df['Display_Size'] = Processor_parts[0]
df['Display_Quality'] = Processor_parts[1]
df['Display_Speed'] = Processor_parts[2]
df.drop(columns = 'Display_Info',inplace=True)

#17 Splitting Camera Column
Camera_parts = df['Camera_Info'].str.split(',', expand=True)
df['Back_Camera'] = Camera_parts[0]
df['LED_Detail'] = Camera_parts[1]
df['Front_Camera'] = Camera_parts[2]
df.drop(columns = 'Camera_Info',inplace=True)

df.to_csv('Cleaned_Mobile_Dataset.csv')

