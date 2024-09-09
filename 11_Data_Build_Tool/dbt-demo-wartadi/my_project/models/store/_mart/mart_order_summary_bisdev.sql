SELECT
    DATE_TRUNC('month', order_at) AS month,
    brand_id,
    brand_name,
    product_name, 
    SUM(order_qty) AS total_order_qty,
    SUM(daily_unit_sales) AS total_unit_sales,
    SUM(daily_unit_sales * order_qty) AS total_amount
FROM {{ ref('fct_sales_daily') }}
GROUP BY 1, 2, 3, 4
ORDER BY 1, 2, 3
