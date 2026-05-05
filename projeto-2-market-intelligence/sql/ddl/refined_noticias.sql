CREATE TABLE REFINED_NOTICIAS AS
SELECT 
    CASE 
        WHEN snippet LIKE '%selic%' THEN 'SELIC'
        WHEN snippet LIKE '%inflação%' THEN 'INFLACAO'
        WHEN snippet LIKE '%juros%' THEN 'JUROS'
        ELSE 'OUTROS'
    END AS categoria,
    COUNT(*) AS quantidade
FROM TRUSTED_NOTICIAS
GROUP BY 
    CASE 
        WHEN snippet LIKE '%selic%' THEN 'SELIC'
        WHEN snippet LIKE '%inflação%' THEN 'INFLACAO'
        WHEN snippet LIKE '%juros%' THEN 'JUROS'
        ELSE 'OUTROS'
    END;
