CREATE TABLE TRUSTED_NOTICIAS AS
SELECT 
    LOWER(titulo) AS titulo,
    link,
    LOWER(snippet) AS snippet,
    data_carga
FROM RAW_NOTICIAS;
