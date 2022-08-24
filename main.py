import pandas as pd

df = pd.read_csv("Alunos.csv")
print(df)

df['média'] = (df['nota_1'] + df['nota_2']) / 2
df['situação'] = 0

df.loc[df['média'] >= 7, 'situação'] = 'Aprovado'
df.loc[df['média'] < 7, 'situação'] = 'Reprovado'
df.loc[df['faltas'] > 5, 'situação'] = 'Reprovado'

media = df['média'].median()
faltas = df['faltas'].max()
maiorMedia = df['média'].max()

print(df)
print('A média geral dos alunos: '+str(media))
print('O maior número de faltas: '+str(faltas))
print('A maior média: '+str(maiorMedia))

#df.to_csv('alunos_situação.csv')