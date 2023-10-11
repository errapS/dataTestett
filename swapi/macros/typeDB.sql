{% macro convert_to_int(field) %}
  CASE
    WHEN {{ field }} IN ('unknown', 'none', 'n/a') THEN NULL
    ELSE CAST({{ field }} AS integer)
  END
{% endmacro %}

{% macro convert_to_float(field) %}
  CASE
    WHEN {{ field }} IN ('unknown', 'none', 'n/a') THEN NULL
    WHEN {{ field }}::text LIKE '%,%' THEN CAST(replace({{ field }}::text, ',', '.') AS double precision)
    ELSE CAST({{ field }} AS double precision)
  END
{% endmacro %}

{% macro convert_to_varchar(field) %}
  CASE
    WHEN {{ field }} = 'n/a' THEN NULL
    ELSE {{ field }}::text
  END
{% endmacro %}

{% macro extract_id_from_url(url_field) %}
  CASE
    WHEN position('/' in reverse({{ url_field }})) = 0 THEN NULL
    ELSE CAST(substring({{ url_field }} from '/([0-9]+)/?$') AS integer)
  END
{% endmacro %}

{% macro extract_ids_from_url_array(url_array) %}
  ARRAY(
    SELECT
      CAST(substring(url from '/([0-9]+)/') AS integer)
    FROM UNNEST(string_to_array({{ url_array }}, ',')) AS url
  )
{% endmacro %}

{% macro count_numof(field) %}
  CAST(array_length({{ field }}, 1) - 1 AS int)
{% endmacro %}


{% macro check_population(field) %}
  CASE
    WHEN {{ field }} IN ('unknown', 'none', 'n/a') THEN NULL
    WHEN {{ field }}::bigint <= 2147483647 THEN {{ field }}::bigint
    ELSE 2147483647
  END
{% endmacro %}

{% macro cast_to_float(field) %}
  CASE
    WHEN {{ field }} ~ '^[0-9]+$' THEN CAST({{ field }} AS float)
    WHEN {{ field }} ~ '^[0-9]+\.[0-9]*$' THEN CAST({{ field }} AS float)
    ELSE NULL
  END
{% endmacro %}