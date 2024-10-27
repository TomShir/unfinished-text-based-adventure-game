import logging 
import random 
from ascii_art import *
import tqdm
number_range=list(range(1,101,1))
#Creating a logger to store crucial player information 
def user_logger(player_info):
    mylogger=logging.getLogger("Player_logger")
    mylogger.setLevel(logging.INFO)
    file_handler=logging.FileHandler("player_info.log")
    logging_format=logging.Formatter("%(asctime)s-%(name)s-%(message)s")
    file_handler.setFormatter(logging_format)
    mylogger.addHandler(file_handler)
    mylogger.info(player_info)

weapons=['scythe','katana','hammer','shurikens','nunchucks','spear']
scythe_damage=40 
katana_damage=50 
hammer_damage=30 
shurikens_damage=50 
nunchucks=50 
spear=20 
#Creating a class to store player stats 
class Player:
    def __init__(self,name,damage_dealt,receive_damage,weapon,health,opponent):
        self.name=name 
        self.damage_dealt=damage_dealt 
        self.receive_damage=receive_damage 
        self.weapon=weapon 
        self.health=health 
        self.opponent=opponent
    def damage_taken(self):
        loop_over(sequence=f'{self.name} has taken damage from {self.opponent}',color=colors[-3],delay_time=0.01)
        if self.health-self.receive_damage>=50 and self.receive_damage<=100:
            for num in tqdm.tqdm(number_range,colour='GREEN',ncols=100,desc='health'):
                time.sleep(0.01)
                if num==self.health-self.receive_damage:
                    break 
                else:
                    pass 
            else:
                loop_over(sequence=f'{self.name} now currently has {self.health} points of health.',color=colors[-3])
        elif self.health-self.receive_damage<=50 and self.receive_damage>=30:
            for x in tqdm.tqdm(number_range,colour='YELLOW',ncols=100,desc='health'):
                time.sleep(0.01)
                if x==self.health-self.receive_damage:
                    break 
                else:
                   pass 
            else:
                loop_over(sequence=f'{self.name} now currently has {self.health} points of health.',color=colors[-3])
        elif self.health-self.receive_damage<=30:
            for s in tqdm.tqdm(number_range,colour='RED',ncols=100,desc='health'):
                time.sleep(0.01)
                if s==self.health-self.receive_damage:
                    break 
                else:
                    pass 
            else:
                time.sleep(1)
                loop_over(sequence=f'{self.name} now currently has {self.health} points of health.',color=colors[-3])
    
    def game_over(self):
        if self.health==0:
            loop_over(sequence="game over".upper(),color=colors[1],delay_time=1)
        else:
            pass 
    
    def weapon_assault(self):
        if self.weapon==weapons[0]:
create_ascii_animation(frames=line_frames,frame_speed=0.1,frame_colour=colors[4])
time.sleep(1)
os.system("cls")
time.sleep(1)
enter_name=input("Enter name:")
user_logger(player_info=f"Player name:{enter_name}" )
time.sleep(1)
loop_over(sequence="\t\n{player_name} welcome to...".format(player_name=enter_name),color=colors[2],delay_time=0.1)
time.sleep(1)
os.system("cls")
loop_over(sequence=game_ascii_title,color=colors[5],delay_time=0.001)
