-- =========================
-- RAW → TRUSTED
-- =========================

INSERT INTO TRUSTED_SELIC (data, valor, data_carga)
SELECT 
    TO_DATE(data_raw, 'YYYY-MM-DD'),
    TO_NUMBER(valor_raw),
    data_carga
FROM RAW_SELIC;


-- =========================
-- TRUSTED → REFINED
-- =========================

INSERT INTO REFINED_SELIC_MENSAL
SELECT 
    TRUNC(data, 'MM'),
    AVG(valor),
    MIN(valor),
    MAX(valor)
FROM TRUSTED_SELIC
GROUP BY TRUNC(data, 'MM');
