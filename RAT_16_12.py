import pygame
import sys
#from sys import exit,executable,argv
from random import randint
from MAZE_GENERATION import *
from MAZE_CELLS import *
from Button import *
import time
import os
import ParticleSystem as PS

pygame.init()

RESOLUTION=(1280,720)
Gamescreen=pygame.display.set_mode(RESOLUTION)
Gamescreen.fill('white')
pygame.display.set_caption("Rat in the Maze") #game Caption
clock=pygame.time.Clock() #clock object

RAT=pygame.image.load("Images/rat.png").convert_alpha()
RATPOS=(100,100)
RAT_RECT=RAT.get_rect(midbottom=RATPOS)
RAT_IMAGE="Images/rat.png"
DOWN_IMAGES=("Images/rat.png","Images/rat_DL.png","Images/rat_DR.png","Images/rat_RD.png","Images/rat_LD.png","Images/rat_LEFT.png","Images/rat_RIGHT.png")
UP_IMAGES=()
USERINPUT=""


RATSPEED=15
MOTIONFLIP=3
POS_X=130
POS_Y=230
BGIMG=pygame.image.load("Images/Background.png").convert_alpha()
BGIMG2=pygame.image.load("Images/Background4.png").convert_alpha()
BGIMG3=pygame.image.load("Images/Background5.png").convert_alpha()
CHEESE=pygame.image.load("Images/CHEESECAKE.png").convert_alpha()
GAMESTATE='STARTPAGE'

FPSCOUNTER=0
SPAWNTIME=0

MAZERECT=[]

#variables for intro:-
BGIMG_SA=pygame.image.load("Images/RAT_SA1_EDIT2.png").convert_alpha()

ANYKEYTOSTART=pygame.image.load("Images/START_GAME.png").convert_alpha()
INTRO_ALPHA=1
BGIMG_SA.set_alpha(INTRO_ALPHA)
INTROSPEED_SA=0.5
START_TXT_A=255
START_TXT_A_CTRL=-1


#temperory
'''
grid1=CELL2_7LE_8DE_1(1000,100,Gamescreen)
MAZERECT.extend(grid1.RectVal())


MAZERECT.extend(grid2.RectVal())
'''
MAZEGEN=False


#grid1=RandomMaze(100,200,Gamescreen)
#MAZERECT.extend(grid1.RectVal())

#collision variables:-

UP=1
DOWN=1
LEFT=1
RIGHT=1

UPBLOCK=[]
DOWNBLOCK=[]
LEFTBLOCK=[]
RIGHTBLOCK=[]



#mainmenu button variables:-
EASY=pygame.image.load("Images/EASY.png").convert_alpha()
MEDIUM=pygame.image.load("Images/MEDIUM.png").convert_alpha()
HARD=pygame.image.load("Images/HARD.png").convert_alpha()
DIFFICULTY_BTN=Button(1000,300,EASY,0.1)
DIFFICULTY="EASY"
DIF_BTN_CLICK=False
GAMEMODE=pygame.image.load("Images/GAMEMODE.png").convert_alpha()
GAMEMODE=pygame.transform.scale(GAMEMODE,(int(GAMEMODE.get_width()*0.1),int(GAMEMODE.get_height()*0.1)))



#timer Variables:-
pygame.font.init()
font=pygame.font.SysFont('CopperplatEF Cond',80)
TIMERCANVAS=pygame.image.load("Images/TimerCanvas.png").convert_alpha()
TCOUNTER=30
start=time.ctime()
buffer=start
ZERO=False

#WINSTATE
FINISHLINE=pygame.image.load("Images/FINISHLINE.png").convert_alpha()

FINISH_RECT=FINISHLINE.get_rect()
FINISH_RECT.topleft=(1130,550)

#score variables
SCORE=2000
SHOCK=0
SCADJUSTMENT=False
SCOREDATA=open("SCOREDATA.txt","r")
BESTSCORE=SCOREDATA.read()
SCOREDATA.close()
SCOREDATA=open("SCOREDATA.txt","w")
if(BESTSCORE==""):
    SCOREDATA.write("0")
    SCOREDATA.close()
    SCOREDATA=open("SCOREDATA.txt","w")
    BESTSCORE="0"

#ELEMENTS:-
    #SPEEDBOOST:-
SPEEDBOOST=pygame.image.load("Images/SPEEDBOOST.png").convert_alpha()
SPEEDBOOST_RECT=SPEEDBOOST.get_rect()
SPEEDPOS=((100,200),(310,200),(520,200),(730,200),(940,200),(100,410),(310,410),(520,410),(730,410),(940,410))
SPEEDBOOST_RECT.topleft=random.choice(SPEEDPOS)
SPEEDBOOST.set_alpha(50)
    #RANDOM HIGH RISK HIGH REWARD:-
RANDOMBOX=pygame.image.load("Images/RANDOM.png").convert_alpha()
RANDOMBOX_RECT=RANDOMBOX.get_rect()
RANDOMBOXPOS=((535,290),(605,220),(675,360),(535,430),(605,500),(745,500))
RANDOMBOX_RECT.topleft=random.choice(RANDOMBOXPOS)
RANDOMLUCK=random.choice(((965,465),(130,230),(130,230)))
RANDOMBBOXTRIG=False

#RAT SHOCK
RATSHOCK=False
RATSHOCKCOUNTER=0

#PARTICLE SYSTEM:-
RATDUST=PS.ParticleSystem()
SHOCKWAVE=PS.ParticleSystem()
def difficultySelection():
    global BGIMG
    global DIFFICULTY
    global DIFFICULTY_BTN
    global DIF_BTN_CLICK
    global TCOUNTER
    global SCORE
    match DIFFICULTY:
        case "EASY":
            DIFFICULTY="MEDIUM"
            DIFFICULTY_BTN.__init__(1000,300,MEDIUM,0.1)
            BGIMG=pygame.image.load("Images/Background2.png").convert_alpha()
            TCOUNTER=25
            line.difficulty="MEDIUM"
            SCORE=4000
        case "MEDIUM":
            DIFFICULTY="HARD"
            DIFFICULTY_BTN.__init__(1000,300,HARD,0.1)
            TCOUNTER=22
            BGIMG=pygame.image.load("Images/Background3.png").convert_alpha()
            line.difficulty="HARD"
            SCORE=8000
        case "HARD":
            line.difficulty="EASY"
            DIFFICULTY="EASY"
            DIFFICULTY_BTN.__init__(1000,300,EASY,0.1)
            TCOUNTER=30
            BGIMG=pygame.image.load("Images/Background.png").convert_alpha()
            SCORE=2000
    DIF_BTN_CLICK=True

def electricWave(pos):
    SHOCKWAVE.clear()
    for j in range(0,5):
                
                SHOCKWAVE.add_particle(pos[0],pos[1],2)
def collisionCheck():
    global RIGHT
    global LEFT
    global UP
    global DOWN

    global POS_X
    global POS_Y
    global RATPOS
    global RAT_RECT
    global RIGHTBLOCK
    global LEFTBLOCK
    global UPBLOCK
    global DOWNBLOCK
    global GAMESTATE
    global SCORE
    global RATSPEED
    global RANDOMBBOXTRIG
    global SHOCK
    global RATSHOCK
    for i in MAZERECT:
        if(i.colliderect(RAT_RECT)):
            if(SHOCK<20):
                SHOCK+=1
            RATSHOCK=True

            if(i.center[0]>RAT_RECT.center[0]):                    
                RIGHT=0
                print("RIGHT",i.x,RAT_RECT.x)
                print(RAT)
                                   
                if(len(RIGHTBLOCK)==0):
                    RIGHTBLOCK.append(i)
                if(USERINPUT=="RIGHT"):
                    POS_X-=5
                    electricWave(i.midleft)
            if(i.center[0]<=RAT_RECT.center[0]):
                LEFT=0
                #POS_X+=RATSPEED
                print("LEFT",i.x,RAT_RECT.midbottom[1])
                if(len(LEFTBLOCK)==0):
                    LEFTBLOCK.append(i)
                if(USERINPUT=="LEFT"):
                    POS_X+=5
                    electricWave(i.midright)
            if(i.center[1]<=RAT_RECT.center[1]):
                UP=0
                #POS_Y+=RATSPEED
                print("UP")
                if(len(UPBLOCK)==0):
                    UPBLOCK.append(i)
                if(USERINPUT=="UP"):
                    POS_Y+=5
                    electricWave(i.midbottom)
            if(i.center[1]>=RAT_RECT.center[1]):
                DOWN=0
                print("DOWN")
                #POS_Y-=RATSPEED
                if(len(DOWNBLOCK)==0):
                    DOWNBLOCK.append(i)
                if(USERINPUT=="DOWN"):
                    POS_Y-=5
                    electricWave(i.midtop)
            """        
            if(UP==0 and DOWN==0 and LEFT==0 and RIGHT==0):
                if(RAT_IMAGE in DOWN_IMAGES):
                    if(RAT_IMAGE in ("rat_RIGHT","rat_LEFT")):
                        pass
                    else:
                        DOWN=1
                        POS_Y-=RATSPEED"""
            if(UP==0 and DOWN==0 and LEFT==0 and RIGHT==0):
                if(USERINPUT=="UP"):
                    POS_Y+=RATSPEED
                if(USERINPUT=="DOWN"):
                    POS_Y-=RATSPEED
                if(USERINPUT=="LEFT"):
                    POS_X+=RATSPEED
                if(USERINPUT=="RIGHT"):
                    POS_X-=RATSPEED
                

        elif(i in RIGHTBLOCK):
            RIGHT=1
            RIGHTBLOCK.remove(i)
        elif(i in LEFTBLOCK):
            LEFT=1
            LEFTBLOCK.remove(i)
        elif(i in UPBLOCK):
            UP=1
            UPBLOCK.remove(i)
        elif(i in DOWNBLOCK):
            DOWN=1
            DOWNBLOCK.remove(i)

        if(FINISH_RECT.colliderect(RAT_RECT) and TCOUNTER>=0):
            
            GAMESTATE='WINSTATE'

            
        if(SPEEDBOOST_RECT.colliderect(RAT_RECT)):
            RATSPEED=21
        else:
            RATSPEED=15

        if(RANDOMBOX_RECT.colliderect(RAT_RECT) and RANDOMBBOXTRIG==False and pygame.key.get_pressed()[pygame.K_f]):
            RANDOMBBOXTRIG=True
            
            POS_X=RANDOMLUCK[0]
            POS_Y=RANDOMLUCK[1]
            RATPOS=RANDOMLUCK
            RAT_RECT.midbottom=RATPOS
            
            
        
    




class P_circles:
    def __init__(self,SCREEN):
        self.circle=pygame.image.load("Images/P_CIRCLE.png").convert_alpha()
        self.circle.set_alpha(50)
        self.velocity=(randint(-5,-1),randint(1,5))
        self.RESX=255
        self.RESY=241
        self.TFORMSPEED=randint(5,10)
        self.PX=randint(1,1000)
        self.PY=10
        self.SCREEN=SCREEN
    def Transform(self):
        self.RESX-=self.TFORMSPEED
        self.RESY-=self.TFORMSPEED
            
        if(self.RESY>=10):
            self.circle1=pygame.transform.scale(self.circle,(self.RESX,self.RESY))
        
    def movement(self):
        self.PX+=self.velocity[0]
        self.PY+=self.velocity[1]
        if(self.RESY>=10):
            self.SCREEN.blit(self.circle,(self.PX,self.PY))
        
        



    
def start_animation(key,ALPHA,TXT_A):
    global GAMESTATE
    global INTRO_ALPHA
    global DIF_BTN_CLICK
    
    
    BGIMG_SA.set_alpha(ALPHA)
    Gamescreen.blit(BGIMG_SA,(0,0))
    Gamescreen.blit(GAMEMODE,(890,300))
    if(DIFFICULTY_BTN.draw(Gamescreen)and DIF_BTN_CLICK==False):
            difficultySelection()
    if(pygame.mouse.get_pressed()[0]==0):
            DIF_BTN_CLICK=False
    
    ANYKEYTOSTART.set_alpha(TXT_A)
    Gamescreen.blit(ANYKEYTOSTART,((RESOLUTION[0]/2)-250,RESOLUTION[1]-100))
    if(key[pygame.K_SPACE]):
        INTRO_ALPHA=1
        GAMESTATE="MAINGAME"
    
def RatTrail():
    if(random.randint(0,5)%1==0):
        RATDUST.add_particle(POS_X,POS_Y,1)
    
    




def RatMotion(key):
    global MOTIONFLIP
    global RATPOS
    global POS_X
    global POS_Y
    global RAT
    global RAT_RECT
    global RAT_IMAGE
    global USERINPUT
    global RATSHOCK
    global RATSHOCKCOUNTER
    global RAT_IMAGE


    collisionCheck()
    

    RECTPOS=RAT_RECT.midbottom
    if(not RATSHOCK):
        if((key[pygame.K_UP] or key[pygame.K_w]) and RECTPOS[1]>230 and UP==1):
            if(MOTIONFLIP==1):
                MOTIONFLIP=2
            else:
                MOTIONFLIP=1
            POS_Y-=RATSPEED
            RatTrail()
            RATPOS=(POS_X,POS_Y)
            USERINPUT="UP"
            
        elif((key[pygame.K_DOWN] or key[pygame.K_s]) and RECTPOS[1]<680 and DOWN==1 ):
            if(MOTIONFLIP==4):
                MOTIONFLIP=5
            else:
                MOTIONFLIP=4
            POS_Y+=RATSPEED
            RatTrail()
            MOUSEPOS=(POS_X,POS_Y)
            USERINPUT="DOWN"
        elif((key[pygame.K_RIGHT] or key[pygame.K_d]) and RECTPOS[0]<1200 and RIGHT==1 ):
            if(MOTIONFLIP==7):
                MOTIONFLIP=8
            else:
                MOTIONFLIP=7
            POS_X+=RATSPEED
            RatTrail()
            MOUSEPOS=(POS_X,POS_Y)
            USERINPUT="RIGHT"
        elif((key[pygame.K_LEFT] or key[pygame.K_a]) and RECTPOS[0]>80 and LEFT==1 ):
            if(MOTIONFLIP==10):
                MOTIONFLIP=11
            else:
                MOTIONFLIP=10
            POS_X-=RATSPEED
            RatTrail()
            USERINPUT="LEFT"
        elif(MOTIONFLIP==1 or MOTIONFLIP==2):
            MOTIONFLIP=0
        elif(MOTIONFLIP==4 or MOTIONFLIP==5):
            MOTIONFLIP=3
        elif(MOTIONFLIP==7 or MOTIONFLIP==8):
            MOTIONFLIP=6
        elif(MOTIONFLIP==11 or MOTIONFLIP==10):
            MOTIONFLIP=9

    if(RATSHOCK):
        MOTIONFLIP=12
        RATSHOCKCOUNTER+=1
    
        



    RATPOS=(POS_X,POS_Y)

    
    RAT_RECT.midbottom=RATPOS
    

    match MOTIONFLIP:
          case 0:
              RAT=pygame.image.load("Images/rat_UP.png").convert_alpha()
              RAT_IMAGE="Images/rat_UP.png"
          case 1:
              RAT=pygame.image.load("Images/rat_UL.png").convert_alpha()
              RAT_IMAGE="Images/rat_UL.png"
          case 2:
              RAT=pygame.image.load("Images/rat_UR.png").convert_alpha()
              RAT_IMAGE="Images/rat_UR.png"
          case 3:
              RAT=pygame.image.load("Images/rat.png").convert_alpha()
              RAT_IMAGE="Images/rat.png"
          case 4:
              RAT=pygame.image.load("Images/rat_DL.png").convert_alpha()
              RAT_IMAGE="Images/rat_DL.png"
          case 5:
              RAT=pygame.image.load("Images/rat_DR.png").convert_alpha()
              RAT_IMAGE="Images/rat_DR.png"
          case 6:
              RAT=pygame.image.load("Images/rat_RIGHT.png").convert_alpha()
              RAT_IMAGE="Images/rat_RIGHT.png"
          case 7:
              RAT=pygame.image.load("Images/rat_RD.png").convert_alpha()
              RAT_IMAGE="Images/rat_RD.png"
          case 8:
              RAT=pygame.image.load("Images/rat_RU.png").convert_alpha()
              RAT_IMAGE="Images/rat_RU.png"
          case 9:
              RAT=pygame.image.load("Images/rat_LEFT.png").convert_alpha()
              RAT_IMAGE="Images/rat_LEFT.png"
          case 10:
              RAT=pygame.image.load("Images/rat_LD.png").convert_alpha()
              RAT_IMAGE="Images/rat_LD.png"
          case 11:
              RAT=pygame.image.load("Images/rat_LU.png").convert_alpha()
              RAT_IMAGE="Images/rat_LU.png"
        
          case 12:
              if(RAT_IMAGE=="Images/RAT_SHOCKED.PNG"):
                      
                  RAT_IMAGE="Images/RAT.PNG"
                  RAT=pygame.image.load(RAT_IMAGE).convert_alpha()
              else:
                  RAT_IMAGE="Images/RAT_SHOCKED.PNG"
                  RAT=pygame.image.load(RAT_IMAGE).convert_alpha()
                      
              if(RATSHOCKCOUNTER==5):
                  RATSHOCKCOUNTER=0
                  MOTIONFLIP=3
                  RATSHOCK=False
          
          
          
          
          
          
          
          
      
    #pygame.time.delay(120) # delay otherwise mouse goes brrrru
              #but time .delay cause fps drop   

        

def MAINGAME_1(alpha):
    global MAZEGEN
    global GRID1
    global GRID2
    global GRID3
    global GRID4
    global GRID5
    global GRID6
    global GRID7
    global GRID8
    global GRID9
    global GRID10
    global MAZERECT
    global SCORE
    BGIMG.set_alpha(alpha)
    Gamescreen.blit(BGIMG,(0,0))
    if(alpha>100):
        match DIFFICULTY:
            case "EASY":
                RATDUST.draw(Gamescreen,(255,217,67))
            case "MEDIUM":
                RATDUST.draw(Gamescreen,(45,70,161))
            case "HARD":
                RATDUST.draw(Gamescreen,(67,48,74))

        if(RATSHOCK):
            match DIFFICULTY:
                case "EASY":
                    SHOCKWAVE.draw(Gamescreen,(255,254,145))
                case "MEDIUM":
                    SHOCKWAVE.draw(Gamescreen,(146,255,255))
                case "HARD":
                    SHOCKWAVE.draw(Gamescreen,(255,163,18))
            SHOCKWAVE.update()
                
        RATDUST.update()        
        #SCORE-=3
        #print(SCORE)#score
        Gamescreen.blit(RAT,RAT_RECT)
        #pygame.draw.rect(Gamescreen,(100,0,0),RAT_RECT,2)
        TIMERCANVAS.blit(Gamescreen,(0,0))
        if(MAZEGEN==False):
            MAZELIST=RandomMaze(100,200,Gamescreen)    
            GRID1=MAZELIST[0]
            GRID2=MAZELIST[1]
            GRID3=MAZELIST[2]
            GRID4=MAZELIST[3]
            GRID5=MAZELIST[4]
            GRID6=MAZELIST[5]
            GRID7=MAZELIST[6]
            GRID8=MAZELIST[7]
            GRID9=MAZELIST[8]
            GRID10=MAZELIST[9]
            MAZERECT.extend(GRID1.RectVal())
            MAZERECT.extend(GRID2.RectVal())
            MAZERECT.extend(GRID3.RectVal())
            MAZERECT.extend(GRID4.RectVal())
            MAZERECT.extend(GRID5.RectVal())
            MAZERECT.extend(GRID6.RectVal())
            MAZERECT.extend(GRID7.RectVal())
            MAZERECT.extend(GRID8.RectVal())
            MAZERECT.extend(GRID9.RectVal())
            MAZERECT.extend(GRID10.RectVal())
            MAZEGEN=True
        Gamescreen.blit(CHEESE,(1130,560))#cheese image
        Gamescreen.blit(FINISHLINE,FINISH_RECT) #finishline invisible box
        Gamescreen.blit(SPEEDBOOST,SPEEDBOOST_RECT) #speedboost blit
        if(RANDOMBBOXTRIG==False):
            
            Gamescreen.blit(RANDOMBOX,RANDOMBOX_RECT)
        #pygame.draw.rect(Gamescreen,(0,255,0),FINISH_RECT,2)
        GRID1.display()
        GRID2.display()
        GRID3.display()
        GRID4.display()
        GRID5.display()
        GRID6.display()
        GRID7.display()
        GRID8.display()
        GRID9.display()
        GRID10.display()
        
        #code for timer:-
        
        global start
        global buffer
        global ZERO
        global TCOUNTER
        t=time.ctime()
        if(time.ctime()[17:19]!=buffer[17:19] and ZERO==False):
            buffer=time.ctime()
            print(TCOUNTER)
            RANDOMBOX.set_alpha(random.randint(180,255))
            TCOUNTER-=1
            if(TCOUNTER<=10):               
                Gamescreen.blit(font.render(str(TCOUNTER),False,(random.randint(180,250),0,0)),(640,50))
                
            else:
                Gamescreen.blit(font.render(str(TCOUNTER),False,(255,255,255)),(1100,50))
                
        else:
            if(TCOUNTER<=10):
                Gamescreen.blit(font.render(str(TCOUNTER),False,(random.randint(180,250),0,0)),(640,50))
            else:
                Gamescreen.blit(font.render(str(TCOUNTER),False,(255,255,255)),(1100,50))
            
        if(TCOUNTER==0):
            ZERO=True
            Gamescreen.blit(font.render(str(TCOUNTER),False,(250,0,0)),(640,50))

       
            
        
P=P_circles(Gamescreen)
  

while True:
            
    pygame.display.update()
    keys=pygame.key.get_pressed()
    for events in pygame.event.get():
        if(events.type==pygame.QUIT):
            SCOREDATA.write(str(BESTSCORE))
            SCOREDATA.close()
            pygame.quit()
            exit()

    match GAMESTATE:
        case 'STARTPAGE':
            if(INTRO_ALPHA<255):
                INTRO_ALPHA+=INTROSPEED_SA                
            if(START_TXT_A<=0):
                START_TXT_A_CTRL=1
            if(START_TXT_A>=255):
                START_TXT_A_CTRL=-1

            
            
              
            START_TXT_A+=(3*START_TXT_A_CTRL)
                
            start_animation(keys,INTRO_ALPHA,START_TXT_A)
            SPAWNTIME+=clock.get_rawtime()
            if(SPAWNTIME>=10):
                P.Transform()
                P.movement()
                SPAWNTIME=0

            
        case 'MAINGAME':
                  
            
            
                   
            


            
            if(INTRO_ALPHA<255): #reused intro alpha for maingame
                INTRO_ALPHA+=INTROSPEED_SA
            FPSCOUNTER+=1
            if(FPSCOUNTER>=10): #for calling rat motion every x frames
                RatMotion(keys)
                FPSCOUNTER=0
            MAINGAME_1(INTRO_ALPHA)
            if(TCOUNTER==0):
                GAMESTATE='GAMEOVER'
                FPSCOUNTER=0
            
        case 'GAMEOVER':
            FPSCOUNTER+=1
            SCORE=round(-((((POS_X-1130)**2)+((POS_Y-550)**2))**(1/2))+1050)
            Gamescreen.blit(BGIMG2,(0,0))
            Gamescreen.blit(font.render("SCORE   :   "+str(SCORE),False,(250,250,250)),(420,50))
            if(FPSCOUNTER>=180):
                SCOREDATA.close()
                os.execvp("python", ['python']+["RAT_16_12.py"])
                
                
                #pygame.quit()
                #exit()
        case 'WINSTATE':
            FPSCOUNTER+=1
            Gamescreen.blit(BGIMG3,(0,0))
            if(SCADJUSTMENT==False):
                SCADJUSTMENT=True
                SCORE=SCORE+(200*TCOUNTER)-(100*SHOCK)
            
            if(SCORE>=int(BESTSCORE)):
                Gamescreen.blit(font.render("SCORE   :   "+str(SCORE)+"  NEW BEST !!",False,(random.randint(1,250),random.randint(1,250),random.randint(1,250))),(220,50))
                
            else:
                Gamescreen.blit(font.render("SCORE   :   "+str(SCORE),False,(250,250,250)),(420,50))
                
                
            
            if(FPSCOUNTER>=180):
                if(SCORE>=int(BESTSCORE)):
                    SCOREDATA.write(str(SCORE))
                SCOREDATA.close()
                os.execvp("python", ['python']+["RAT_16_12.py"])
                
                #pygame.quit()
                #exit()
            
    #print(clock.get_fps())   
    clock.tick(60)


    
    
    
    
