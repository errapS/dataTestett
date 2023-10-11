with planets as (
  select
    *
  from {{ ref('stg_planets')}}
),

people as (
  select
    *
  from {{ ref('stg_people')}}
),

final as (
  select
    people.person_id,
    planets.planet_name
  from
    people 
  join
    planets
  on
    people.homeworld_id = planets.planet_id
)

select * from final