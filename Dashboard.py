import pandas as pd
import plotly.express as px

#def grafico():
    

    #Selecionando o arquivo
tab_df = pd.read_excel("tabela.ods")
df = px.data.tips

    #seleçao de coluna
Data_df = tab_df["Data"]
instagram_df = tab_df["Instagram"]
tiktok_df = tab_df["tiktok"]
trabalhando_df = tab_df["trabalhando"]
Total_df = tab_df["Total"]

seletor = Total_df
#-------

#grafico
fig_graf = px.bar (tab_df, x = Data_df, y= seletor)
Data_df = px.data.medals_long()


mostra = fig_graf.show (), 

#-------




