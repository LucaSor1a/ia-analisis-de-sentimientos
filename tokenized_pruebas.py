import os
from dotenv import load_dotenv
import pandas as pd
import requests

pd.options.display.max_rows = 40
pd.options.display.max_seq_items = 20

df = pd.read_csv("TechTweets1.csv") #para no volver a pedir los datos
#print("Leer Datos")
#print(df)

df = df[['text']]
#print("\n\nLeer Datos  de text ")
#print(df)
df2 = df
df = df2

from nltk.tokenize import TweetTokenizer
# Instanciar Tokenizer
tt = TweetTokenizer()
# Aplicar Tokenizer a la columna
tokenized_text = df['text'].apply(tt.tokenize)
df["tokenized_text"] = tokenized_text

tokenized_list = df.explode('tokenized_text')

print("Ver lista tokenizada")

#print(tokenized_list['tokenized_text'])


tokenized_list_text = tokenized_list['tokenized_text']

tokenized_list_text_min = list(map(str.lower,tokenized_list_text))



caracteres_a_eliminar = ("#","@","!","’",",",";",".",":","+","/","*","'","?","¿","¡","!","|","ª","/","~","¬","%","&","(",")","=","-","...",'…',"_")


for i in caracteres_a_eliminar:    
    if i in tokenized_list_text_min:
        tokenized_list_text_min = list(filter(lambda val: val !=  i, tokenized_list_text_min))

#print(tokenized_list_text_min)


for j in range(2):
    for i in tokenized_list_text_min:
        if ("http" in i) or ("t.co" in i) or ("https://t.co/" in i):             
            tokenized_list_text_min.remove(i)

print(len(tokenized_list_text_min))