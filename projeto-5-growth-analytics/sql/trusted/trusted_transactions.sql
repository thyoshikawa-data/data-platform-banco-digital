CREATE TABLE TRUSTED_TRANSACTIONS AS
SELECT 
    fk_contact,
    date_purchase,
    gmv_success,
    total_tickets_quantity_success,
    
    place_origin_departure || ' → ' || place_destination_departure AS route_dep,

    CASE 
        WHEN place_origin_return IS NOT NULL THEN 1
        ELSE 0
    END AS is_return

FROM RAW_OTA_PURCHASES
WHERE fk_contact IS NOT NULL;
