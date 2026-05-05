-- =====================================
-- RAW → TRUSTED
-- =====================================

INSERT INTO TRUSTED_SELIC (data, valor, data_carga)
SELECT 
    TO_DATE(data_raw, 'YYYY-MM-DD'),
    TO_NUMBER(valor_raw),
    data_carga
FROM RAW_SELIC
WHERE valor_raw IS NOT NULL;


-- =====================================
-- TRUSTED → REFINED
-- =====================================

INSERT INTO REFINED_SELIC_MENSAL (mes, media_selic, min_selic, max_selic, qtd_registros)
SELECT 
    TRUNC(data, 'MM'),
    AVG(valor),
    MIN(valor),
    MAX(valor),
    COUNT(*)
FROM TRUSTED_SELIC
GROUP BY TRUNC(data, 'MM')
ORDER BY mes;
