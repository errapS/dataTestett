
{% macro array_to_id(field) %}
list_apply({{ field }}::text[], x -> {{ get_id('x') }})
{% endmacro %}

{% macro to_type(field, type='int') %}
case 
  when {{field}} = 'unknown' then NULL
  when {{field}} = 'none' then NULL
  when {{field}} = 'n/a' then NULL
  when {{field}} = 'indefinite' then 2147483647
  when contains({{field}}, ',') then (replace({{field}}, ',', '.'))::{{type}}
else {{field}}::{{type}}
end
{% endmacro %}

{% macro to_float(field) %}
{{ to_type(field, 'float')}}
{% endmacro %}

{% macro to_int(field, int_type='int') %}
{{ to_type(field, int_type) }}
{% endmacro %}