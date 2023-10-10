with source as (
  select
    *
  from {{ ref('people_model') }}
),

final as (
  select
    name,
    height,
    mass,
    hair_color,
    skin_color,
    eye_color,
    birth_year,
    gender,
    homeworld,
    films,
    species,
    vehicles,
    starships,
    created,
    edited,
    url
  from source
)


select * from final