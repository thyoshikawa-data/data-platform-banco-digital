CREATE TABLE REFINED_STOCKS AS
SELECT 
    ticker,
    AVG(close) AS avg_price,
    MIN(low) AS min_price,
    MAX(high) AS max_price,
    STDDEV(close) AS volatility
FROM TRUSTED_STOCKS
GROUP BY ticker;
