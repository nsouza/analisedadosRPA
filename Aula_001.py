# %% 📦 Imports
import pandas as opcoesPandas
import numpy as opcoesNumpy

# %%
dataFrame_Datas = opcoesPandas.date_range("20221201",periods=31)


# %%
print(dataFrame_Datas)


# %%

dataFrame_Meses = opcoesPandas.date_range("20221201",periods=12,freq="ME")
print(dataFrame_Meses)
# %%
numerosAleatorios = opcoesPandas.DataFrame(opcoesNumpy.random.rand(5,10)*100)
print(numerosAleatorios)
# %%
notasAlunos_DF = opcoesPandas.DataFrame({
    "Alunos": ["João", "Maria", "Pedro", "Ana", "Lucas"],
    "Matemática": [8.5, 9.0, 7.5, 6.0, 9.5],
    "Português": [7.0, 8.5, 6.0, 9.0, 8.0],
    "Ciências": [9.0, 7.5, 8.0, 6.5, 7.0]
})

print(notasAlunos_DF)
# %%
