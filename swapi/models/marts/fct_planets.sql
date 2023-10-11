with source as (
  select
    *
  from {{ ref('stg_planets')}}
),

final as (
  select
    planet_id,
    planet_name,
    orbital_period,
    diameter,
    climate,
    gravity,
    surface_water,
    population,
    {{ count_numof('residents_id') }} AS number_of_residents,
    {{ count_numof('films_id') }} AS number_of_films
  from source
)

select * from final