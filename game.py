import pygame
from rat import Rat,Cheese
from maze import Wall,Cell,WallType,Maze
from utilities import Button
from enum import Enum

class GameModeType(Enum):
    MENU = 0
    GAME = 1
    GAMEOVER = 2

class GameDifficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2
    NIGHTMARE = 3

class GameMode:
    def __init__(self,game):
        self.game = game
    
    def update(self,dt):
        pass
    def render(self,canvas,dt):
        pass

class GameModeMenu(GameMode):
    def __init__(self,game):
        super().__init__(game)

        #Main Menu
        self.play_button = Button("Play",(600,250))
        self.customize_button = Button("Customize",(600,300))
        self.quit_button = Button("Quit Game",(600,350),hovered_color = (200,0,0))

        
        
        #Difficulty menu
        self.font = pygame.font.Font(None,36)
        self.under_difficulty_menu = False
        self.difficulty_text = self.font.render("Difficulty",True,(200,200,200))

        self.back_button = Button("Back",(600,600))
        self.easy_button = Button("Easy",(100,250))
        self.medium_button = Button("Medium",(100,300))
        self.hard_button = Button("Hard",(100,350))
        self.nightmare_button = Button("Nightmare",(100,400),hovered_color = (255,0,0))

        self.back_button.hide_button()
        self.easy_button.hide_button()
        self.medium_button.hide_button()
        self.hard_button.hide_button()
        self.nightmare_button.hide_button()


    def quit_game(self):
        self.game.close_game()

    def select_difficulty(self):
        self.under_difficulty_menu = True
        self.play_button.hide_button()
        self.customize_button.hide_button()
        self.quit_button.hide_button()

        self.back_button.show_button()
        self.easy_button.show_button()
        self.medium_button.show_button()
        self.hard_button.show_button()
        self.nightmare_button.show_button()


        
    def back_to_main_menu(self):
        self.under_difficulty_menu = False 
        self.play_button.show_button()
        self.customize_button.show_button()
        self.quit_button.show_button()
        self.back_button.hide_button()
        

        self.back_button.hide_button()
        self.easy_button.hide_button()
        self.medium_button.hide_button()
        self.hard_button.hide_button()
        self.nightmare_button.hide_button()

    def create_game(self,difficulty:GameDifficulty):
        self.back_to_main_menu()
        self.game.CreateGame(difficulty)

    def update(self,dt):
            
        self.play_button.on_hovered()
        self.customize_button.on_hovered()
        self.quit_button.on_hovered()
        self.back_button.on_hovered()

        self.easy_button.on_hovered()
        self.medium_button.on_hovered()
        self.hard_button.on_hovered()
        self.nightmare_button.on_hovered()




        self.play_button.on_pressed(self.select_difficulty)
        # self.play_button.on_pressed(self.game.CreateGame,[GameDifficulty.MEDIUM])
        self.quit_button.on_pressed(self.quit_game)
        self.back_button.on_pressed(self.back_to_main_menu)

        self.easy_button.on_pressed(self.create_game,[GameDifficulty.EASY])
        self.medium_button.on_pressed(self.create_game,[GameDifficulty.MEDIUM])
        self.hard_button.on_pressed(self.create_game,[GameDifficulty.HARD])
        self.nightmare_button.on_pressed(self.create_game,[GameDifficulty.NIGHTMARE])
        

    
    def render(self,canvas,dt):
        if(self.under_difficulty_menu):
            canvas.blit(self.difficulty_text,(200,200))

        self.play_button.render(canvas,dt)
        self.customize_button.render(canvas,dt)
        self.quit_button.render(canvas,dt)
        self.back_button.render(canvas,dt)

        self.easy_button.render(canvas,dt)
        self.medium_button.render(canvas,dt)
        self.hard_button.render(canvas,dt)
        self.nightmare_button.render(canvas,dt)

        self.game.set_camera_offset((0,0))


class GameModeGame(GameMode):

    def __init__(self,game,difficulty:GameDifficulty):
        super().__init__(game)
        self.player = Rat()
        match difficulty:
            case GameDifficulty.EASY:
                self.maze = Maze((100,100),(8,12),WallType.WALL3)
            case GameDifficulty.MEDIUM:
                self.maze = Maze((100,100),(10,15),WallType.WALL1)
            case GameDifficulty.HARD:
                self.maze = Maze((100,100),(16,15),WallType.WALL2)
            case GameDifficulty.NIGHTMARE:
                self.maze = Maze((100,100),(10,15),WallType.WALL2)
            case _:
                self.maze = Maze((100,100),(8,12),WallType.WALL3)


        self.wall_list = self.maze.get_wall_list()
        self.collision_manager = CollisionManager(self.player,self.wall_list)
        self.player_controller = PlayerController(self.player)
        last_wall =  self.wall_list[-1]

        self.cheese_pos = (last_wall.pos_x + (last_wall.rect.width ),last_wall.pos_y - (last_wall.rect.width/1.25))
        # self.cheese_pos = (last_wall.pos_x,last_wall.pos_y)
        self.cheese = Cheese(self,self.cheese_pos)
        self.collision_manager.add_object(self.cheese)

        #end game
        self.game_ended = False
        self.game_end_time = 0


        
    def handle_input(self,dt):
        
        keys = pygame.key.get_pressed()

        player_moving = False

        if(not self.collision_manager.check_wall_collisions()):
            self.player.reset_movement()
    
        if(keys[pygame.K_w]):
            self.player_controller.w_command.execute(dt)
            player_moving = True
        if(keys[pygame.K_a]):
            self.player_controller.a_command.execute(dt)
            player_moving = True
        if(keys[pygame.K_s]):
            self.player_controller.s_command.execute(dt)
            player_moving = True
        if(keys[pygame.K_d]):
            self.player_controller.d_command.execute(dt)
            player_moving = True

        if(not player_moving):
            self.player_controller.stop_player()

    def update(self,dt):

        if(self.game_ended):
            self.game_end_time += dt
        if(self.game_end_time >=5):
            self.game.end_game()

        self.handle_input(dt)
        self.player.update(dt)
        self.cheese.update(dt)


    def render(self,canvas,dt):
        self.player.render(canvas)
        self.maze.render(canvas,dt)
        self.cheese.render(canvas) 
        offset = self.calculate_camera_offset()
        self.game.set_camera_offset(offset)

    def end_game(self):
        self.player.move_by_AI()
        self.game_ended = True


    def calculate_camera_offset(self):
        
        x = 0
        y = 0

        if(self.player.posx > self.game.screen_dim[0]-100):
            x = -(self.player.posx - (self.game.screen_dim[0] - 100))
        if(self.player.posy > self.game.screen_dim[1]-100):
            y = -(self.player.posy - (self.game.screen_dim[1] - 100))

        return (x,y)


class CollisionManager:
    def __init__(self,player,walls:pygame.sprite.Sprite=[],objects:pygame.sprite.Sprite=[]):
    
        self.player = player
        self.walls = walls
        
        self.wall_collision_list=[False for i in self.walls]
        self.obj =[]

    def check_wall_collisions(self)->bool:

        rects = []
        collision = False
        for i in range(0,len(self.walls)):
            if(self.player.rect.colliderect(self.walls[i].rect)):
                self.wall_collision_list[i] = True
                rects.append(self.walls[i].rect)
                collision = True
            else:
                self.wall_collision_list[i] = False

        self.player.collide_walls(rects)

        for i in self.obj:
            if(i.get_rect().colliderect(self.player.rect)):
                i.handle_collision()
        
        return collision

    def add_object(self,obj):
        self.obj.append(obj)






class Command:
    def __init__(self):
        pass

    def execute(self,object,dt):
        pass

class MoveCommand(Command):

    def __init__(self,character=None,dirn = (0,0)):
        super().__init__()
        self.dirn = dirn
        self.character = character

    def execute(self,dt,player=None):
        if(player):
            player.move(dt,self.dirn)
        elif(self.character):
            self.character.move(dt,self.dirn)
        else:
            print("No character to move")


class PlayerController:
    
    def __init__(self,player):
        self.player = player
        
        self.w_command = MoveCommand(player,(0,-1))
        self.a_command = MoveCommand(player,(-1,0))
        self.s_command = MoveCommand(player,(0,1))
        self.d_command = MoveCommand(player,(1,0))

    def stop_player(self):
        self.player.stop()


class Game:

    def __init__(self):
        
        pygame.init()
        pygame.display.init()
        pygame.font.init()

        self.running = True
        self.screen_dim = (1280,720)
        self.screen = pygame.display.set_mode(self.screen_dim)
       
        self.canvas = pygame.Surface((1500,3000))
        self.clock = pygame.time.Clock()
        
        self.game_mode_menu : GameMode = GameModeMenu(self) 
        self.game_mode_game : GameMode = None
        self.game_mode = self.game_mode_menu 

        self.camera_offset_x = 0
        self.camera_offset_y = 0

        

        self.dt = 0


    def set_camera_offset(self,offset):
        self.camera_offset_x,self.camera_offset_y = offset[0],offset[1]


    def CreateGame(self,difficulty:GameDifficulty):
        self.game_mode_game = GameModeGame(self,difficulty)
        self.change_game_mode(GameModeType.GAME)

    def end_game(self):
        self.game_mode_game = None
        self.change_game_mode(GameModeType.MENU)

    def change_game_mode(self,mode:GameModeType):
        
        match mode:
            case GameModeType.MENU:
                self.game_mode = self.game_mode_menu
            case GameModeType.GAME:
                if(self.game_mode_game):
                    self.game_mode = self.game_mode_game
                else:
                    self.game_mode = self.game_mode_menu
                    print("error creating game")

            case GameModeType.GAMEOVER:
                print("GameOver")
            case _:
                print("Invalid")
        

    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

        pygame.event.clear()
        
    
    def update(self):
        self.handle_input()
        self.game_mode.update(self.dt)
        
        

    
    def render(self):
        
        self.canvas.fill("black")
        self.game_mode.render(self.canvas,self.dt)
        self.screen.blit(self.canvas,(0 + self.camera_offset_x,0 + self.camera_offset_y ))

        pygame.display.flip()


    def loop(self):
        
        while(self.running):
            self.update()
            self.render()
            self.dt = self.clock.tick(60) / 1000
            

    def close_game(self):
        pygame.quit()
        exit(0)