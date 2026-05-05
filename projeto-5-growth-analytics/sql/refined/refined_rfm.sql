CREATE TABLE REFINED_RFM AS
SELECT 
    fk_contact,

    MAX(date_purchase) AS last_purchase,
    COUNT(*) AS frequency,
    SUM(gmv_success) AS monetary,

    TRUNC(SYSDATE - MAX(date_purchase)) AS recency

FROM TRUSTED_TRANSACTIONS
GROUP BY fk_contact;
