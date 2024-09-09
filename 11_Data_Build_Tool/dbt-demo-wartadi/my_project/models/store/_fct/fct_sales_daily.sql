SELECT
    order_id,
    order_at,
    country,
    brand_id,
    brand_name,
    product_name,  -- Menambahkan product_name
    order_qty,
    unit_sales AS daily_unit_sales
FROM {{ ref('int_order_details') }}
