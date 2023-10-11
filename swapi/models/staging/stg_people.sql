with source as (
  select
    *
  from {{ ref('raw_people')}}
),

final as (
  select
    {{ extract_id_from_url('url') }} AS person_id,
    {{ convert_to_varchar('name') }} AS name,
    {{ convert_to_int('height') }} AS height,
    {{ convert_to_float('mass') }} AS mass,
    {{ convert_to_varchar('hair_color') }} AS hair_color,
    {{ convert_to_varchar('skin_color') }} AS skin_color,
    {{ convert_to_varchar('eye_color') }} AS eye_color,
    {{ convert_to_varchar('birth_year') }} AS birth_year,
    {{ convert_to_varchar('gender') }} AS gender,
    {{ extract_id_from_url('homeworld') }} AS homeworld_id,
    {{ extract_ids_from_url_array('films')}} AS films_id,
    {{ extract_ids_from_url_array('species')}} AS species_id,
    {{ extract_ids_from_url_array('vehicles')}} AS vehicles_id,
    {{ extract_ids_from_url_array('starships')}} AS starships_id,
    created,
    edited
from source
)

select * from final

