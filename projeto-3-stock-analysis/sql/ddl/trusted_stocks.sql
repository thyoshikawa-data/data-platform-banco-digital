CREATE TABLE TRUSTED_STOCKS AS
SELECT 
    ticker,
    data,
    open,
    high,
    low,
    close,
    volume
FROM RAW_STOCKS;
