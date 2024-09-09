{% macro format_currency(value, currency_symbol='$') %}
    {% set formatted_value = value | float | format('0,.2f') %}
    {{ currency_symbol ~ ' ' ~ formatted_value }}
{% endmacro %}