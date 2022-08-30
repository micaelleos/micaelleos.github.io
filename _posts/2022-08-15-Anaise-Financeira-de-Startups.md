---
layout: post
title:  "Análise Financeira de Startups"
info: "toy project"
tech: "python"
type: Project 
---

O projeto completo pode ser encontrado em: [Análise Financeira de Startups](https://github.com/micaelleos/Portfolio-Data-Science/blob/main/ProfitPrediction/dataanalisys.ipynb)

## Introdução

O lucro obtido por uma empresa, por um determinado período, depende de vários fatores como custos e investimentos em setores administrativos, marketing , pesquisa e desenvolvimento, etc. A tarefa de prever o lucro é importante para a determinação de metas. Essas metas se tornam diretrizes estratégicas para o crescimento contínuo da empresa. Para empresas de rápido crescimento, como startups, conhecer essas previsões torna-se, mais do que importante, essencial para a sobrevivência da empresa.


O banco de dados foi obtido em: [https://raw.githubusercontent.com/amankharwal/Website-data/master/Startups.csv](https://raw.githubusercontent.com/amankharwal/Website-data/master/Startups.csv)

Palavras-chave: *data prediction*, *data modeling*, *Linear Regression*, *Baeysian Regression*, *Clustering*, *K-means*, *Cross-validation*, *Market segmentation*.

## Importação de Bibliotecas

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.metrics import  mean_absolute_error
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import BayesianRidge, LinearRegression
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.cluster import KMeans
warnings.filterwarnings('ignore')
```

## Análise Inicial do Banco de Dados

```python
dados.info()
```
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 50 entries, 0 to 49
    Data columns (total 5 columns):
     #   Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
     0   R&D Spend        50 non-null     float64
     1   Administration   50 non-null     float64
     2   Marketing Spend  50 non-null     float64
     3   State            50 non-null     object 
     4   Profit           50 non-null     float64
    dtypes: float64(4), object(1)
    memory usage: 2.1+ KB
    

O bando de dados não possui nenhum dado nulo.

    As colunas presentes no DtaFrame são:
     Index(['R&D Spend', 'Administration', 'Marketing Spend', 'State', 'Profit'], dtype='object')
    

## Análise Exploratória (EDA)

Quais estados estão presentes no dataset?

    Estados listadas no dataset:['New York' 'California' 'Florida']
    
    Quantidade de empresas por estados listadas no dataset: 
    New York      17
    California    17
    Florida       16
    Name: State, dtype: int64
    

Estatísticas básicas do dataset:


```python
dados.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>R&amp;D Spend</th>
      <th>Administration</th>
      <th>Marketing Spend</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>73721.615600</td>
      <td>121344.639600</td>
      <td>211025.097800</td>
      <td>112012.639200</td>
    </tr>
    <tr>
      <th>std</th>
      <td>45902.256482</td>
      <td>28017.802755</td>
      <td>122290.310726</td>
      <td>40306.180338</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>51283.140000</td>
      <td>0.000000</td>
      <td>14681.400000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>39936.370000</td>
      <td>103730.875000</td>
      <td>129300.132500</td>
      <td>90138.902500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>73051.080000</td>
      <td>122699.795000</td>
      <td>212716.240000</td>
      <td>107978.190000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>101602.800000</td>
      <td>144842.180000</td>
      <td>299469.085000</td>
      <td>139765.977500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>165349.200000</td>
      <td>182645.560000</td>
      <td>471784.100000</td>
      <td>192261.830000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ax = sns.heatmap(dados.corr(),annot=True,cmap='Blues')
ax.figure.set_size_inches(10,5)
ax.set(title="Correlação Entre Variáveis")
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_17_0.png)
    


Todas as variáveis possuem uma correlação direta com o lucro.


```python
sns.pairplot(dados)
```
    
![png](/assets/img/posts/2022-08-15/output_19_1.png)
    


As variáveis de maior influência com o lucro das startups são: 

- R&D Spend (gastos com pesquisa e desenvolvimento)
- Marketing Spend (despesas com marketing)

O maior retorno monetário para as startups são de investimentos em R&D. Os gastos com administração possuem pequena relação com lucro da startup.

Pelo gráfico de correlação, é possível perceber que a relação entre lucro e custos de R&D, nas startups, é quase linear e  bem comportada. Essa relação pode ser vista melhor no gráfico exibido abaixo. Diferentemente dos custos com marketing, que também possui uma alta correlação com o lucro, mas não apresenta um gráfico bem comportado. 


```python
ax = sns.lmplot(x="Profit", y="R&D Spend",data=dados,height=5,scatter_kws={"s": 10, "alpha": 1})
ax.figure.set_size_inches(7,4)
ax.set(title='Relação Lucro X Custos com R&D das Startups',xlabel='Lucro',ylabel='Custo em R&D')
```

![png](/assets/img/posts/2022-08-15/output_21_1.png)
    


## Analisando Lucro por Estado


```python
ax = sns.barplot(data=dados,x='State',y='Profit')
ax.figure.set_size_inches(10,5)
ax.set(title="Distribuição de Lucros por estado",ylabel="Lucro",xlabel='Estado')
```
    
![png](/assets/img/posts/2022-08-15/output_23_1.png)
    


Em média, as startups dos três estados possuem um lucro aproximado.

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>New York</th>
      <th>California</th>
      <th>Florida</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>17.000000</td>
      <td>17.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>113756.446471</td>
      <td>103905.175294</td>
      <td>118774.024375</td>
    </tr>
    <tr>
      <th>std</th>
      <td>41140.258117</td>
      <td>44446.359357</td>
      <td>35605.470428</td>
    </tr>
    <tr>
      <th>min</th>
      <td>35673.410000</td>
      <td>14681.400000</td>
      <td>49490.750000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>96479.510000</td>
      <td>78239.910000</td>
      <td>99147.922500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>108552.040000</td>
      <td>97427.840000</td>
      <td>109543.120000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>129917.040000</td>
      <td>134307.350000</td>
      <td>142719.627500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>192261.830000</td>
      <td>191792.060000</td>
      <td>191050.390000</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig,axs = plt.subplots(1,3, figsize=(15,5))
fig.suptitle('Distribuição de Lucro por Estado')
for i in range(0,3):
    sns.distplot(dados.query(f"State == '{list(dados['State'].unique())[i]}'")["Profit"],bins=10,ax=axs[i])
    axs[i].set(title= list(dados['State'].unique())[i])
```


    
![png](/assets/img/posts/2022-08-15/output_26_0.png)
    


## Detectando Outliers


```python
ax = sns.boxplot(data=dados, x="Profit")
ax.figure.set_size_inches(10,5)
ax.set(title="Distribuição de Lucros",ylabel="Lucro")
```
 
![png](/assets/img/posts/2022-08-15/output_28_1.png)
    

O banco de dados possui poucos candidatos a outliers na variável "Profit".

Medidas separatrizes da variável Lucro:


```python
dados['Profit'].describe()
```




    count        50.000000
    mean     112012.639200
    std       40306.180338
    min       14681.400000
    25%       90138.902500
    50%      107978.190000
    75%      139765.977500
    max      192261.830000
    Name: Profit, dtype: float64



Medidas separatrizes por estado:


```python
ax = sns.boxplot(data=dados, x="State", y="Profit")
ax.figure.set_size_inches(10,5)
ax.set(title="Distribuição de Lucros por Estado",ylabel="Lucro")
```

![png](/assets/img/posts/2022-08-15/output_33_1.png)
    


New York é o estado com maior número de candidatos a outliers, a maior parte das empresas desse estado possui lucro numa faixa bem estabelecida, com pequeno desvio padrão, quando comparado aos outros estados. A Califórnia possui a maior heterogeniedade entre as empresas, quando comparado o lucro.

Por conta da pequena quantidade de dados, e pelo fato de haverem poucos outliers, eles nãos serão retirados do dataset.

## Analisando Gastos por Estado


```python
fig,axs = plt.subplots(1,3, figsize=(20,5))
fig.suptitle('Distribuição de Lucro por Estado')
for i in range(0,3):
    sns.boxplot(data=dados.query(f"State == '{list(dados['State'].unique())[i]}'").iloc[:,:-1],ax=axs[i])
    axs[i].set(title= list(dados['State'].unique())[i],ylim=(-10000,500000))
```


    
![png](/assets/img/posts/2022-08-15/output_36_0.png)
    


O maior valor de custo nas startups, em média, é em Marketing, seguido de custos em sua admnistração e, por fim, em pesquisa de desenvolvimento (R&D).
 
![png](/assets/img/posts/2022-08-15/output_38_1.png)
  

## Modelando o Lucro das Startups

A seguir, é construido um modelo, para prever o lucro das startups com base nos seus gastos.

```python
#Divisão dos conjuntos de teste e treinamento
X = dados.iloc[:,:-1].values
labelenc = LabelEncoder() 
X[:,3] = labelenc.fit_transform(X[:,3])
y = dados.iloc[:,1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 2)
```

    Tamanho do conjunto de treinamento: 37 amostras
    Tamanho do conjunto de teste: 13 amostras
    


```python
# Normalização das variáveis
sc_x = StandardScaler()
X_train,X_test = sc_x.fit_transform(X_train), sc_x.fit_transform(X_test)

sc_y = StandardScaler()
y_train, y_test = sc_y.fit_transform(y_train.reshape(-1, 1)) ,sc_y.fit_transform(y_test.reshape(-1, 1))
```

A seguir, são avaliados dois tipos de regressão linear, para modelagem dos dados. Como o banco de dados é composto por uma pequena quantidade de amostras, os dois modelos serão avaliados por meio da validação cruzada, segundo sua medida de acurácia.

### Regressão Linear por Mínimos Quadrados


```python
lin_reg = LinearRegression()
k=5
lin_reg_scores = cross_val_score(lin_reg, X, y, cv=k)
print('Acurácia média do modelo por correlação cruzada:',(lin_reg_scores.sum()/k)*100)

lin_reg = lin_reg.fit(X_train, y_train)
print('Acurácia do conjunto de treinamento:',lin_reg.score(X_train, y_train))
print('Acurácia do conjunto de teste:',lin_reg.score(X_test, y_test))
```

    Acurácia média do modelo por correlação cruzada: 100.0
    Acurácia do conjunto de treinamento: 1.0
    Acurácia do conjunto de teste: 1.0
    
    
![png](/assets/img/posts/2022-08-15/output_49_0.png)
    


O encaixe do modelos nos dados foi praticamente perfeita, mesmo com o uso da validação cruzada. É muito porvável que tenha ocorrido o overfit dos dados durante o processo de modelagem. Mas isso é compreensivel, uma vez que os dados são bem comportados, e possuirem uma pequena quantidade de amostras. 

### Regressão Linear Bayesiana

    Acurácia média do modelo: 100.0
    Acurácia do conjunto de treinamento: 0.9999999999999999
    Acurácia do conjunto de teste: 0.9999999999999999
    

O modelo de regressão baysiano também se aproximou muito de uma acurácia do último modelo de regressão. O modelo selecionado para a previsão do lucro é a regressão linear por mínimos quadrados.


```python
lucro = lin_reg.predict(X_test)
print('O erro na predição do valor do lucro é de:',mean_absolute_error(y_test,lucro))
```

    O erro na predição do valor do lucro é de: 4.568994755188144e-16
    

## Segmentando Startups por Perfil de Custo

Por meio das informações presentes no baco de dados é possível segmentar as startups em grupos segundo seu perfil de custo. Existem startups que destinam boa parte do seu orçamento para o marketing, outras destinam a maior parte em R&D. A segmentação do banco de dados vai permitir uma análise mais aprofundado com base no perfil de cada uma delas. Essa segmentação por ser feita com métodos de clusterização, e é o que será feito a serguir com um método conhecido como K-means. 

O K-means é um método de clusterização, que procura agrupamentos no espaço de característica da variável. Esse é um método não supervisionado, ou seja, não depende que os dados possuam rótulos. Ele agrupa as amostras de acordo com a sua disposição no espaço. Neste método, é definido a priori a quantidade de grupos que serão formados no espaço. Para definir a quantidade de agrupamentos, será usado o *Elbow Method*.

Como o perfil de custo das startups não depende da sua localização (existem empresas de todos os portes em todos os lugares), a informação sobre a localização de cada uma das empresas não será considerada para definir os agrupamentos pelo K-means, apenas as seguintes variáveis: 'R&D Spend', 'Administration', 'Marketing Spend', 'Profit'.


```python
#normalização dos dados
sc = StandardScaler()
valores = dados.loc[:,['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']].values
dados_cluster = sc.fit_transform(valores) 
```


```python
# aplicação do k-means para diferentes k
clusters=[]
for k in range(1,10):
    kmeans = KMeans(n_clusters=k, random_state=0).fit(dados_cluster)
    clusters.append(kmeans.inertia_)
```


```python
fig, ax = plt.subplots(figsize=(10,5))
plt.title('K-means Elbow Method')
plt.plot(clusters,marker='o')
plt.plot(2,clusters[2],'r.',markersize=15)
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_60_0.png)
    


O joelho da curva se encontra em 3 clusters. Com esse dados em mãos, então as startups podem ser segmentadas de acordo com os clusters encontrados pelo método k-means.


```python
kmeans = KMeans(n_clusters=3, random_state=0).fit(dados_cluster)
```


```python
# Salvando o resultado da segmentação no DataFrame
dados["Segmentation"] = pd.Categorical(kmeans.labels_ )
dados.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>R&amp;D Spend</th>
      <th>Administration</th>
      <th>Marketing Spend</th>
      <th>State</th>
      <th>Profit</th>
      <th>Segmentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>165349.20</td>
      <td>136897.80</td>
      <td>471784.10</td>
      <td>New York</td>
      <td>192261.83</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>162597.70</td>
      <td>151377.59</td>
      <td>443898.53</td>
      <td>California</td>
      <td>191792.06</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>153441.51</td>
      <td>101145.55</td>
      <td>407934.54</td>
      <td>Florida</td>
      <td>191050.39</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>144372.41</td>
      <td>118671.85</td>
      <td>383199.62</td>
      <td>New York</td>
      <td>182901.99</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>142107.34</td>
      <td>91391.77</td>
      <td>366168.42</td>
      <td>Florida</td>
      <td>166187.94</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Vizualização dos cluster de acordo com o lucro
fig = plt.subplots(figsize=(10,5))
plt.title('Relação Lucro X Custos com R&D das Startups por Clusters')
for i in dados['Segmentation'].unique():
    plt.plot(dados.query(f"Segmentation == {i}")['R&D Spend'], dados.query(f"Segmentation == {i}")['Profit'],'o',label='Cluster '+str(i))
plt.legend()
plt.xlabel('Lucro')
plt.ylabel('Custo R&D')
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_64_0.png)
    


### Definindo Perfis de Startups

É possível definir os perfis de startups presentes em cada cluster, observado os valores médios das variáveis no dataset. Abaixo segue medidas estatísticas para a variável lucro em cada cluster.


```python
s0 = dados.query("Segmentation == 0")['Profit'].describe()
s1 = dados.query("Segmentation == 1")['Profit'].describe()
s2 = dados.query("Segmentation == 2")['Profit'].describe()

lucro_estado = pd.DataFrame(data = {"Cluster 0":s0,"Cluster 1":s1,"Cluster 2":s2})
lucro_estado
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cluster 0</th>
      <th>Cluster 1</th>
      <th>Cluster 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>14.000000</td>
      <td>12.000000</td>
      <td>24.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>90351.204286</td>
      <td>73448.101667</td>
      <td>143930.745000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>21626.325437</td>
      <td>27298.191120</td>
      <td>26752.928075</td>
    </tr>
    <tr>
      <th>min</th>
      <td>42559.730000</td>
      <td>14681.400000</td>
      <td>105008.310000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>74996.282500</td>
      <td>65996.555000</td>
      <td>125094.502500</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>97455.700000</td>
      <td>79622.835000</td>
      <td>142922.460000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>102712.945000</td>
      <td>91581.732500</td>
      <td>156339.662500</td>
    </tr>
    <tr>
      <th>max</th>
      <td>122776.860000</td>
      <td>108552.040000</td>
      <td>192261.830000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ax = sns.barplot(data=dados,x='Segmentation',y='Profit')
ax.figure.set_size_inches(10,5)
ax.set(title="Distribuição de Lucros por Cluster",ylabel="Lucro",xlabel='Cluster')
```
    
![png](/assets/img/posts/2022-08-15/output_68_1.png)
    


O cluster 2 possui a maior média de lucro das startups. Os clusters 0 e 1 obtiveram lucros relativamente próximos. Levando em consideração as outras variáveis do dataset, é possível ter um entendimento melhor dos agrupamentos das empresas, como mostrado nos boxplots abaixo.
    
![png](/assets/img/posts/2022-08-15/output_70_0.png)
    


Observando o gráfico, é possível retirar as seguintes conclusões:

- O cluster 0 é composto por empresas que possuem a segunda menor faixa de lucro, ganhando apenas do cluster 1. Apesar disso, são as empresas que possuem os maiores custos com admninstração, e menores custos com R&D e Marketing.  
- O cluster 1 é composto por empresas que possuem um alto custo com Marketing, quando comparados aos seus outros custos. Por esse motivo, esse cluster possui o segundo maior lucro.
- Já o cluster 2, é composto por empresa que possuem os maiores custos com R&D de todas as startups, juntamente com os custos com Markting. Esse combo de investimento faz com que sejam as startups mais lucrativas.


A distribuição dos três grupos de startups pelos estados do banco de dados pode ser vista no gráfico abaixo.


```python
fig = plt.subplots(figsize=(10,5))
plt.bar(np.arange(0,3),dados.query('Segmentation == 0')['State'].value_counts().values, width=0.2,label='Cluster 0')
plt.bar(np.arange(0,3)+0.2,dados.query('Segmentation == 1')['State'].value_counts().values, width=0.2,label='Cluster 1')
plt.bar(np.arange(0,3)+0.2*2,dados.query('Segmentation == 2')['State'].value_counts().values, width=0.2,label='Cluster 2')
plt.xticks(np.arange(0,3)+0.2,['New York','California','Florida'])
plt.legend()
plt.title('Distribuição dos Clusters por Estado')
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_72_0.png)
    


O que aconteceria se as as empresas do cluster 0 reduzissem em 10% o custo com administração e investissem esse dinheiro nos seus setores de R&D? Vamos descobrir isso no estudo de caso apresentado a seguir. 

## Estudo de Caso

Para as empresas dos clusters 0 e 1, que foram os grupos de empresas com menores faixas de lucro, vamos fazer a seguinte simulação :

1) Reduzir em 10% seus custos com administração;
2) Investir esse dinheiro em pesquisa e desenvolvimento;
3) Observar o impacto dessa redistribuição de custos no lucro médio das empresas desses grupos.

#### Reajuste de Custo do Cluster 0


```python
# Selecionando dados das startups do cluster 0
startups_c0 = dados.query('Segmentation == 0')
startups_c0.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>R&amp;D Spend</th>
      <th>Administration</th>
      <th>Marketing Spend</th>
      <th>State</th>
      <th>Profit</th>
      <th>Segmentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19</th>
      <td>86419.70</td>
      <td>153514.11</td>
      <td>0.00</td>
      <td>New York</td>
      <td>122776.86</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>64664.71</td>
      <td>139553.16</td>
      <td>137962.62</td>
      <td>California</td>
      <td>107404.34</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>75328.87</td>
      <td>144135.98</td>
      <td>134050.07</td>
      <td>Florida</td>
      <td>105733.54</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>66051.52</td>
      <td>182645.56</td>
      <td>118148.20</td>
      <td>Florida</td>
      <td>103282.38</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>65605.48</td>
      <td>153032.06</td>
      <td>107138.38</td>
      <td>New York</td>
      <td>101004.64</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Criando um novo DataFram com os ajustes de custo: redução de 10% com gastos com AMD e aumento desse valor em R&D
startups_c0_new = startups_c0.copy()
startups_c0_new['R&D Spend'] = startups_c0['R&D Spend'] + startups_c0['Administration']*0.1
startups_c0_new['Administration'] = startups_c0['Administration']*0.9
```

Com as modificações feitas, pode-se fazer a projeção de lucro, com base no modelo desenvolvido na seção [Modelando o Lucro das Startups](#Modelando-o-Lucro-das-Startups):


```python
X = startups_c0_new.iloc[:,:-2].values
X[:,3] = labelenc.fit_transform(X[:,3])
x = sc_x.fit_transform(X)
startups_c0['Profit'] = sc_y.inverse_transform(lin_reg.predict(x))
```

Qual foi a porcentagem de aumento do lucro com o reinvestimeto do custo?


```python
print('A porcentagem do aumento do lucro foi de:',round((1-startups_c0_new['Profit'].mean()/startups_c0['Profit'].mean())*100,2),'%')
```

    A porcentagem do aumento do lucro foi de: 25.74 %
    


```python
fig = plt.subplots(figsize=(5,5))
plt.bar(0,startups_c0_new['Profit'].mean(), width=0.2,label='Sem Ajuste')
plt.bar(0.3,startups_c0['Profit'].mean(), width=0.2,label='Com Ajuste')
plt.xticks([0,0.3],['Sem','Com'])
plt.legend()
plt.title('Lucro Médio das Startups do Cluster 0, Sem e Com Ajuste de Custos')
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_83_0.png)
    


#### Reajuste de Custos Cluster 1


```python
# Selecionando dados das startups do cluster 1
startups_c1 = dados.query('Segmentation == 1')
startups_c1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>R&amp;D Spend</th>
      <th>Administration</th>
      <th>Marketing Spend</th>
      <th>State</th>
      <th>Profit</th>
      <th>Segmentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>77044.01</td>
      <td>99281.34</td>
      <td>140574.81</td>
      <td>New York</td>
      <td>108552.04</td>
      <td>1</td>
    </tr>
    <tr>
      <th>33</th>
      <td>55493.95</td>
      <td>103057.49</td>
      <td>214634.81</td>
      <td>Florida</td>
      <td>96778.92</td>
      <td>1</td>
    </tr>
    <tr>
      <th>35</th>
      <td>46014.02</td>
      <td>85047.44</td>
      <td>205517.64</td>
      <td>New York</td>
      <td>96479.51</td>
      <td>1</td>
    </tr>
    <tr>
      <th>37</th>
      <td>44069.95</td>
      <td>51283.14</td>
      <td>197029.42</td>
      <td>California</td>
      <td>89949.14</td>
      <td>1</td>
    </tr>
    <tr>
      <th>38</th>
      <td>20229.59</td>
      <td>65947.93</td>
      <td>185265.10</td>
      <td>New York</td>
      <td>81229.06</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Criando um novo DataFram com os ajustes de custo: redução de 10% com gastos com AMD e aumento desse valor em R&D
startups_c1_new = startups_c1.copy()
startups_c1_new['R&D Spend'] = startups_c1['R&D Spend'] + startups_c1['Administration']*0.1
startups_c1_new['Administration'] = startups_c1['Administration']*0.9
```


```python
X = startups_c1_new.iloc[:,:-2].values
X[:,3] = labelenc.fit_transform(X[:,3])
x = sc_x.fit_transform(X)
startups_c1['Profit'] = sc_y.inverse_transform(lin_reg.predict(x))
```

Qual foi a porcentagem de aumento do lucro com o reinvestimeto do custo?


```python
print('A porcentagem do aumento do lucro foi de:',round((1-startups_c1_new['Profit'].mean()/startups_c1['Profit'].mean())*100,2),'%')
```

    A porcentagem do aumento do lucro foi de: 39.63 %
    


```python
fig = plt.subplots(figsize=(5,5))
plt.bar(0,startups_c1_new['Profit'].mean(), width=0.2,label='Sem Ajuste')
plt.bar(0.3,startups_c1['Profit'].mean(), width=0.2,label='Com Ajuste')
plt.xticks([0,0.3],['Sem','Com'])
plt.legend()
plt.title('Lucro Médio das Startups do Cluster 1, Sem e Com Ajuste de Custos')
plt.show()
```


    
![png](/assets/img/posts/2022-08-15/output_90_0.png)
    


## Conclusão

- Os gastos com administração possuem pequena relação com lucro da startup.

- As variáveis de maior influência com o lucro das startups são: R&D Spend e Marketing Spend 

- O maior retorno monetário para as startups são de investimentos em R&D. 

- Em média, as startups dos três estados possuem um lucro aproximado.

- O maior valor de custo nas startups, em média, é em Marketing, seguido de custos em sua admnistração e, por fim, em pesquisa de desenvolvimento (R&D).
- As startups podem segmentadas em três grupos, com os seguintes perfis: 
    - O cluster 0 é composto por empresas que possuem a segunda menor faixa de lucro e maiores custos com admninstração. Também possuem menores custos com R&D e Marketing. São as empresas com maior potêncial de aumento de lucro com ajuste de custos. 
    - O cluster 1 é composto por empresas que possuem um alto custo com Marketing e possui o menor lucro dos três grupos.
    - O cluster 2, é composto por empresa que possuem os maiores custos com R&D. São as startups mais lucrativas.

- Existem startups dos três perfis em todos os estados.
- Estudo de Caso: Se as empresas do cluster 0 reduzissem em 10% o custo com administração, e investissem esse dinheiro nos seus setores de R&D, aumentariam em 25% seu lucro. De forma semelhante, se as empresas do cluster 1 reduzissem em 10% o custo com administração, e investissem esse dinheiro nos seus setores de R&D, aumentariam em 49.63% seu lucro.
