import pandas as pd
import numpy as np

# 1. Carregar os dados (usando separador ponto e vírgula)
df = pd.read_csv('imoveis.csv', sep=';')

# 2. Corrigir nomes das colunas (removendo espaços em branco extras)
df.columns = df.columns.str.strip()

# 3. Tratamento de Nulos e Textos em colunas numéricas
# Substituir "NÃO SE APLICA" por 0 em Quartos e Suítes
df['QUARTOS'] = df['QUARTOS'].replace('NÃO SE APLICA', 0)
df['SUITE'] = df['SUITE'].replace('NÃO SE APLICA', 0)

# Substituir os bairros "INOÃ" por "CHACARAS DE INOÃ" erro muito comum.
df['BAIRRO'] = df['BAIRRO'].replace('INOÃ', 'CHACARAS DE INOÃ')

# Preencher os 6 nulos da coluna SUITE com 0
df['SUITE'] = df['SUITE'].fillna(0)

# Converter essas colunas para números inteiros
df['QUARTOS'] = df['QUARTOS'].astype(int)
df['SUITE'] = df['SUITE'].astype(int)

# 4. Engenharia de Recursos e Correção de Anomalias

# Criando a Métrica Rainha do Investidor (Agora com as áreas corrigidas)
# Só calculamos o Valor do Metro Quadrado onde a Área Construída é maior que zero para evitar erro de divisão
df['VALOR_M2'] = np.where(df['AREA_CONSTRUIDA'] > 0, df['VALOR'] / df['AREA_CONSTRUIDA'], 0)

# 5. Modelagem de Dados (Criando as tabelas Dimensão e Fato)

# Tabela Dimensão: Localização
dim_localizacao = df[['CIDADE', 'DISTRITO', 'BAIRRO']].drop_duplicates().reset_index(drop=True)
dim_localizacao['ID_LOCALIZACAO'] = dim_localizacao.index + 1

# Fazendo o merge (PROCV) para trazer o ID para a tabela principal
df = df.merge(dim_localizacao, on=['CIDADE', 'DISTRITO', 'BAIRRO'], how='left')

# Tabela Fato: Imóveis/Ofertas
fato_ofertas = df[['CODIGO', 'ATIVO', 'TIPO', 'ID_LOCALIZACAO', 'QUARTOS', 'SUITE', 
                   'AREA_TERRENO', 'AREA_CONSTRUIDA', 'VALOR', 'VALOR_M2', 
                   'PISCINA_IMOVEL', 'CHURRASQUEIRA', 'CONDOMINIO', 'ALTO_PADRAO', 'STATUS']]

# 6. Exportar os dados limpos COM PADRÃO BRASILEIRO (Isso resolve o bug do Power BI)
dim_localizacao.to_csv('dim_localizacao.csv', index=False, sep=';', decimal=',')
fato_ofertas.to_csv('fato_ofertas.csv', index=False, sep=';', decimal=',')

print("Dados limpos e modelados com sucesso! Prontos para o Power BI.")
