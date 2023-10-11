with source as (
  select
    *
  from {{ ref('stg_people')}}
),

final as (
  select
    person_id,
    name,
    height,
    mass,
    hair_color,
    skin_color,
    eye_color,
    birth_year,
    gender,
    {{ count_numof('films_id') }} AS number_of_films,
    {{ count_numof('vehicles_id') }} AS number_of_vehicles,
    {{ count_numof('starships_id') }} AS number_of_starships
  from source
)

select * from final