import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


#df= pd.read_csv(se for outro tipo de planilha altera("nome da planilha com os dados", sep"separação", decimal )
df= pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df=df.sort_values("Date")

#Com uma visão mensal

df["Month"] = df["Date"].apply(lambda x: str(x.year)+"-"+ str(x,month).zfill(2))
month = st.sidebar.selectbox("Mês",df["Month"].unique())

#Filtro do pandas para meses e anos
df_filtered = df[df["Month"] == month]

#Caixas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

#Graficos

#Grafico de faturamento por dia pelo mês selecionado e por filial 
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date)

# Grafico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Product line", y="Total", color="City", title="Faturamento por produto",
                  orientation="h")
col2.plotly_chart(fig_prod)

# Grafico de contribuição por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="total", title="Faturamento por filial",
                  orientation="v")
col3.plotly_chart(fig_city)

# Grafico de faturamento por tipo de pagamento

fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind)

#Avaliação media por cidade
city_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_rating, x="city", y="Rating",
                  title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)





