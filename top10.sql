SELECT 
    DISTRITO,
    BAIRRO,
    COUNT(*) AS Qtd_Vendidos
FROM 
    imoveis
WHERE 
    ATIVO = 'VENDIDO'
GROUP BY 
    DISTRITO,
    BAIRRO
ORDER BY 
    Qtd_Vendidos DESC
LIMIT 10;