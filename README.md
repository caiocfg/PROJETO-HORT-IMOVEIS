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

### Troubleshooting de Localidade (Locale Clash) no Pipeline de Dados
O Cenário: Durante a validação das métricas no Power BI, o KPI de Valor Médio do Metro Quadrado (R$/m²) apresentou distorções críticas. O Power BI estava lendo a área dos imóveis de forma superestimada (ex: um imóvel de 120m² era lido como 1200m²), o que derrubou artificialmente o ticket médio.

O Diagnóstico (Causa Raiz): Após inspecionar a base original, verifiquei que os dados não possuíam erro de escala. O problema era um conflito de integração (Locale Clash). O Pandas (Python) estava exportando o CSV no padrão americano, utilizando o "ponto" para separar as casas decimais (ex: 120.0). Quando o motor do Power BI (configurado em PT-BR) importava o arquivo, ele interpretava esse ponto americano como um separador de milhar brasileiro, ignorando-o e transformando 120.0 em 1200.

A Solução de Engenharia Aplicada: Em vez de realizar tratamentos matemáticos paliativos na base (como dividir a coluna por 10, o que corromperia o dado original para outras ferramentas), a solução foi atuar diretamente na serialização do pipeline ETL. Configurei o script Python para forçar o delimitador e as casas decimais para o padrão PT-BR no momento do output.

### Fix de Integração: Forçando delimitador (;) e decimal (,) no output para alinhar com o BI local
dim_localizacao.to_csv('dim_localizacao.csv', index=False, sep=';', decimal=',')

fato_ofertas.to_csv('fato_ofertas.csv', index=False, sep=';', decimal=',')

Impacto: A correção restabeleceu a precisão da métrica (Ticket Médio real de R$ 4.270,00 / m²) sem adulterar os dados originais, garantindo que o dataset possa ser consumido com segurança por qualquer outra ferramenta do stack de dados.

O erro identificado poderia ser corrigido na planilha original, porém optou-se pela correção no código python para trabalhar o uso da ferramenta.
Esse pensamento repetiu-se para algumas configurações identificáveis no código .py;
