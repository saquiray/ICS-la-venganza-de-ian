from sklearn import datasets
import pandas as pd

digits = datasets.load_digits()

separador = pd.DataFrame(data=[[0,0,0,0,0,0,0,0]])
df_final=pd.DataFrame(data=[])
i = 0
while (i<1796):
    df1 = pd.DataFrame(data=digits["images"][i])
    df2 = pd.DataFrame(data=digits["images"][i+1])
    df_final=pd.concat([df_final,df1],ignore_index=True)
    df_final = pd.concat([df_final,separador], ignore_index=True)
    df_final = pd.concat([df_final,df2], ignore_index=True)
    df_final = pd.concat([df_final, separador], ignore_index=True)
    i=i+2
df2 = pd.DataFrame(data=digits["images"][1796])
df_final = pd.concat([df_final,df2], ignore_index=True)
df_final = pd.concat([df_final, separador], ignore_index=True)


#Generar una lista con 9 veces cada target
miLista=[]
i = 0
while(i<1797):
    j = 0
    while(j<9):
        miLista.append(digits["target"][i])
        j=j+1
    i=i+1


df_final["el número"] = miLista
print(df_final)
df_final.to_csv("base_de_datos_digits.csv")


