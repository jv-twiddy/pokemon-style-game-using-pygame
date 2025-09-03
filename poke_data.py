def pokedex():
  pokemons=[
    {
      'name':'Mossozor',
      'img':'moss.png',
      'type':'grass',
      'level':10,
      'exp up':1000,
      'exp':0,
      'max hp':100,
      'hp':100,
      'atk':30,
      'def':30,
      'sp atk':40,
      'sp def':35,
      'speed':10,
      'evs':[10,3,3,4,3.5,1],
      'moves':[
        ['slice','grass',20,'s'],
        ['headbutt','normal',40,'a'],
        ['grow','normal',10,'a'],
        ['squirt','water',20,'s']
      ]
    },
    {
      'name':'Chardeer',
      'img':'deer.png',
      'type':'fire',
      'level':10,
      'exp up':1000,
      'exp':0,
      'max hp':100,
      'hp':100,
      'atk':30,
      'def':30,
      'sp atk':40,
      'sp def':35,
      'speed':20,
      'evs':[8,3,3,4,3.5,2],
      'moves':[
        ['ember','fire',25,'s'],
        ['stomp','normal',35,'a'],
        ['flare','fire',10,'s'],
        ['dash','normal',20,'a']
      ]
    },
    {
      'name':'Dropkane',
      'img':'dog.png',
      'type':'water',
      'level':10,
      'exp up':1000,
      'exp':0,
      'max hp':100,
      'hp':100,
      'atk':30,
      'def':30,
      'sp atk':40,
      'sp def':35,
      'speed':15,
      'evs':[9,3,3,4,3.5,1.5],
      'moves':[
        ['splash','water',20,'s'],
        ['headbutt','normal',40,'a'],
        ['grow','grass',10,'s'],
        ['squirt','water',20,'s']
      ]
    },
    {
      'name':'Dmouse',
      'img':'mouse.png',
      'type':'normal',
      'level':10,
      'exp up':1000,
      'exp':0,
      'max hp':60,
      'hp':60,
      'atk':10,
      'def':15,
      'sp atk':10,
      'sp def':15,
      'speed':30,
      'evs':[12,4,1.5,1,1.5,3],
      'moves':[
        ['nible','normal',10,'a'],
        ['scratch','normal',15,'a'],
        ['grow','grass',10,'s'],
        ['nible','normal',10,'a']
      ]
    }
    ]
  return pokemons

bag=[
  ['heal',3,'player','health',20],
  ['small heal',3,'player','health',10],
  [' mega heal',1,'player','health',50]
]
  
  



#fire>grass
#grass>water
#water>fire
#normal is nuetral for now