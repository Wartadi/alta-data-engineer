SELECT
    details.order_detail_id,
    details.order_id,
    orders.order_date AS order_at,  -- Ganti order_at dengan order_date jika order_at tidak ada
    normalized_phone,
    CASE
        WHEN {{ normalize_phone_number('orders.customer_phone') }} LIKE '62%' THEN 'Indonesia'
        WHEN {{ normalize_phone_number('orders.customer_phone') }} LIKE '91%' THEN 'India'
        ELSE 'Unknown'
    END AS country,
    products.brand_id,
    products.brand_name,
    details.product_id,
    products.product_name,  -- Pastikan kolom ini ada di model int_products
    details.quantity AS order_qty,  
    details.unit_sales
FROM {{ ref('stg_order_details') }} AS details
LEFT JOIN {{ ref('int_orders') }} AS orders
    ON details.order_id = orders.order_id
LEFT JOIN {{ ref('int_products') }} AS products
    ON details.product_id = products.product_id