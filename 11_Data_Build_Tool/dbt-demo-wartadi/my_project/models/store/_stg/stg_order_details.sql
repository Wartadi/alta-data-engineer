SELECT
    order_detail_id::int AS order_detail_id,
    order_id::int AS order_id,
    product_id::int AS product_id,
    quantity::int AS quantity,  -- Pastikan nama kolom ini sesuai
    price::float AS unit_sales
FROM {{ source('store', 'order_details') }}