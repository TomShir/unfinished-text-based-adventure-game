#Create a text-based adventure game in Python 
from playsound import playsound
from colorama import Fore 
import sys 
import os 
import tqdm 
import random 
import logging 
import time 
import tqdm
#ascii_art:
game_title='''
 ____  ____      ______    ____  ____  ______  _______
/___/ /   /     /     / \ /   / /   / /______ |       \ 
\___\/   /____ /  ___/  /  \______ / /______  /   ___ / 
/___/________//__/  /__/  /_______/ /_______ /__/  \_/
'''
boss_battle_title='''
 _____        ____  ____  _____    ____   ______   ______   ___      _______
|_____) ____ /___/ /___/ |_____)  /    \\ |______| |______| |   |    | |_____
|_____)|    |\___\ \___\ |_____) /______\\  |  |     |  |   |   |___ | |_____
|_____)|____|/___/ /___/ |_____)/        \\ |__|     |__|   |___|___||_|_____ '''
thanks_for_playing_screen='''
 ________
 |__   __| |               | |         / _|           |  __ \| |           (_)            
    | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __  | |__) | | __ _ _   _ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__| |  ___/| |/ _` | | | | | '_ \ / _` |
    | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | |    | | (_| | |_| | | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\___/ |_| \___/|_|    |_|    |_|\__,_|\__, |_|_| |_|\__, |
                                                                       __/ |         __/ |
                                                                      |___/         |___/ '''
ascii_bread='''
    
    
    
             __________                    
          __|          |
       __|             |
    __|                |
 ___|                  | 
|                      |
|                    __|
|                    |
|_                 __|
 |__               |
    |__          __|  
      |__________|'''  
ascii_health_potion='''
   
   _______________________
  \\                      /
   \\                    /
    \\__________________/
       |_____________|
  ______|___________|______
  | _____________________  |
  |                        |
  |                        | 
  |                        |
  |                        |
  |                        |
  |                        |
  |                        |
  |________________________|
        '''
ascii_you_lost_msg='''
 __   __  _______  __   __    ___      _______  _______  _______ 
|  | |  ||       ||  | |  |  |   |    |       ||       ||       |
|  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||_     _|
|       ||  | |  ||  |_|  |  |   |    |  | |  || |_____   |   |  
|_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  |  |   |  
  |   |  |       ||       |  |       ||       | _____| |  |   |  
  |___|  |_______||_______|  |_______||_______||_______|  |___|  '''
ascii_you_won_msg='''
 __   __  _______  __   __    _     _  _______  __    _  __  
|  | |  ||       ||  | |  |  | | _ | ||       ||  |  | ||  | 
|  |_|  ||   _   ||  | |  |  | || || ||   _   ||   |_| ||  | 
|       ||  | |  ||  |_|  |  |       ||  | |  ||       ||  | 
|_     _||  |_|  ||       |  |       ||  |_|  ||  _    ||__| 
  |   |  |       ||       |  |   _   ||       || | |   | __  
  |___|  |_______||_______|  |__| |__||_______||_|  |__||__| '''
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.CYAN,Fore.MAGENTA,Fore.RESET]
sounds=['sand.mp3','roar.mp3','twig.mp3','wolf.mp3','error.mp3']
biomes=['Desert','Artic','Forest','Space']
weapons=['sword','warhammer','nunchucks','shurikens','scythe','spear','katana']
default_health=100
range_of_numbers=list(range(1,101,1))
#weapon damage stats:
sword_damage=30
warhammer_damage=40 
nunchucks_damage=19
scythe_damage=27
shuriken_damage=18
katana_damage=23 
spear_damage=25
player_inventory=[]
player_attack_power=20
#Creating player class  to store player's stats 
class Player:
  def __init__(self,name,health,damage_dealt,opponent,receive_damage,weapon,attack_power):
    self.health=health 
    self.damage_dealt=damage_dealt 
    self.opponent=opponent 
    self.receive_damage=receive_damage 
    self.weapon=weapon
    self.attack_power=attack_power 
    self.name=name
  def assault(self):
    print(f'{self.name} attacks {self.opponent},dealing {self.attack_power} points of damage')
    
  def damage_taken(self):
    if self.health<=100 and self.health>50:
      for num in tqdm.tqdm(range_of_numbers,colour='GREEN',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break 
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
    elif self.health<50 and self.health>=31:
      for num in tqdm.tqdm(range_of_numbers,colour='YELLOW',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
    elif self.health<30:
      for num in tqdm.tqdm(range_of_numbers,colour='RED',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break 
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
        

  def weapon_assault(self):
    if self.weapon==weapons[0] and self.damage_dealt==sword_damage:
            print(f'You swung your {self.weapon} at {self.opponent} dealing {self.damage_dealt} points of damage.')
    elif self.weapon==weapons[1] and self.damage_dealt==warhammer_damage:
            print(f'You hammered down on {self.opponent}, causing {self.opponent} to lose {self.damage_dealt} points of damage.')
    elif self.weapon==weapons[2] and self.damage_dealt==nunchucks_damage:
            print(f'You swing your {self.weapon} at {self.opponent}, causing him to have grazes and losing {self.damage_dealt} points of health.')
    elif self.weapon==weapons[3] and self.damage_dealt==shuriken_damage:
            print(f'You throw your shurikens at {self.opponent}, dealing {self.damage_dealt} points of damage.')
    elif self.weapon==weapons[4] and self.damage_dealt==scythe_damage:
            print(f'You swing your {self.weapon} at {self.opponent}, dealing {self.damage_dealt} points of damage.')
    elif self.weapon==weapons[5] and self.damage_dealt==spear_damage:
            print(f'You throw your {self.weapon} like a javelin, directly at {self.opponent}, dealing {self.damage_dealt} points of damage.')
    elif self.weapon==weapons[-1] and self.damage_dealt==katana_damage:
            print(f'You wield your dual katana and swing them vertically at {self.opponent}, dealing {self.damage_dealt} points of damage.')
         
#Creating an instance of the player class outside the while loop 
myplayer=Player(name=None,health=default_health,damage_dealt=0,opponent=None,receive_damage=0,weapon=None,attack_power=0)   
#creating a function that loops over a subscriptable sequence and prints it horizontially 
def loop_over(sequence,color,delay_time):
  if sequence==f'{game_title}\n\t':
    for text in sequence:
      sys.stdout.flush()
      time.sleep(0.01)
      sys.stdout.write(f'{random.choice(colors[:-1])}{text}')
    else:
      print(f'{colors[-1]}')
  else:
    for n in sequence:
      sys.stdout.flush()
      time.sleep(delay_time)
      sys.stdout.write(f'{color}{n}')
    else:
      print(f'{colors[-1]}')
      
#Creating a basic monster class 
class Basic_Monster:
  def __init__(self,name,opponent,health,damage_dealt,move,receive_damage):
    self.name=name 
    self.opponent=opponent 
    self.health=health 
    self.damage_dealt=damage_dealt 
    self.move=move 
    self.receive_damage=receive_damage
  def assault(self):
    print(f'{self.opponent} attacks {self.opponent} with its {self.move}, dealing {self.damage_dealt} points of damage')
    
  def damage_taken(self):
    if self.health<=100 and self.health>50:
      for num in tqdm.tqdm(range_of_numbers,colour='GREEN',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break 
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
    elif self.health<50 and self.health>=31:
      for num in tqdm.tqdm(range_of_numbers,colour='YELLOW',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
    elif self.health<30:
      for num in tqdm.tqdm(range_of_numbers,colour='RED',desc='health'):
        time.sleep(0.1)
        if num==self.health-self.receive_damage+1:
          break 
      print(f'{self.name} took damage from {self.opponent}.{self.name} now currently has {self.health-self.receive_damage} points of health')
      
class Cactus_Monster(Basic_Monster):
  pass
#creating a function that handle errors 
def error_message(text):
  #Creating a logging object 
  error_logger=logging.getLogger('error_logger')
  file_handler=logging.FileHandler('ERRORR.log')
  myformat=logging.Formatter('%(asctime)s-%(name)s-%(message)s')
  file_handler.setFormatter(myformat)
  error_logger.setLevel(logging.ERROR)
  file_handler.setLevel(logging.ERROR)
  error_logger.addHandler(file_handler)
  loop_over(sequence=text,color=colors[0],delay_time=0.1)
  time.sleep(1)
  error_logger.error(f'{text}')
  
#Creating a function that sends messages to a log file about the player 
def log_player_information(player_information):
  player_logger=logging.getLogger('Player_Logger:')
  player_logger.setLevel(logging.INFO)
  myformat=logging.Formatter('%(name)s-%(message)s')
  file_handler=logging.FileHandler('Player.log')
  file_handler.setFormatter(myformat)
  file_handler.setLevel(logging.INFO)
  player_logger.addHandler(file_handler)
  player_logger.info(player_information)
  
#Creating a function that can generate options 
def generate_options(number_limit,option1,option2,option3,option4,option5,option6,option7,option8,option9,option10):
  for options in range(number_limit+1):
    if options==1:
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)             
      random.shuffle(colors[:-1])
      print(f'1. {option1}')
      time.sleep(1)
      print('\n')
      time.sleep(1) 
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==2:
      print(f'2. {option2}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==3:
      print(f'3. {option3}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==4:
      print(f'4. {option4}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==5:
      print(f'5. {option5}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==6:
      print(f'6. {option6}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==7:
      print(f'7. {option7}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==8:
      print(f'8. {option8}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==9:
      print(f'9. {option9}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    elif options==10:
      print(f'10. {option10}')
      time.sleep(1)
      print('\n')
      time.sleep(1)
      loop_over(sequence='________________',color=colors[1],delay_time=0.01)
      time.sleep(1)
    else:
      pass
#Creating a function that created a progress  bar based on its parameters 
def create_progress_bar(sequence,bar_colour,number_of_columns,description,delay_time):
  for n in tqdm.tqdm(sequence,colour=bar_colour,ncols=number_of_columns,desc=description):
    time.sleep(delay_time)
  else:
    pass
  
def player_move(player_health,opponent_health,Opponent_class,opponent_alias,opponent_moves):
  myplayer=Player(name=player_name,health=player_health,damage_dealt=0,opponent=opponent_alias,receive_damage=0,weapon=choose_weapon,attack_power=player_attack_power)
  myopponent=Opponent_class(name=opponent_alias,health=opponent_health,receive_damage=0,damage_dealt=0,move=opponent_moves,opponent=player_name) 
  generate_options(number_limit=2,option1=myplayer.weapon,option2='attack',option3=None,option4=None,option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
  choose_fight_option=int(input('option:'))
  if choose_fight_option==1:
    myplayer.weapon_assault()
    if myplayer.weapon==weapons[0]:
     myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=sword_damage,damage_dealt=0,move=opponent_moves,opponent=player_name) 
    elif myplayer.weapon==weapons[1]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=warhammer_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    elif myplayer.weapon==weapons[2]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=nunchucks_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    elif myplayer.weapon==weapons[3]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=shuriken_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    elif myplayer.weapon==weapons[4]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=scythe_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    elif myplayer.weapon==weapons[5]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=spear_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    elif myplayer.weapon==weapons[6]:
      myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=katana_damage,damage_dealt=0,move=opponent_moves,opponent=player_name)
    
    myopponent.damage_taken()
  elif choose_fight_option==2:
    myplayer.assault()
    myopponent=Opponent_class(name=opponent_alias,health=opponent_health-myopponent.receive_damage,receive_damage=player_attack_power,damage_dealt=0,move=opponent_moves,opponent=player_name)
    myopponent.damage_taken()
  else:
    pass
  
#Creating a function that returns a certain output based on the player's input 
def check_move(player_move,correct_move,incorrect_move):
  if player_move==correct_move:
    pass 
  else:
    playsound(sounds[-1])
    time.sleep(1)
    loop_over(sequence='Exitting game...',color=colors[0],delay_time=0.01)
    time.sleep(1)
    sys.exit('')
#Creating loading menu
while True:
  try:
    loop_over(sequence='Loading text based adventure game...\n\t',color=colors[-3],delay_time=0.01)
    time.sleep(1)
    create_progress_bar(sequence=list(range(1,101,1)),bar_colour='YELLOW',number_of_columns=100,description='',delay_time=0.01)
    time.sleep(1)
    print('\n\t')
    time.sleep(1)
    loop_over(sequence='Loading options...\n\t',color=colors[-3],delay_time=0.01)
    create_progress_bar(sequence=list(range(1,101,1)),bar_colour='RED',number_of_columns=100,description='',delay_time=0.01)
    time.sleep(1)
    print('\n\t')
    time.sleep(1)
    loop_over(sequence='Generating Options:\n\t',color=colors[-3],delay_time=0.01)
    print(f'{colors[-1]}')
    time.sleep(1)
    generate_options(number_limit=4,option1='Play',option2='Exit Game',option3='Credits',option4='Tutorial',option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
    time.sleep(1)
    option=int(input('option:'))
    if option==1:
      time.sleep(1)
      player_name=input('player_name:')
      log_player_information(player_information=f'Player Alias:{player_name}\n')
      time.sleep(1)
      loop_over(sequence=f'\nWelcome {player_name} to...\n\t',color=colors[-1],delay_time=0.1)
      time.sleep(1)
      loop_over(sequence=f'{game_title}\n\t',color=random.choice(colors[:-1]),delay_time=0.01)
      time.sleep(1)
      os.system("cls")
      generate_options(number_limit=7,option1=weapons[0],option2=weapons[1],option3=weapons[2],option4=weapons[3],option5=weapons[4],option6=weapons[5],option7=weapons[6],option8=None,option9=None,option10=None)
      time.sleep(1)
      choose_weapon=input('weapon:')
      if choose_weapon not in weapons:
        error_message(text='Please choose the correct option')
      else:
        log_player_information(player_information=f'Player\'s chosen weapon:{choose_weapon}\n')
        player_inventory.append(choose_weapon)
        time.sleep(1)
        loop_over(sequence='Biomes:\n\t',color=colors[1],delay_time=0.1)
        time.sleep(1)
        generate_options(number_limit=4,option1=biomes[0],option2=biomes[1],option3=biomes[2],option4=biomes[3],option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
        time.sleep(1)
        choose_biome=input('biome:')
        if choose_biome in biomes:
          log_player_information(player_information=f'Chosen_biome:{choose_biome}')
          time.sleep(1)
          os.system('cls')
          time.sleep(1)
          loop_over(sequence='Generating World..',color=colors[-1],delay_time=0.01)
          time.sleep(1)
          os.system("cls")
          time.sleep(1)
          if choose_biome==biomes[0]:
           loop_over(sequence='You find yourself in a swirling sandstorm...',color=colors[-1],delay_time=0.01)
           time.sleep(1)
           print('What do you do?')
           time.sleep(1)
           generate_options(number_limit=2,option1='run',option2='hide behind a rock',option3=None,option4=None,option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
          time.sleep(1)
          choose_option=int(input('option:'))
          if choose_option==1:
            print('You attempt to run,in order to escape the sandstorm,but it sweeps you away like nothing..')
            time.sleep(1)
            check_move(player_move=1,correct_move=2,incorrect_move=1)
          elif choose_option==2:
            time.sleep(1)
            loop_over(sequence='The sandstorm clears off...',color=colors[-1],delay_time=0.01)
            time.sleep(1)
            print('\n')
            loop_over(sequence='You are parched but at the same time you are hungry',color=colors[-1],delay_time=0.01)
            time.sleep(1)
            print('Do you find water or food?\n')
            time.sleep(1)
            generate_options(number_limit=2,option1='find water',option2='find food',option3=None,option4=None,option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
            time.sleep(1)
            choose_option=int(input('option:'))
            if choose_option==2:
              check_move(player_move=2,correct_move=1,incorrect_move=2)
            else:
              time.sleep(1)
              loop_over(sequence='After meandering aimlessly in the Vast Desert, you find a cactus',color=colors[-1],delay_time=0.01)
              time.sleep(1)
              print('\n')
              loop_over(sequence='Feeling relieved,you sprint towards it',color=colors[-1],delay_time=0.01)
              time.sleep(1)
              print('\n')
              time.sleep(1)
              loop_over(sequence='You attempt to extract the water that the cactus absorbed',color=colors[-1],delay_time=0.1)
              time.sleep(1)
              loop_over(sequence='As soon as you touch the cactus,it protudes',color=colors[0],delay_time=0.01)
              time.sleep(1)
              loop_over(sequence='It turns out the cactus was actually disguised as a monster',color=colors[-1],delay_time=0.01)
              time.sleep(1)
              print('You consider your options,do you fight or do  you run for it?')
              time.sleep(1)
              generate_options(number_limit=2,option1='fight',option2='run',option3=None,option4=None,option5=None,option6=None,option7=None,option8=None,option9=None,option10=None)
              time.sleep(1)
              choose_option=int(input('option:'))
              if choose_option==1:
                time.sleep(1)
                player_move(player_health=default_health,opponent_health=70,Opponent_class=Cactus_Monster,opponent_alias='the cactus monster',opponent_moves='spikes')
              elif choose_option==2:
                time.sleep(1)
                loop_over(sequence='You attempt to run away from the colossal cactus monster,but its roots capture you')
                time.sleep(1)
                check_move(player_move=choose_option,correct_move=1,incorrect_move=2)
              while choose_option!=1 and choose_option!=2:
                error_message(text='Please choose one of the given options')
                time.sleep(1)
                choose_option=int(input('option:'))
        else:
         error_message(text='Error,invalid biome name has been entered,please try again')
         time.sleep(1)
         choose_biome=input('biome:')
    elif option==2:
      loop_over(sequence='Exitting game...',color=colors[0],delay_time=0.1)
      time.sleep(1)
      sys.exit('')
    elif option==3:
      loop_over(sequence='**Credits**',color=colors[-2],delay_time=0.1)
      time.sleep(1)
      print('\n')
      loop_over(sequence='Creator:Anomalist\n',color=colors[4],delay_time=0.1)
    elif option==4:
      loop_over(sequence='In this game,you are given  a certain amount of options.\nIt is your job to use your wits to pick the correct option.\n\tHowever,if you pick the wrong option,you will inevitably exit the game.\n',delay_time=0.1,color=colors[1])
    else:
      error_message(text='Error,not a valid option please try again')
  except ValueError:
    error_message(text='A ValueError,occurred please try again')