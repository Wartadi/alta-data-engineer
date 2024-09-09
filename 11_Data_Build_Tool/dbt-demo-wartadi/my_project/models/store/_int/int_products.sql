SELECT
    products.product_id,
    products.product_name,
    products.product_price,
    brands.brand_id,  
    brands.brand_name
FROM {{ ref('stg_products') }} as products
left JOIN {{ ref('stg_brands') }} as brands 
    ON products.brand_id = brands.brand_id