with source as (
  select
    *
  from {{ source('raw', 'raw_planets')}}
),

final as (
  select
    {{ extract_id_from_url('url') }} AS planet_id,
    {{ convert_to_varchar('name') }} AS planet_name,
    {{ convert_to_int('orbital_period') }} AS orbital_period,
    {{ convert_to_float('diameter') }} AS diameter,
    {{ convert_to_varchar('climate') }} AS climate,
    {{ convert_to_varchar('gravity') }} AS gravity,
    {{ cast_to_float('surface_water') }} AS surface_water,
    {{ check_population('population') }} AS population,
    {{ extract_ids_from_url_array('residents')}} AS residents_id,
    {{ extract_ids_from_url_array('films')}} AS films_id,
    created,
    edited
from source
)

select * from final
