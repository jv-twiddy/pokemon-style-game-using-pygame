import sys
import random as r
import pygame
import poke_data
from pygame.locals import * 


def check_input(position):
  keys = pygame.key.get_pressed()

  if position == 0:
    if keys[pygame.K_DOWN]:
      return 2
    elif keys[pygame.K_RIGHT]:
      return 1
    else:
      return 0

  elif position == 1:
    if keys[pygame.K_DOWN]:
      return 3
    elif keys[pygame.K_LEFT]:
      return 0
    else:
      return 1

  elif position == 2:
    if keys[pygame.K_UP]:
      return 0
    elif keys[pygame.K_RIGHT]:
      return 3
    else:
      return 2

  elif position == 3:
    if keys[pygame.K_UP]:
      return 1
    elif keys[pygame.K_LEFT]:
      return 2
    else:
      return 3


def step_act(move, player_health, enemy_health, p_mon,e_mon):  # this processes the attack

  player_type=p_mon['type']
  enemy_type=e_mon['type']

  e_choice = r.randint(0, 3)
  e_choice = e_mon['moves'][e_choice]
  print(e_choice)

  if move[3] == 'a':
    pa_mod=p_mon['atk']/e_mon['def']
  else:
    pa_mod=p_mon['sp atk']/e_mon['sp def']

  if e_choice[3] == 'a':
    ea_mod=e_mon['atk']/p_mon['def']
  else:
    ea_mod=e_mon['sp atk']/p_mon['sp def']

  enemy_health-=move[2]*type_check(move[1],enemy_type)*pa_mod
  player_health-=e_choice[2]*type_check(e_choice[1],player_type)*ea_mod

  ##player attacks

  return [player_health, enemy_health, e_choice]

def type_check(a_type,d_type):

  if a_type==d_type:
    val=1

  elif (a_type=='normal') or (d_type =='normal'):
    val= 1
  elif a_type=='fire':
    if d_type=='water':
      val=0.5
    elif d_type=='grass':
      val=2

  elif a_type=='water':
    if d_type=='grass':
      val=0.5
    elif d_type=='fire':
      val=2

  elif a_type=='grass':
    if d_type=='fire':
      val=0.5
    elif d_type=='water':
      val=2
  else:
    val=1
    print(d_type,a_type)

  print(val)
  return val

def open_bag(inventory):

  window = pygame.display.set_mode((400, 600))
  myfont = pygame.font.SysFont("monospace", 20)
  BLACK = (0, 0, 0)
  run=True
  position=0



  while run:

    pos_print=0

    for event in pygame.event.get():
      keys = pygame.key.get_pressed()

      if event.type == KEYDOWN:

        if keys[pygame.K_SPACE]:

          return [inventory[position], remove_item(inventory,position)]
        if keys[pygame.K_UP]:
          position-=1
        if keys[pygame.K_DOWN]:
          position+=1
        if keys[pygame.K_b]:
          return ['null', inventory]

    window.fill((255, 255, 255))
    for items in inventory: 
      item_t =  myfont.render(items[0]+'x'+str(items[1]), 1, BLACK)
      window.blit(item_t, (100, 35+75*pos_print))
      pos_print+=1

    pygame.draw.rect(window, (0, 0, 0), [0, position*75, 400, 75], 3)
    pygame.display.update()

def remove_item (bag, choice):
  if bag[choice][1]==1:
    del bag[choice]
  else:
    bag[choice][1]=bag[choice][1]-1
  return bag 

def item_act(item, player_health, enemy_health): 
  if item[2]=='player':
    if item[3]=='health':
      player_health+=item[4]
  return[player_health,enemy_health]

#########################
#---------FIGHT---------#
#########################
def fight(p_mon,e_mon,bag):       

  window = pygame.display.set_mode((400, 600))
  #-------ASSIGN BASIC VARIABLES------

  position = 0  # variable to store the choice of positions
  positions = [[0, 300], [200, 300], [0, 450], [200, 450]]

  menu='main' #stores the which menu they are in

  main_menu_options = ['moves', 'defend', 'special', 'run']

  player_health = p_mon['max hp']
  enemy_health = e_mon['max hp']

  # TEMPORARY GET LEVEL 
  player_lvl=p_mon['level']
  enemy_lvl=e_mon['level']

  myfont = pygame.font.SysFont("monospace", 20)
  myfont2= pygame.font.SysFont("monospace", 15)
  BLACK = (0, 0, 0)
  e_choice = ' '    #holds text of enemy move

  step = False # makes sure that the moves arent just re occuring between inputs 
  run = True

  moves=p_mon["moves"]

  move_e=e_mon['moves']

  #--- setting unchanging text---
  #main menu
  T_moves =  myfont.render("moves", 1, BLACK)  
  T_defend =  myfont.render("bag", 1, BLACK)
  T_special = myfont.render("not yet", 1, BLACK)
  T_run =     myfont.render("run", 1, BLACK)

  #moves
  T_move1 =  myfont.render(moves[0][0], 1, BLACK)
  T_move2 =  myfont.render(moves[1][0], 1, BLACK)
  T_move3 =  myfont.render(moves[2][0], 1, BLACK)
  T_move4 =  myfont.render(moves[3][0], 1, BLACK)

  #--- GAME IMAGES ---#

  player_o = pygame.image.load(p_mon['img']).convert_alpha()
  player_i = pygame.transform.scale(player_o, (100, 100))

  enemy_o = pygame.image.load(e_mon['img']).convert_alpha()
  enemy_i = pygame.transform.scale(enemy_o, (100, 100))

  window.fill((255, 255, 255))

  #--------GAME LOOP---------# 

  while run:          
    for event in pygame.event.get():
      keys = pygame.key.get_pressed()

    #------ MENUING ------#

      if event.type == KEYDOWN:  #get key press

        if keys[pygame.K_SPACE]:
          if menu=='main' and position==0:    #enter moves menu 
            menu='moves'

          elif menu=='main' and position==1:     #bag
            bag_store=open_bag(bag)
            if bag_store[0]!='null':
              bag=bag_store[1]
              temp=item_act(bag_store[0],player_health,enemy_health)
              player_health=temp[0]
              enemy_health=temp[1]

          elif menu=='main' and position==2:
            # switch pokemon ?!?!?
            print('not done yet')

          elif menu=='main' and position==3:    #run
            run=False

          elif menu=='moves':                    #move select
            # get move and set to variable
            move_choice=moves[position]
            step=True

        elif keys[pygame.K_b] and menu=='moves':

          menu='main'

        else:
          position = check_input(position)

      #---- ACTIONING INPUT ----#
      if step:

        midway = step_act(move_choice, player_health, enemy_health, p_mon, e_mon)

        if midway == 'QUIT':
          run = False
        else:
          player_health = midway[0]
          enemy_health = midway[1]
          e_choice = midway[2]    

        step = False  #stops the moves from repeating over and over

      #--- check if health for ending game ---#
      if player_health <= 0:
        return 'DEFEAT'
      elif enemy_health <= 0:
        exp_gain=(enemy_lvl*100)/type_check(p_mon['type'],e_mon['type'])
        return exp_gain

    #----------DRAWING------THE------SCREEN-----------
    window.fill((255, 255, 255))
    #-------TEXT----- 

    TE_health=myfont2.render((str(enemy_health)+'/'+str(e_mon['max hp'])),1,BLACK)
    TP_health=myfont2.render((str(player_health)+'/'+str(p_mon['max hp'])),1,BLACK)

    TE_choice=myfont2.render(("enemy choice:"+e_choice[0]),1,BLACK)

    window.blit(TE_choice,(180, 250)) #enemies move
    if menu=='main':
      window.blit(T_moves, (100, 375))
      window.blit(T_defend, (300, 375))
      window.blit(T_special, (100, 525))
      window.blit(T_run, (300, 525))

    if menu=='moves':
      window.blit(T_move1, (100, 375))
      window.blit(T_move2, (300, 375))
      window.blit(T_move3, (100, 525))
      window.blit(T_move4, (300, 525))

    #-- HEALTH BARS------
    pygame.draw.line(window, (0, 255, 0), [245, 50], [245 + enemy_health, 50], 3)
    window.blit(TE_health, (245, 40))

    pygame.draw.line(window, (0, 255, 0), [45, 110], [45 + player_health, 110], 3)
    window.blit(TP_health, (45, 100))

    #-----DRAW PLAYERS-----
    window.blit(player_i,(50,150))
    window.blit(enemy_i,(250,50))
    #-----DRAW CHOICE BOX-----
    pygame.draw.rect(window, (0, 0, 0), [positions[position][0], positions[position][1], 200, 150], 2)

    pygame.display.update()
  return 'DEFEAT'

def lvl_up(p_mon , exp_gain):
  lvl=p_mon['level']
  exp2_lvl= p_mon['exp up']
  exp_crnt=p_mon['exp']
  evs=p_mon['evs']
  
  print(lvl, exp2_lvl, exp_crnt, exp_gain)

  window = pygame.display.set_mode((400, 600))

  myfont = pygame.font.SysFont("monospace", 30)

  BLACK = (0, 0, 0)
  GREEN = (0,250,0)
  TERQ = (0,175,175)
  
  lvldnt=True  # what a fucking terrible variable name
  # lvldnt becomes false when they dont have ebnough exp 2 lvl breaking the cycle 
  first=True
  
  while lvldnt:
    exp_cr=(exp_crnt*200)/exp2_lvl
    exp_gr=(exp_gain*200)/exp2_lvl
    #--- draw sceen---

    window.fill((255,255,255))          
    if first:             # on first way round they have old exp
      pygame.draw.line(window, GREEN, [100,125],[100+exp_cr,125],3)
      pygame.draw.line(window, TERQ, [100+exp_cr,125],[100+exp_cr+exp_gr,125],3)
      first=False
    else:     #further lvls it will be new exp
      pygame.draw.line(window, TERQ, [100,125],[100+exp_cr,125],3)
      
    pygame.draw.line(window, BLACK, [100,100], [100,150],3)
    pygame.draw.line(window, BLACK, [300,100], [300,150],3)
    

    exp_crnt+=exp_gain
    exp_gain=0
    if exp_crnt>=exp2_lvl:
      line1=myfont.render('level:'+str(lvl)+'+1',1,BLACK)
      line2=myfont.render('helath:'+str(p_mon['max hp'])+'+'+str(evs[0]),1,BLACK)
      line3=myfont.render('attack:'+str(p_mon['atk'])+'+'+str(evs[1]),1,BLACK)
      line4=myfont.render('defense:'+str(p_mon['def'])+'+'+str(evs[2]),1,BLACK)
      line5=myfont.render('special attack:'+str(p_mon['sp atk'])+'+'+str(evs[3]),1,BLACK)
      line6=myfont.render('special defense:'+str(p_mon['sp def'])+'+'+str(evs[4]),1,BLACK)
      line7=myfont.render('speed'+str(p_mon['speed'])+'+'+str(evs[5]),1,BLACK)
      window.blit(line1, (100, 175))
      window.blit(line2, (100, 200))
      window.blit(line3, (100, 225))
      window.blit(line4, (100, 250))
      window.blit(line5, (25, 275))
      window.blit(line6, (25, 300))
      window.blit(line7, (100, 325))
      lvl+=1
      exp_crnt-=exp2_lvl
      exp2_lvl=exp2_lvl*(1+(lvl/100))
      p_mon['max hp']+=evs[0]
      p_mon['atk']+=evs[1]
      p_mon['def']+=evs[2]
      p_mon['sp atk']+=evs[3]
      p_mon['sp def']+=evs[4]
      p_mon['speed']+=evs[5]
      
    else:
      lvldnt=False
      print('here')

    pygame.display.update()
    
    contin = False      # wait for input :)
    while not contin:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          contin = True
          print('here2')
    
  p_mon['level']= lvl
  p_mon['exp up'] = exp2_lvl
  p_mon['exp'] = exp_crnt
  return p_mon



def roam(p_mon,bag):
  window = pygame.display.set_mode((400, 600))

  background_o = pygame.image.load('roam.png').convert_alpha()
  background_i = pygame.transform.scale(background_o, (400, 600))

  player_o = pygame.image.load(p_mon['img']).convert_alpha()
  player_i = pygame.transform.scale(player_o, (40, 40))

  player_x,player_y= 200, 300 
  clock = pygame.time.Clock()

  pokedex=poke_data.pokedex()

  run=True
  step=False
  while run:
    clock.tick(30)
    for event in pygame.event.get():
      if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        pygame.quit()
        sys.exit()

    if run:
      keys= pygame.key.get_pressed()
      if keys[pygame.K_DOWN]:
        player_y+=5
        step=True
      elif keys[pygame.K_UP]:
        player_y-=5
        step=True
      elif keys[pygame.K_LEFT]:
        player_x-=5
        step=True
      elif keys[pygame.K_RIGHT]:
        player_x+=5
        step=True

    #-- check player position --#
    if step:
      if player_x<185 and player_y<100:
        fight_c=r.random()
        if fight_c>0.95:
          enemy= pokedex[r.randint(0,3)]
          exp_gain=fight(p_mon,enemy,bag)
          if exp_gain != 'DEFEAT':
            p_mon= lvl_up(p_mon,exp_gain)
          else:
            print('lost')
          print(p_mon['level'],p_mon['exp up'],p_mon['exp'])


      if player_x<100 and 200<player_y<500:
        fight_c=r.random()
        if fight_c>0.95:
          enemy= pokedex[r.randint(0,3)]
          exp_gain=fight(p_mon,enemy,bag)
          if exp_gain == 'DEFEAT':
            print('lost')
          else:
            p_mon = lvl_up(p_mon,exp_gain)
          print(p_mon['level'],p_mon['exp up'],p_mon['exp'])
      step=False
  #--- draw---#
    window.fill((0,0,0))
    window.blit(background_i,(0,0))
    window.blit(player_i,(player_x,player_y))

    pygame.display.update()


#-- end screen---
#window.fill((255, 255, 255))
#end_text =  myfont.render("game over", 1, BLACK)
#window.blit(end_text, (130, 100))
#pygame.display.update()


#---start----
pygame.init()

p_mon=poke_data.pokedex()[0]
bag=[
  ['heal',3,'player','health',20],
  ['small heal',3,'player','health',10],
  [' mega heal',1,'player','health',50]
]


roam(p_mon,bag)

x = input()
pygame.quit()
