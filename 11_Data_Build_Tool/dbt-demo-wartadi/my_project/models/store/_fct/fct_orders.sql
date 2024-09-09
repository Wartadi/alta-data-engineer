select
    order_id
    , order_date
    , normalized_phone
    , case
        when orders.order_id % 2 != 0 then 'Sales Marketing 1'
        else 'Sales Marketing 2'
    end as mart_flaging

from {{ ref('int_orders') }} as orders