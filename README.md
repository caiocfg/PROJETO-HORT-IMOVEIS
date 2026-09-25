# Análise de KPIs para Investidores Imobiliários em Maricá/RJ
Bem-vindo ao repositório deste projeto de Análise de Dados focado no mercado imobiliário de Maricá/RJ.

Objetivo: Transformar dados brutos de cadastros de imóveis em ferramentas para tomada de decisão. Este projeto foi desenvolvido para guiar a tomada de decisão baseada em dados de investidores e construtores que buscam comprar terrenos e construir casas para venda/aluguel.

Através da exploração e estruturação dos dados locais, o projeto mapeia o comportamento do mercado e expõe KPIs estratégicos, respondendo a perguntas fundamentais para o sucesso do investimento com indicadores como:

Preço médio de venda de acordo com a localização e características da propriedade.

Configuração ideal para liquidez: cruzamento de dados sobre a quantidade de quartos e metragem quadrada que mais atraem compradores.

Impacto de comodidades: como a presença de piscinas ou a localização em condomínio fechado influenciam no valor final e na velocidade de venda.

Taxa de conversão/absorção: análise comparativa entre imóveis vendidos e disponíveis.

Aliando visão analítica e conhecimento prático do setor de construção civil, este projeto traduz números em diretrizes claras para maximizar o retorno sobre o investimento (ROI).

Tecnologias: Excel, SQL, Power BI e Python

# Registro de Alterações - Histórico de ocorrências

### Identificação e Correção de Anomalia nos Dados (Data Quality)
O Cenário: Durante a fase de Análise Exploratória de Dados (EDA) e validação das métricas, foi detetada uma discrepância crítica no KPI de Valor Médio do Metro Quadrado (R$/m²), que apresentava valores muito abaixo do praticado no mercado imobiliário da região.

O Diagnóstico: Ao aplicar o conhecimento de negócio e engenharia civil para inspecionar os dados brutos (ex: imóvel ID JA1574), identifiquei um erro de escala na base de origem. As colunas AREA_TERRENO e AREA_CONSTRUIDA estavam com os valores multiplicados por 10 (ex: uma casa de 120m² estava registada como 1200m²).

A Solução Aplicada:
Em vez de corrigir manualmente na folha de cálculo, implementei uma regra de tratamento diretamente no pipeline de ETL em Python (Pandas) para garantir a reprodutibilidade. A transformação divide os vetores de área por 10 antes da criação das métricas financeiras calculadas:

Tratamento no pipeline ETL para correção de escala

df['AREA_TERRENO'] = df['AREA_TERRENO'] / 10

df['AREA_CONSTRUIDA'] = df['AREA_CONSTRUIDA'] / 10

Impacto: A correção reestabeleceu a precisão matemática do painel, permitindo que os investidores simulem o VGV e a rentabilidade com base em dados corretos.
O erro identificado poderia ser corrigido na planilha original, porém optou-se pela correção no código python para trabalhar o uso de ferramenta.
Esse pensamento repetiu-se para algumas configurações identificáveis no código .py;
