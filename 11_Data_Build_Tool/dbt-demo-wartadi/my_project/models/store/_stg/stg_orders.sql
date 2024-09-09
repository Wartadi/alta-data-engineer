select
    order_id::int as order_id
    , order_date::timestamp as order_date
    , customer_phone
    , {{ normalize_phone_number('orders.customer_phone') }} as normalized_phone
from {{ source('store', 'orders') }}