select *
from {{ ref('fct_orders') }}
where mart_flaging = 'Sales Marketing 1'