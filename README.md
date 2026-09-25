# Análise de Oportunidades para Investidores Imobiliários em Maricá/RJ
# Portfólio de Dados - Caio Gonçalves

Projetos desenvolvidos durante minha transição da Engenharia Civil para a área de Dados.

Tecnologias:
- SQL
- Power BI
- Python
- Git

# Identificação e Correção de Anomalia nos Dados (Data Quality)
O Cenário: Durante a fase de Análise Exploratória de Dados (EDA) e validação das métricas, foi detetada uma discrepância crítica no KPI de Valor Médio do Metro Quadrado (R$/m²), que apresentava valores muito abaixo do praticado no mercado imobiliário da região.

O Diagnóstico: Ao aplicar o conhecimento de negócio e engenharia civil para inspecionar os dados brutos (ex: imóvel ID JA1574), identifiquei um erro de escala na base de origem. As colunas AREA_TERRENO e AREA_CONSTRUIDA estavam com os valores multiplicados por 10 (ex: uma casa de 120m² estava registada como 1200m²).

A Solução Aplicada:
Em vez de corrigir manualmente na folha de cálculo, implementei uma regra de tratamento diretamente no pipeline de ETL em Python (Pandas) para garantir a reprodutibilidade. A transformação divide os vetores de área por 10 antes da criação das métricas financeiras calculadas:

Tratamento no pipeline ETL para correção de escala

df['AREA_TERRENO'] = df['AREA_TERRENO'] / 10

df['AREA_CONSTRUIDA'] = df['AREA_CONSTRUIDA'] / 10

Impacto: A correção reestabeleceu a precisão matemática do painel, permitindo que os investidores simulem o VGV e a rentabilidade com base em dados fidedignos.
