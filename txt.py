#Creating a text-based adventure game in Python 
from colorama import Fore 
import time 
import sys 
import random 
from playsound import playsound  
import os 
import tqdm 
#Fore.RED=red 
#Fore.GREEN=green
#Fore.BLUE=blue
#Fore.YELLOW=yellow
#Fore.MAGENTA=pink
#Fore.LIGHTRED_EX=orange
#Fore.LIGHTMAGENTA_EX=purple
#Fore.BLACK=Gray
#Fore.CYAN=cyan
#Fore.RESET=white
number_range=list(range(1,101,1))
sounds=['desert_wind.mp3','roar.mp3','twig.mp3','wolf.mp3','error.mp3']
Places=['Desert','Artic','Forest','Space']
weapons=['sword','warhammer','shurikens','scythe','spear','katana','sword mace','pistol']
default_health=100
circle_frames=['○',' ○','  ○','    ○','      ○','       ○','        ○','          ○','                ○','                  ○','                           ○']
#weapon damage stats:
sword_damage=30
warhammer_damage=40 
scythe_damage=27
shuriken_damage=18
katana_damage=23 
spear_damage=25
player_inventory=[]
player_attack_power=20
colors=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTRED_EX,Fore.LIGHTMAGENTA_EX,Fore.BLACK,Fore.CYAN,Fore.RESET]
bullet_ascii_art=f'''
       {colors[3]}    /\ 
                     |  |
                     |  |
                     |  |
                     |__| '''
weapons_ascii_art=[f'''        
                 
                      {colors[-3]}__
                     {colors[-3]}/{colors[3]}__{colors[-3]}\ 
                     {colors[-3]}|{colors[3]}__{colors[-3]}|
                     {colors[-3]}|{colors[3]}__{colors[-3]}|
                     {colors[-3]}|{colors[3]}__{colors[-3]}|            
                     {colors[-3]}|{colors[3]}__{colors[-3]}|
                  ___|__|__     
                  \{colors[0]}.{colors[-3]}_{colors[3]}. {colors[0]}.{colors[-3]}_{colors[3]}.{colors[-3]}/
                   {colors[-3]}| | | |
                   |{colors[3]}_{colors[-3]}| |{colors[3]}_{colors[-3]}|
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   |{colors[3]}_{colors[-3]}| |{colors[3]}_{colors[-3]}|
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}| 
                   |{colors[3]}_{colors[-3]}| |{colors[3]}_{colors[-3]}|
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   |{colors[3]}_{colors[-3]}| |{colors[3]}_{colors[-3]}|
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}| | | |
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   |{colors[3]}_{colors[-3]}| |{colors[3]}_{colors[-3]}|
                   {colors[-3]}| | | | 
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}| | | |
                   {colors[-3]}| | | |
                   |{colors[0]}.{colors[-3]}| |{colors[0]}.{colors[-3]}|
                   {colors[-3]}|{colors[3]}_{colors[-3]}| {colors[-3]}|{colors[3]}_{colors[-3]}|
                   {colors[-3]}\ | | /
                   {colors[-3]} \| |/''','''
               ___________________________________________
              /____________________________________/  ____ \\
              |____________________________________| |    ||
              |____________________________________| |    ||
              |____________________________________| |    ||
              |____________________________________| |    ||
              |____________________________________| |____||
              |____________________________________|_______|
                             |___|__\\
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___| 
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|___|
                             |___|__/''',f'''
                                                             {colors[3]}____ 
                                                            {colors[3]}({colors[1]}_<>_{colors[3]})
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                            {colors[3]}|{colors[1]}_<>_{colors[3]}|
                                                          __{colors[3]}|{colors[1]}_<>_{colors[3]}|__
                                                         /  {colors[3]}|{colors[1]}_<>_{colors[3]}|  \\
                                                        |\__________/|
                                                         \__________/
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|    
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}| {colors[-1]}|| {colors[3]}|
                                                            {colors[3]}|   {colors[1]}-{colors[3]}|
                                                            {colors[3]}|   {colors[1]}-{colors[3]}|
                                                            {colors[3]}|   {colors[1]}-{colors[3]}|
                                                            {colors[3]}|    {colors[3]}/
                                                            {colors[3]}| {colors[1]}○ {colors[3]}/
                                                            {colors[3]}|__/
                                                          
                                                           ''','''
                                                           
                                         ____ _____ __ __________________________      
                                        /                                       /
                                       /                                      /
                                      /                            __________/       
                                     /____________________________/
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |   |
                                                   |__/   ''',f''' 
                                                       {colors[0]} 
                                                                    __
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                   |  |
                                                                 __|  |__
                                                                /  _____  \ 
                                                                | |     | |
                                                                | |     | |
                                                                | |     | |
                                                                | |     | |
                                                                | |     | |
                                                                 \|     |/''',f'''                                                                
                                                                                __ __ _
                                                                               <       |   
                                                                                |      |
                                                                                |      |
                                                                                |      |
                                                                                |      |
                                                                                |      |
                                                                                /      | 
                                                                              |__________|
                                                 _________________________ __ /\________/\ __ _______________________/\ 
                                                 |                        |  |____________|  |                        |        
                                                 | ______________________ |  |____________|  | _______________________|
                                                 \/                      \|__|____________|__|/                        
                                                                              \/_________\/        
                                                                               |_________|    
                                                                                 \      |   
                                                                                  |     |
                                                                                  |     |
                                                                                  |     |
                                                                                  |     |  
                                                                                  |     |
                                                                                  |     |
                                                                                  |     |
                                                                                  |_____>
                                                                               ''',f'''
                                                                                             {colors[-3]}_{colors[5]}_{colors[2]}_{colors[-3]}_{colors[5]}_{colors[2]}_{colors[-3]}_{colors[5]}_  
                                                                                            {colors[2]}/ /    \ \  
                                                                                           {colors[5]}/ /{colors[-2]} ____ {colors[5]}\ \  
                                                                                          {colors[-3]}/ / {colors[-2]}/    \ {colors[-3]}\ \  
                                                                                          {colors[2]}| | {colors[-2]}|_   | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}| |  | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| |  |{colors[-3]} | |
                                                                                          {colors[2]}| | {colors[-2]}|_|  | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}|    | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  | {colors[-3]}| | 
                                                                                          {colors[2]}| | {colors[-2]}| {colors[-2]}|  | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}| {colors[-2]}|  | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  | {colors[-3]}| |
                                                                                          {colors[2]}| | {colors[-2]}| {colors[-2]}|  | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}| {colors[-2]}|  | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  | {colors[-3]}| |
                                                                                          {colors[2]}| | {colors[-2]}|    | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}|  {colors[-2]}/|| {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}|  {colors[-2]}\|| {colors[-3]}| |
                                                                                          {colors[2]}| | {colors[-2]}|    | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}| {colors[-2]}|  | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  | {colors[-3]}| |
                                                                                          {colors[2]}| | {colors[-2]}| {colors[-2]}|  | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}| {colors[-2]}|  | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  |{colors[-3]} | |
                                                                                          {colors[2]}| | {colors[-2]}| {colors[-2]}|  | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}|    | {colors[5]}| | 
                                                                                          {colors[-3]}| | {colors[-2]}|    | {colors[-3]}| |
                                                                                          {colors[2]}| | {colors[-2]}|    | {colors[2]}| |
                                                                                          {colors[5]}| | {colors[-2]}|{colors[-2]}_   | {colors[5]}| |
                                                                                          {colors[-3]}| | {colors[-2]}| {colors[-2]}|  | {colors[-3]}| |          
                                                                                          {colors[2]}| | {colors[-2]}| {colors[-2]}|  | {colors[2]}| | 
                                                                                          {colors[5]}| | {colors[-2]}|{colors[-2]}_|  | {colors[5]}| |
                                                                                         {colors[-2]}/||| |    {colors[-2]}||||\  
                                                                                         {colors[-2]}|||| |    {colors[-2]}|||||
                                                                                         {colors[-2]}|||| |    {colors[-2]}||||| 
                                                                                         {colors[-2]}\|\| |    {colors[-2]}||/|/
                                                                                           {colors[-3]}\  \    /  /
                                                                                         {colors[-3]} / /\_\__/_/\ \  
                                                                                         {colors[-3]}| |_|  {colors[-2]}|| {colors[-3]}|_| |
                                                                                         {colors[-3]}\{colors[5]}_{colors[-3]}\_| {colors[5]}-{colors[-2]}||{colors[5]}-{colors[-3]}|_/{colors[2]}_{colors[-3]}/
                                                                                             |{colors[-3]}__{colors[-2]}\/{colors[-3]}_|
                                                                                              {colors[2]}|{colors[-2]}___{colors[2]}| 
                                                                                              {colors[5]}|   {colors[5]}|
                                                                                              {colors[-3]}|   {colors[-3]}|
                                                                                              {colors[2]}|   {colors[2]}|
                                                                                              {colors[5]}|{colors[-2]}___{colors[5]}|                         
                                                                                              {colors[-3]}|   {colors[-3]}|
                                                                                              {colors[2]}|   {colors[2]}|
                                                                                              {colors[5]}|   {colors[5]}|
                                                                                              {colors[-3]}|{colors[-2]}___{colors[-3]}|
                                                                                              {colors[2]}|   |
                                                                                              {colors[5]}|   |
                                                                                              {colors[-3]}|   |
                                                                                              {colors[2]}|{colors[-2]}___{colors[2]}|
                                                                                              {colors[5]}|   |
                                                                                              {colors[-3]}|   |
                                                                                              {colors[2]}|   |
                                                                                              {colors[5]}|{colors[-2]}___{colors[5]}|
                                                                                              {colors[-3]}|   |
                                                                                             {colors[-3]}_{colors[5]}/{colors[5]}_{colors[-3]}_{colors[2]}_{colors[2]}\{colors[-3]}_
                                                                                           {colors[5]}|| |   {colors[2]}| ||
                                                                                           {colors[5]}||{colors[-3]}_{colors[5]}|{colors[-2]}___{colors[2]}|{colors[-3]}_{colors[2]}||
                                                                                              {colors[5]}\{colors[5]}_{colors[-3]}_{colors[2]}_/
                                       '''
                                        ,'''
                                                              _____________________________________________________________
                                                             /           _____________________________________          \  \ 
                                                            /           |                                     |          \  \ 
                                                            |           |                                     |          |  |
                                                            |           |                                     |          |  | 
                                                            |           |                                     |          |  |
                                                            |           |                                     |          |  |
                                                            |___________|_____________________________________|_________/__/
                                                            |             |  |       /  /  /
                                                            |             |  |      /  /  /
                                                            |             |  |     /  /  /
                                                            |             |  |____/  /  /
                                                            |             |  |______/__/ 
                                                            |             |  | 
                                                            |             |  |
                                                            |             |  |
                                                            |             |  |
                                                            \             |  |
                                                             \____________|__|
                                  ''']
line_frames=['''|''','''/''','''-''','''\ '''] 
for num in range(3):
    line_frames.extend(['''|''','''/''','''-''','''\ '''])
else:
    pass
ascii_developing_frames=[f'''{colors[-3]}          
                          _____        
                         |     |  
                         |_____| ''','''
                         ________     
                        |        |
                        |________|''','''
                       ___________
                      |           |
                      |___________|''','''
                     ______________  
                    |              |
                    |______________|''','''
                   _________________ 
                  |                 |
                  |_________________|''','''
                 ____________________  
                |                    |
                |____________________|''','''
                 ____________________      
                |                    |     
                |                    |     
                |                    |     
                |                    |     
                |                    |     
                |                    |     
                |                    |     
                |____________________|                                     ''','''
                
                **********************  
                *                    *  
                *                    *
                *                    *
                *                    *
                *                    *
                *                    *
                *                    *
                *                    *
                **********************                  ''','''
                
                          *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         *
                              ''','''
                
                          * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * *
                              ''','''
                
                          * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * *
                              ''','''
                
                          * * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * * *''','''
                
                          * * * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * * * *''','''
                
                          * * * * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * * * * *''','''
                
                          * * * * * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    * 
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * * * *
            *                         *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        * 
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * * * *
            *                         *                    *
              *                     *
                *                 *
                  *             *
                    *         *
                      *     *                  
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *  
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * * * *
            *                         *                   *
              *                     *                   *
                *                 *
                  *             *
                    *         *
                      *     *                  
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *
               *                    *
             *                        *
           *                            * * * * * * * * * * *
            *                         *                   *
              *                     *                   *
                *                 *                   *
                  *             *                  
                    *         *
                      *     *                  
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *
             *                        *
           *                            * * * * * * * * * * *
            *                         *                   *
              *                     *                   *
                *                 *                   *
                  *             *                   *
                    *         *
                      *     *                  
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *
           *                            * * * * * * * * * * *
            *                         *                   *
              *                     *                   *
                *                 *                   *
                  *             *                   *
                    *         *                   *
                      *     *                  
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                            * * * * * * * * * * *
            *                         *                   *
              *                     *                   *
                *                 *                   *
                  *             *                   *
                    *         *                   *
                      *     *                   *
                         * * * * * * * * * * *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
                                      *                   *
                                    *                   *
                                  *                   *
                                *                   *
                              *                   *
                            *                   *
                      ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
                                  *                   *
                                *                   *
                              *                   *
                            *                   *
                           
                      ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
                                *                   *
                              *                   *
                            *                   *
                          *                   *
                      ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
                              *                   *
                            *                   *
                          *                   *
                        *                   *
                      ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                      ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                         *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                         *                   *
                       *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                         *                   *
                       *                   *
                     *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           *                   *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 *                   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * *                 *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * *                 *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * *                 *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * *                 *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * *               *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * *               *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * *             *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * *             *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * *           *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * *           *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * *         *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * *         *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * *         *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * * *       *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * *       *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * * * *     *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * *     *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * * * *     *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * *   *
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * * * * *   *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * * **
                         *                   *
                       *                   *
                     *                   *
                   *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * * **
                         *                   *
                       *                   *
                     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * * **
                         *                   *
                       *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * * **
                         *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
                           * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
                          *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
                         *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
                        *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
                      *                   *
                       *                   *
         *              *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
                        *                   *
       *              *                   *
        *              *                   *
         *              *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
                          *                   *
      *                 *                   *
       *              *                   *
        *              *                   *
         *              *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                   *
       *                            *                   *
     *                            *                   *
   *                            *                   *
 *                            *                   *
                            *                   *
     *                    *                   *
      *                 *                   *
       *              *                   *
        *              *                   *
         *              *                   *
          *              *                   *
           *              *                   *
            *              * * * * * * * * * **
             *           *                   *
              *        *                   *
               *     *                   *
                *  *                   *
                 * * * * * * * * * * *
                        ''','''
                
                          * * * * * * * * * * *
                       *    *                   *
                     *        *                   *
                   *            *                   *
                 *                *                   *
               *                    *                   *
             *                        *                   *
           *                           * * * * * * * * * * *
         *                            *                    *
       *                            *                    *
     *                            *                    *
   *                            *                    *
    *                          *                   *
     *                       *                   *
      *                    *                   *
       *                 *                   *
        *              *                   *
         *              *                   *
          *              *                   *
           *              *                   *
            *              *                   *
             *              * * * * * * * * * **
              *           *                   *
               *        *                   *
                *     *                   *
                 *  *                   *
                  * * * * * * * * * * *
                        ''',]
missle_frames=[f'''{colors[-3]}
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[0]}\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[-2]}\n\n\n 
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[1]}\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[3]}\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[5]}\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[4]}\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[6]}\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[7]}\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[0]}\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[-3]}\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[-2]}\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[3]}\n\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[2]}\n\n\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[1]}\n\n\n\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[5]}\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''',f'''{colors[-1]}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                 ______
                 \____/
                  /||\ 
                 |    |
                 |    |
                 /    \ 
                 |    |
                 |    |
                  |  |
                   \/''']
scifi_jet_frames=['''
                                __ __
                               /  \  \ 
                               \   \  \  
                            __/ \   \  \__ 
        ____________________\ \__\   \__\ \__________________ 
       /___________________\ \ \  \  /  /\ \__________________\ 
       \                    \ \ \  \/__/\ \ \                  \ 
        \                    \ \_\  \  \ \ \_\                  \ 
         \                    \/_/   \  \ \/_/                   \ 
          \                       \   \  \                        \ 
           \                       \   \  \ 
                                    \___\__\ 
                                    (___)___)         
                                    \     \  \ 
                                     \     \  \ 
                                      \     \  \ 
                                       \     \__\ 
                                        \___ /__/      
                                     ''','''\n\n
                                             __ __
                                            /  \  \ 
                                            \   \  \  
                                         __/ \   \  \__ 
                     ____________________\ \__\   \__\ \__________________ 
                    /___________________\ \ \  \  /  /\ \__________________\ 
                    \                    \ \ \  \/__/\ \ \                  \ 
                     \                    \ \_\  \  \ \ \_\                  \ 
                      \                    \/_/   \  \ \/_/                   \ 
                       \                       \   \  \                        \ 
                        \                       \   \  \ 
                                                 \___\__\ 
                                                 (___)___)         
                                                 \     \  \ 
                                                  \     \  \ 
                                                   \     \  \ 
                                                    \     \__\ 
                                                     \___ /__/             
                                           ''','''\n\n\n
                                                         __ __
                                                        /  \  \ 
                                                        \   \  \  
                                                     __/ \   \  \__ 
                                ___________________\ \__\     \__\ \__________________ 
                                /___________________\ \ \  \  /  /\ \__________________\ 
                                \                    \ \ \  \/__/\ \ \                  \ 
                                 \                    \ \_\  \  \ \ \_\                  \ 
                                  \                    \/_/   \  \ \/_/                   \ 
                                   \                       \   \  \                        \ 
                                    \                       \   \  \ 
                                                             \___\__\ 
                                                             (___)___)         
                                                             \     \  \ 
                                                              \     \  \ 
                                                               \     \  \ 
                                                                \     \__\ 
                                                                 \___ /__/   
                                           
                                    ''','''\n\n\n\n
                                                                      __ __
                                                                     /  \  \ 
                                                                     \   \  \  
                                                                  __/ \   \  \__ 
                                              ____________________\ \__\   \__\ \__________________ 
                                             /___________________\ \ \  \  /  /\ \__________________\ 
                                             \                    \ \ \  \/__/\ \ \                  \ 
                                              \                    \ \_\  \  \ \ \_\                  \ 
                                               \                    \/_/   \  \ \/_/                   \ 
                                                \                       \   \  \                        \ 
                                                 \                       \   \  \ 
                                                                          \___\__\ 
                                                                          (___)___)         
                                                                          \     \  \ 
                                                                           \     \  \ 
                                                                            \     \  \ 
                                                                             \     \__\ 
                                                                              \___ /__/   ''','''\n\n\n\n\n
                                                                              
                                                                                   __ __
                                                                                  /  \  \ 
                                                                                  \   \  \  
                                                                               __/ \   \  \__ 
                                                           ____________________\ \__\   \__\ \__________________ 
                                                          /___________________\ \ \  \  /  /\ \__________________\ 
                                                          \                    \ \ \  \/__/\ \ \                  \ 
                                                           \                    \ \_\  \  \ \ \_\                  \ 
                                                            \                    \/_/   \  \ \/_/                   \ 
                                                             \                       \   \  \                        \ 
                                                              \                       \   \  \ 
                                                                                       \___\__\ 
                                                                                       (___)___)         
                                                                                       \     \  \ 
                                                                                        \     \  \ 
                                                                                         \     \  \ 
                                                                                          \     \__\ 
                                                                                           \___ /__/                                            ''','''\n\n\n\n\n\n
                                                                                             
                                                                                              __ __
                                                                                             /  \  \ 
                                                                                             \   \  \  
                                                                                          __/ \   \  \__ 
                                                                      ____________________\ \__\   \__\ \__________________ 
                                                                     /___________________\ \ \  \  /  /\ \__________________\ 
                                                                     \                    \ \ \  \/__/\ \ \                  \ 
                                                                      \                    \ \_\  \  \ \ \_\                  \ 
                                                                       \                    \/_/   \  \ \/_/                   \ 
                                                                        \                       \   \  \                        \ 
                                                                         \                       \   \  \ 
                                                                                                  \___\__\ 
                                                                                                  (___)___)         
                                                                                                  \     \  \ 
                                                                                                   \     \  \ 
                                                                                                    \     \  \ 
                                                                                                     \     \__\ 
                                                                                                      \___ /__/   ''','''\n\n\n\n\n\n\n
                                                                                                      
                                                                                                              __ __
                                                                                                             /  \  \ 
                                                                                                             \   \  \  
                                                                                                          __/ \   \  \__ 
                                                                                      ____________________\ \__\   \__\ \__________________ 
                                                                                     /___________________\ \ \  \  /  /\ \__________________\ 
                                                                                     \                    \ \ \  \/__/\ \ \                  \ 
                                                                                      \                    \ \_\  \  \ \ \_\                  \ 
                                                                                       \                    \/_/   \  \ \/_/                   \ 
                                                                                        \                       \   \  \                        \ 
                                                                                         \                       \   \  \ 
                                                                                                                  \___\__\ 
                                                                                                                  (___)___)         
                                                                                                                  \     \  \ 
                                                                                                                   \     \  \ 
                                                                                                                    \     \  \ 
                                                                                                                     \     \__\ 
                                                                                                                      \___ /__/                             
                                                                                                      ''','''\n\n\n\n\n\n\n\n
                                                                                                                                 __ __
                                                                                                                                /  \  \ 
                                                                                                                                \   \  \  
                                                                                                                             __/ \   \  \__ 
                                                                                                         ____________________\ \__\   \__\ \__________________ 
                                                                                                        /___________________\ \ \  \  /  /\ \__________________\ 
                                                                                                        \                    \ \ \  \/__/\ \ \                  \ 
                                                                                                         \                    \ \_\  \  \ \ \_\                  \ 
                                                                                                          \                    \/_/   \  \ \/_/                   \ 
                                                                                                           \                       \   \  \                        \ 
                                                                                                            \                       \   \  \ 
                                                                                                                                     \___\__\ 
                                                                                                                                     (___)___)         
                                                                                                                                     \     \  \ 
                                                                                                                                      \     \  \ 
                                                                                                                                       \     \  \ 
                                                                                                                                        \     \__\ 
                                                                                                                                         \___ /__/  
                                                                                                 ''','''\n\n\n\n\n\n\n\n\n
                                                                                                 
                                                                                               __ __
                                                                                              /  \  \ 
                                                                                              \   \  \  
                                                                                           __/ \   \  \__ 
                                                                      ____________________\ \__\    \__\ \__________________ 
                                                                      /___________________ \ \ \ \  /  /\ \__________________\ 
                                                                       \                    \ \ \ \/__/\ \ \                  \ 
                                                                        \                    \ \_\  \  \  \_\                  \ 
                                                                         \                    \/_/   \  \ /_/                   \ 
                                                                          \                       \   \  \                       \ 
                                                                           \                       \   \  \ 
                                                                                                    \___\__\ 
                                                                                                    (___)___)         
                                                                                                    \     \  \ 
                                                                                                     \     \  \ 
                                                                                                      \     \  \ 
                                                                                                       \     \__\ 
                                                                                                        \___ /__/                  
                                                                                                 ''','''\n\n\n\n\n\n\n\n\n\n
                                                                                                 
                                                                                                              __ __
                                                                                                             /  \  \ 
                                                                                                             \   \  \  
                                                                                                          __/ \   \  \__ 
                                                                                      ____________________\ \__\   \__\ \__________________ 
                                                                                     /___________________\ \ \  \  /  /\ \__________________\ 
                                                                                     \                    \ \ \  \/__/\ \ \                  \ 
                                                                                      \                    \ \_\  \  \ \ \_\                  \ 
                                                                                       \                    \/_/   \  \ \/_/                   \ 
                                                                                        \                       \   \  \                        \ 
                                                                                         \                       \   \  \ 
                                                                                                                  \___\__\ 
                                                                                                                  (___)___)         
                                                                                                                  \     \  \ 
                                                                                                                   \     \  \ 
                                                                                                                    \     \  \ 
                                                                                                                     \     \__\ 
                                                                                                                      \___ /__/  
                                                                                                 ''',f'''\n\n\n\n\n\n\n\n\n\n\n
                                                                                                 
                                                            __ __
                                                           /  \  \ 
                                                           \   \  \  
                                                        __/ \   \  \__ 
                                    ____________________\ \__\   \__\ \__________________ 
                                  /___________________\ \ \   \  /  /\ \__________________\ 
                                  \                    \ \ \   \/__/\ \ \                  \ 
                                   \                    \ \_\  \  \  \ \_\                  \ 
                                    \                    \/_/   \  \  \/_/                   \ 
                                     \                       \   \  \                         \ 
                                      \                       \   \  \                         \ 
                                                               \___\__\ 
                                                               (___)___)         
                                                               \     \  \ 
                                                                \     \  \ 
                                                                 \     \  \ 
                                                                  \     \__\ 
                                                                   \___ /__/  
                                                                                                 ''']
#Creating a function that generates options for the user to select 
def generate_options(number_of_options,option1=None,option2=None,option3=None,option4=None,option5=None,option6=None,option7=None,option8=None,option9=None):
    count=0 
    for n in range(1,number_of_options+1,1):
        count+=1
        if n==1:
            loop_over(sequence='________________',color=colors[-2],delay_time=0.01)
            time.sleep(1)
            print(f'\n {count}. {colors[-1]}{option1}')
            time.sleep(1)
            print('\n')
        elif n==2:
            loop_over(sequence='________________',color=colors[5],delay_time=0.01)
            time.sleep(1)
            print(f'\n {count}. {colors[-1]}{option2}')
            time.sleep(1)
            print('\n')
        elif n==3:
            loop_over(sequence='________________',color=colors[6],delay_time=0.01)
            time.sleep(1)
            print(f'\n {count}. {colors[-1]}{option3}')
            time.sleep(1)
            print('\n')
        elif n==4:
            loop_over(sequence='________________',color=colors[0],delay_time=0.01)
            time.sleep(1)
            print(f'\n {count}. {colors[-1]}{option4}')
            time.sleep(1)
            print('\n')
        elif n==5:
            loop_over(sequence='________________',color=colors[1],delay_time=0.01)
            time.sleep(1)
            print(f'\n {count}. {colors[-1]}{option5}')
            time.sleep(1)
            print('\n')
        elif n==6:
            loop_over(sequence='________________',color=colors[7],delay_time=0.01)
            time.sleep(1)
            print(f'\n\t{count}. {colors[-1]}{option6}')
            time.sleep(1)
            print('\n')
        elif n==7:
            loop_over(sequence='________________',color=colors[3],delay_time=0.01)
            time.sleep(1)
            print(f'\n\t{count}. {colors[-1]}{option7}')
            time.sleep(1)
            print('\n')
        elif n==8:
            loop_over(sequence='________________',color=colors[2],delay_time=0.01)
            time.sleep(1)
            print(f'\n\t{count}. {colors[-1]}{option8}')
            time.sleep(1)
            print('\n')
        elif n==9:
            loop_over(sequence='________________',color=colors[-1],delay_time=0.01)
            time.sleep(1)
            print(f'\n\t{count}. {colors[-1]}{option9}')
            time.sleep(1)
            print('\n')
            
#Creating a function that takes in a subscriptable sequence and loops over it,printing it horizontially 
def loop_over(sequence,color,delay_time):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{colors[-1]}')
#Creating a player class to store player stats 
class Player:
    def __init__(self,name,damage_dealt,receive_damage,weapon,health,opponent):
        self.name=name 
        self.damage_dealt=damage_dealt 
        self.receive_damage=receive_damage 
        self.weapon=weapon 
        self.health=health 
        self.opponent=opponent
    def fist_attack(self):
        loop_over(sequence=f'{self.name} punches {self.opponent} with his fist,dealing {self.damage_dealt} points of damage',color=colors[-3],delay_time=0.01)
        
    def kick(self):
        loop_over(sequence=f'{self.name} kicks {self.opponent} dealing {self.damage_dealt} points of damage',color=colors[-3])
        
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
                
    def weapon_assault(self):
     if self.weapon==weapons[0] and self.damage_dealt==sword_damage:
            print(f'You swung your {self.weapon} at {self.opponent} dealing {self.damage_dealt} points of damage.')
     elif self.weapon==weapons[1] and self.damage_dealt==warhammer_damage:
            print(f'You hammered down on {self.opponent}, causing {self.opponent} to lose {self.damage_dealt} points of damage.')
     elif self.weapon==weapons[3] and self.damage_dealt==shuriken_damage:
            print(f'You throw your shurikens at {self.opponent}, dealing {self.damage_dealt} points of damage.')
     elif self.weapon==weapons[4] and self.damage_dealt==scythe_damage:
            print(f'You swing your {self.weapon} at {self.opponent}, dealing {self.damage_dealt} points of damage.')
     elif self.weapon==weapons[5] and self.damage_dealt==spear_damage:
            print(f'You throw your {self.weapon} like a javelin, directly at {self.opponent}, dealing {self.damage_dealt} points of damage.')
     elif self.weapon==weapons[-1] and self.damage_dealt==katana_damage:
            print(f'You wield your dual katana and swing them vertically at {self.opponent}, dealing {self.damage_dealt} points of damage.')

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
boss_battle_title='''                  
 _____        ____  ____  _____    ____   ______   ______   ___      _______
|_____) ____ /___/ /___/ |_____)  /    \\ |______| |______| |   |    | |_____
|_____)|    |\___\ \___\ |_____) /______\\  |  |     |  |   |   |___ | |_____
|_____)|____|/___/ /___/ |_____)/        \\ |__|     |__|   |___|___||_|_____ '''
game_title='''                                                                                                                                                                                                                                                          
           _ _____________   ______________       _______________   __ ______________       _______________           _______________   ___________________ ___
          |_|_|_|_|_|_|_|_| /__/_|_|_|_|_|_|     |_|_|_|_|_|_|_|_| |__|_|_|_|_|_|_|_|      / |_|_|_|_|_|\____\       |_|_|_|_|_|_|_|_| |__|_|_|_|_|_|_|_|_|_|___|
          |_|_|________     |__|_|_|_|_|_|_|     |_|_|_|_|_|_|_|_| |__|_|_|_|_|_|_|_|      | |_|_|_|_|_||____|       |_|_|_|_|_|_|_|_| |__|__|                
          |_|_|_|_|_|_||    |__|_|_|___|_|_|     |_| | | |___| | | |__|__|                 | |_|_|_|_|_||____|       | | | | |___| | | |__|__|__________________
          |_|_|             |__|_|_|_|_|_|_|     |_|_|_|_|_|_|_|_| |__|__|                 | |_|_|_|_|_||____|       |_|_|_|_|_|_|_|_| |__|__|_|_|_|_|_|_|_|_|__|
          |_|_|            /___/_/   \_\\___\\     |_|_|    |_|_|    |__|__|___________      |_|_|_|_|_|_||____|       |_|_|    |_|_|    |__|__|
          |_|_|           /___/_/     \_\\___\\    |_|_|    |_|_|    |__|_|_|_|_|_|_|_|      |_|_|_|_|_|_||____|       |_|_|    |_|_|    |__|__|_____________ ___
          |_|/           /___/_/       \_\\___\\   |_|_|    |_|_|    |__|_|_|_|_|_|_|_|      \_|_|_|_|_|_||____/       |_|_|    |_|_|    |__|__|_|_|_|_|_|_|_|___|'''
creator_title='''



                        ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗██████╗     ██████╗ ██╗   ██╗     █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ██╗     ██╗███████╗████████╗
                        ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗  ██║██╔═══██╗████╗ ████║██╔══██╗██║     ██║██╔════╝╚══██╔══╝
                        ██║     ██████╔╝█████╗  ███████║   ██║   █████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ███████║██╔██╗ ██║██║   ██║██╔████╔██║███████║██║     ██║███████╗   ██║   
                        ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║     ██║╚════██║   ██║   
                        ╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗██████╔╝    ██████╔╝   ██║       ██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗██║███████║   ██║   
                         ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝   
                                                                                                                                                          '''
#Creating a function that takes in parameters/arguments and displays an animation in the output stream 
def create_ascii_animation(frames,delay_time,color):
    for frame in frames:
        #Flushing the output buffer,so that the text appears as soon as possible 
        sys.stdout.flush()
        time.sleep(delay_time)
        os.system('cls')
        if color==None:
         print(f'{frame}')
        else:
            print(f'{color}{frame}')
    else:
        print(f'{colors[-1]}')

create_ascii_animation(frames=line_frames,color=colors[-2],delay_time=0.1)
time.sleep(1)
os.system('cls')
create_ascii_animation(frames=circle_frames,color=colors[1],delay_time=0.1)
time.sleep(1)
os.system('cls')
create_ascii_animation(frames=missle_frames,delay_time=0.01,color=random.choice(colors[0:-1]))
time.sleep(1)
os.system('cls')
create_ascii_animation(frames=ascii_developing_frames,delay_time=0.1,color=None)
time.sleep(1)
os.system('cls')
time.sleep(1)
loop_over(sequence=creator_title,color=colors[-2],delay_time=0.01)
for n in range(100):
 backslash_character=['\n','\b','\t']
 random_backslash_character=random.choice(backslash_character)
 rain_frames=['|',' |','  |','    |','     |','      |','       |','        |','         |','          |','            |','             |         ','           | ','                   |','                      |','                               |','                                       |','                                                     |','                                                                                 |','                                                                              |','                                                                                                |','                                                                                                                 |']
 random_rain_frame=random.choice(rain_frames)
 print(f'{colors[1]}{random_rain_frame}{random_backslash_character}')
 time.sleep(0.01)
else:
    os.system('cls')
    time.sleep(1)
name=input(f'{colors[-3]}name:')
time.sleep(1)
loop_over(sequence=f'\n\n\t welcome {name} to...\n\t',color=colors[-3],delay_time=0.01)
time.sleep(1)
loop_over(sequence=game_title,color=colors[2],delay_time=0.0001)
loop_over(sequence='Loading game...\n\n\t\t',color=colors[-3],delay_time=0.01)
time.sleep(1)
for num in tqdm.tqdm(number_range,ncols=100,colour='CYAN'):
    time.sleep(0.01)
else:
    time.sleep(1)
    loop_over(sequence='\nLoading options...\n\n\t\t',color=colors[-3],delay_time=0.01)
    time.sleep(1)
    for nim in tqdm.tqdm(number_range,ncols=100,colour='YELLOW'):
        time.sleep(0.01)
    else:
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        generate_options(number_of_options=4,option1='play'.title(),option2='tutorial'.title(),option3='credits'.title(),option4='exit game')
        time.sleep(1)
        try:
            input_option=int(input('Enter option:'))
            while input_option!=1 and input_option!=2 and input_option!=3 and  input_option!=4:
                loop_over(sequence=f'{input_option} wasn\'t a valid option,pls try again\n',color=colors[0],delay_time=0.01)
                input_option=int(input('Enter option:'))
            else:
                if input_option==1:
                    time.sleep(1)
                    loop_over(sequence=f'Weapons:\n\t',color=colors[-3],delay_time=0.1)
                    time.sleep(1)
                    generate_options(number_of_options=8,option1=f'{weapons[0]} {weapons_ascii_art[0]}',option2=f'{weapons[1]} {weapons_ascii_art[1]}',option3=f'{weapons[2]} {weapons_ascii_art[5]}',option4=f'{weapons[3]}  {weapons_ascii_art[3]}',option5=f'{weapons[4]} {weapons_ascii_art[4]}',option6=f'{weapons[5]} {weapons_ascii_art[2]}',option7=f'{weapons[6]} {weapons_ascii_art[6]}',option8=f'{weapons[7]} {weapons_ascii_art[7]}')
                    time.sleep(1)
                    choose_weapon=input(f'{colors[-3]}choose weapon:')
                    while choose_weapon not in weapons:
                        loop_over(sequence=f'Error,given weapon was not found in the given weapons_list:{weapons}\nplease try again.\n\n',color=colors[0],delay_time=0.01)
                        time.sleep(1)
                        choose_weapon=input(f'{colors[-3]}choose weapon:')
                    else:
                     loop_over(sequence='Places:',color=colors[-3],delay_time=0.1)
                     generate_options(number_of_options=4,option1=Places[0],option2=Places[1],option3=Places[2],option4=Places[3])
                     time.sleep(1)
                     choose_place=int(input(f'{colors[-3]}select place by number:'))
                    if choose_place==1:
                        time.sleep(1)
                        playsound(sounds[0])
                        loop_over(sequence='You find yourself in a swirling sandstorm...',color=colors[-1],delay_time=0.01)
                        time.sleep(1)
                        print('What do you do?')
                        time.sleep(1)
                        generate_options(number_of_options=2,option1='run',option2='hide behind a rock')
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
                    elif choose_place==4:
                       loop_over(sequence='You find yourself in a space jet...',color=colors[-2],delay_time=0.1)
                       time.sleep(1)
                       os.system('cls')
                       time.sleep(1)
                       create_ascii_animation(frames=scifi_jet_frames,delay_time=0.1,color=colors[-1])
                elif input_option==2:
                    time.sleep(1)
                    loop_over(sequence='In order to play the text based game adventure of Farcore,\nyou need to pick the correct option...',color=colors[1],delay_time=0.1)
                elif input_option==3:
                    time.sleep(1)
                    loop_over(sequence='Credits:Creator of farcore:\nAnomalist',color=colors[4],delay_time=0.1)
                    time.sleep(1)
                elif input_option==4:
                    time.sleep(1)
                    loop_over(sequence='\n\nExitting game...',color=colors[0],delay_time=0.01)
                    time.sleep(1)
                    sys.exit('')
        except ValueError:
            pass
