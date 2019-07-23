''' Name: Yuanxin Xue

    Date: May 7, 2015
    
    Description: This program contains the sprites needed for a Brawl of the 
    Kirbys fighting game.
'''

import pygame
pygame.init()
pygame.mixer.init()

class Kirby(pygame.sprite.Sprite):
    '''This class defines the sprite for a Kirby character.'''
    
    def __init__(self,twin):
        '''This initializer method accepts a integer argument that determines 
        which Twin Kirby (Red or Blue). Many of Kirby's conditional and 
        directional attributes, e.g dx and dy, basic and special damage, frame, 
        moving and in air conditions are also set. On top of that, it also loads 
        the Kirby images and sets up rect attribute and image attribute.'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)     
        
        # Create a basic and special damage, directional and conditional variables
        self.__time = 0
        self.__frame = 0
        self.__basic_damage = 10
        self.__special_damage = 30
        self.__attacking = False
        self.__moving = False
        self.__in_air = False
        self.__dx = 0
        self.__dy = -4
        self.__state = ''
        self.__jumps_left = 4
        if twin == 1:
            self.__twin = '_Twin1'
        else:
            self.__twin = '_Twin2'
        
        # Create sound effect objects
        self.__hurt_sound = pygame.mixer.Sound("./soundEffects/Kirby_Hurt.wav")
        self.__hurt_sound.set_volume(0.2)    
        
        self.__jump_sound = pygame.mixer.Sound("./soundEffects/Kirby_Jump.wav")
        self.__jump_sound.set_volume(0.5)    
        
        self.__punch_sound = pygame.mixer.Sound("./soundEffects/Kirby_Punch.wav")
        self.__punch_sound.set_volume(0.1)    
        
        self.__moving_punch_sound = pygame.mixer.Sound("./soundEffects/Kirby_Moving_Punch.wav")
        self.__moving_punch_sound.set_volume(0.5) 
        
        
        # LOAD AND SET UP KIRBY IMAGES
        # Load and set up Kirby Idle images
        self.__rightidle_image = pygame.image.load('./kirbyIdle/kirby_idle_right'+self.__twin+'.gif')
        self.__rightidle_image = self.__rightidle_image.convert()
        self.__rightidle_image.set_colorkey((255,255,255))
                
        self.__leftidle_image = pygame.image.load('./kirbyIdle/kirby_idle_left'+self.__twin+'.gif')
        self.__leftidle_image = self.__leftidle_image.convert()
        self.__leftidle_image.set_colorkey((255,255,255))        
                
        
        # Load and set up Kirby Walking images
        self.__leftwalk_images = []
        self.__rightwalk_images = []
        
        for images in range(1,9):
            self.__leftwalk_frame = pygame.image.load('./kirbyWalk./LeftWalk'+self.__twin+'/kirby_leftwalk_'+ str(images)+'.gif')
            self.__rightwalk_frame = pygame.image.load('./kirbyWalk./RightWalk'+self.__twin+'/kirby_rightwalk_'+ str(images)+'.gif')
            
            self.__leftwalk_frame = self.__leftwalk_frame.convert()
            self.__leftwalk_frame.set_colorkey((255,255,255))
            
            self.__rightwalk_frame = self.__rightwalk_frame.convert()
            self.__rightwalk_frame.set_colorkey((255,255,255))
            
            self.__leftwalk_images.append(self.__leftwalk_frame)
            self.__rightwalk_images.append(self.__rightwalk_frame)
           
            
            
        # Load and set up Kirby Jumping images 
        self.__leftjump_images = []
        self.__rightjump_images = []
        
        for images in range(1,5):
            self.__leftjump_frame = pygame.image.load('./kirbyJumpand\
Fall./LeftJump'+self.__twin+'/kirby_leftjump_'+ str(images)+'.gif')
            self.__rightjump_frame = pygame.image.load('./kirbyJumpand\
Fall./RightJump'+self.__twin+'/kirby_rightjump_'+ str(images)+'.gif')
            
            self.__leftjump_frame = self.__leftjump_frame.convert()
            self.__rightjump_frame = self.__rightjump_frame.convert()
            
            self.__leftjump_frame.set_colorkey((255,255,255))
            self.__rightjump_frame.set_colorkey((255,255,255))
            
            self.__leftjump_images.append(self.__leftjump_frame)
            self.__rightjump_images.append(self.__rightjump_frame)
            
            
            
        # Load and set up Kirby falling images
        self.__leftfall_image = pygame.image.load('./kirbyJumpandFall./Left\
Jump'+self.__twin+'/kirby_leftjump_5.gif')  
        self.__rightfall_image = pygame.image.load('./kirbyJumpandFall./Right\
Jump'+self.__twin+'/kirby_rightjump_5.gif')
        
        self.__leftfall_image = self.__leftfall_image.convert()
        self.__rightfall_image = self.__rightfall_image.convert()
        
        self.__leftfall_image.set_colorkey((255,255,255))
        self.__rightfall_image.set_colorkey((255,255,255))
        
        
        
        # Load and set up Kirby Stationary Basic Attack images
        self.__leftbasic_images = []
        self.__rightbasic_images = []
                
        for images in range(1,7):
            self.__leftbasic_frame = pygame.image.load('./kirbyBasicAttack\
Stationary./BasicAttackLeft'+self.__twin+'/kirby_leftbasic_attack_'+ str(images)+'.gif')        
            self.__rightbasic_frame = pygame.image.load('./kirbyBasicAttack\
Stationary./BasicAttackRight'+self.__twin+'/kirby_rightbasic_attack_'+ str(images)+'.gif')
            
            self.__leftbasic_frame = self.__leftbasic_frame.convert()
            self.__rightbasic_frame = self.__rightbasic_frame.convert()
            
            self.__leftbasic_frame.set_colorkey((255,255,255))
            self.__rightbasic_frame.set_colorkey((255,255,255))     
            
            self.__leftbasic_images.append(self.__leftbasic_frame)
            self.__rightbasic_images.append(self.__rightbasic_frame)  
            
            
            
        # Load and set up Kirby Horizontally Moving Basic images
        self.__leftbasic_moving_images = []
        self.__rightbasic_moving_images = []
         
        for images in range(1,9):
            self.__leftbasic_moving_frame = pygame.image.load('./kirbyBasicAttack\
Horizontal./BasicMovingLeftAttack'+self.__twin+'/kirby_leftbasic_attack_'+ str(images)+'.gif')            
            self.__rightbasic_moving_frame = pygame.image.load('./kirbyBasicAttack\
Horizontal./BasicMovingRightAttack'+self.__twin+'/kirby_rightbasic_attack_'+ str(images)+'.gif')
            
            self.__leftbasic_moving_frame = self.__leftbasic_moving_frame.convert()
            self.__rightbasic_moving_frame = self.__rightbasic_moving_frame.convert()
            
            self.__leftbasic_moving_frame.set_colorkey((255,255,255))
            self.__rightbasic_moving_frame.set_colorkey((255,255,255))            
            
            self.__leftbasic_moving_images.append(self.__leftbasic_moving_frame)
            self.__rightbasic_moving_images.append(self.__rightbasic_moving_frame) 
        
        
            
        #Load and set up Kirby Stationary Special Attack images
        self.__special_images = []
        
        for images in range(1,6):
            self.__special_frame = pygame.image.load('./kirbySpecialAttack\
./SpecialAttack'+self.__twin+'/kirby_special_'+ str(images)+'.gif')
            
            self.__special_frame = self.__special_frame.convert()
            self.__special_frame.set_colorkey((255,255,255))           
            self.__special_images.append(self.__special_frame) 
        
            
            
        #Load and set up Kirby Hurt images
        self.__hurt_images = []
        
        for images in range(1,4):
            self.__hurt_frame = pygame.image.load('./kirbyHurt./Hurt'+self.__twin+'/kirby_hurt_'+ str(images)+'.gif')
            self.__hurt_frame = self.__hurt_frame.convert()
            self.__hurt_frame.set_colorkey((255,255,255))            
            self.__hurt_images.append(self.__hurt_frame)
            
            
            
        # Set up the rect and image attribute of Kirby based on its twin integer
        # If it is Twin 1, Kirby is placed onto the left side of the platform and faces right
        if twin == 1:
            self.__facing = 'right'
            self.image = self.__rightidle_image
            self.rect = self.image.get_rect()
            self.rect.left = 300
            
        # If it is Twin 2, Kirby is placed onto the right side of the platform and faces right
        else:
            self.__facing = 'left'
            self.image = self.__leftidle_image
            self.rect = self.image.get_rect()
            self.rect.left = 710
            
        # Both Kirby Twins are leveled on the platform
        self.rect.bottom = 380
        
        
    def idle(self):
        '''This method changes the image attribute to an Kirby Idle image and 
        sets Kirby's direction attributes,dx to 0 and dy to -4. It also sets
        Kirby's moving attribute to False.'''
        
        # Kirby image attribute is set to a Kirby Idle image according to Kirby's orientation
        if self.__facing == 'right':
            self.__state = 'self.__right_idle'
        else:
            self.__state = 'self.__left_idle'
        
        self.__moving = False
        self.__attacking = False
        self.__dx = 0
        self.__dy = -4
        

    
    def left_walk(self):
        '''This method sets Kirby's state to walking
        left and changes other movement and orientational attributes accordingly.
        The x directional value is also changed so that Kirby moves 6 pixels left
        every 30th of a second'''
        
        self.__state = 'self.__walking_left'
        self.__facing = 'left'
        self.__moving = True
        self.__dx = -6

    
        
    def right_walk(self):
        '''This method sets Kirby's state to walking
        right and changes other movement and orientational attributes accordingly.
        The x directional value is also changed so that Kirby moves 6 pixels right
        every 30th of a second'''
        
        self.__state = 'self.__walking_right'
        self.__facing = 'right'
        self.__moving = True
        self.__dx = 6
        
        
    def jump(self):
        '''This method sets Kirby's state is set to either left jumping or 
        right jumping based on Kirby's orientation and the movement attributes 
        are also changed accordingly, if Kirby has jumps remaining. The y directional
        attribute is also changed so that Kirby moves 8 pixels upward every 30th 
        of a second,if Kirby still has jumps left.'''
        
        # Kirby jumps if its jump attribute is greater than 0
        if self.__jumps_left > 0:
            if self.__facing == 'right':
                self.__state = 'self.__right_jumping'
            else:
                self.__state = 'self.__left_jumping' 
                
            self.__in_air = True
            self.__moving = True
            self.__dy = 8     
            
            # A jump sound is played
            self.__jump_sound.play()
    
    def fall(self):
        ''' This method sets Kirby's state
        to either left falling or right falling based on Kirby's orientation and
        the moving attribute is set to True. The y directional attribute is set
        to make Kirby fall 6 pixels every 30th of a second.'''
        
        if self.__facing == 'right':
            self.__state = 'self.__right_falling'
        else:
            self.__state = 'self.__left_falling'
        
        self.__attacking = False
        self.__moving = True
        self.__dy = -6
        
    def stationary_basic_attack(self):
        '''This method sets Kirby's state to either left or right basic based 
        on Kirby's orientation. Its moving attribute is also set to True.'''
        
        if self.__facing == 'left':
            self.__state = 'self.__left_basic' 
        else:
            self.__state = 'self.__right_basic'
            
        self.__moving = True
        self.__attacking = True
    
    def moving_basic_attack(self):
        '''This method sets Kirby's state to either left or right moving basic based 
        on Kirby's orientation. Its moving attribute is also set to True.'''

        if self.__facing == 'left':
            self.__state = 'self.__left_moving_basic' 
        else:
            self.__state = 'self.__right_moving_basic'
            
        self.__moving = True
        self.__attacking = True
            
    def special_attack(self):
        '''This method sets Kirby's state to either left or right special based 
        on Kirby's orientation. Its moving attribute is also set to True.'''
  
        self.__state = 'special'
        self.__dy = -12
        self.__dx = 0
            
        self.__moving = True
        self.__attacking = True
    
    def collide_player(self, side):
        '''This method accepts a string argument that could either be left or 
        right to determine which side the Kirby collided and move Kirby
        6 pixels away from the collision site.'''
        
        if side == 'left':
            self.rect.left += 6
        elif side == 'right':
            self.rect.left -= 6
            
    def player_hit(self,xy_direction):
        '''This method takes a tuple containing an 
        integer for the horizontal direction that Kirby gets knocked back 
        towards (positive integer means knocked to the right and 
        negative integer means knocked to the left) and secondly, a integer to 
        represent the vertical direction that Kirby gets knocked back towards 
        (positive integer represents knocked upwards and negative integer means
        knocked downwards). The knock back time of Kirby is also determined 
        by the tuple.'''

        self.__state = 'self.__hurt'
        self.__hurt_sound.play()
        
        self.__max_x_speed = xy_direction[0]
        self.__max_y_speed = xy_direction[1]
        
        self.__hurt_time = abs(self.__max_x_speed)/2
        
    def revive(self):
        '''This method places Kirby back at its starting position based on the 
        twin attribute (First Twin: Left of Platform, Second Twin: Right of 
        Platform) and calls Kirby's idle method.'''
        
        # If it is Twin 1, position to left of the platform
        if self.__twin == '_Twin1':
            self.rect.left = 300
        # If it is Twin 2, position to right of the platform
        else:
            self.rect.left = 710
            
        self.rect.bottom = 280
        
        # Set Kirby to its idle form
        self.idle()

    def get_position(self):
        '''This method returns the center tuple position of Kirby.'''
        return self.rect.center
    
    def get_facing(self):
        '''This method returns which way Kirby is facing.'''
        return self.__facing
            
    def get_moving(self):
        '''This method returns whether or not Kirby is moving.'''
        return self.__moving
    
    def get_attacking(self):
        '''This method returns whether or not Kirby is attacking.'''
        return self.__attacking
    
    def get_in_air(self):
        '''This method returns whether or not Kirby is in the air.'''
        return self.__in_air
    
    def get_state(self):
        '''This method returns the state of Kirby.'''
        return self.__state
    
    def update(self):
        '''This methods prevents Kirby from going through the platform and updates 
        Kirby's position based on its directional values. If Kirby has landed
        on the platform, Kirby's jump attribute is set to 5 (regains jumps) and
        Kirby's in air attribute is set to False. This method checks Kirby's 
        state attribute to determine which list of Kirby images to set the image 
        attribute to, one by one. The time attribute keeps track of the time that
        has passed by to changes the some images every 15th of a second.'''
        
        # Change Kirby's position by adding the dx and dy attribute to its rect
        self.rect.top -= self.__dy
        self.rect.left += self.__dx
        # Add one to the time attribute (each integerial increase represents 30th 
        # of a second that has passed by
        self.__time +=1
        
        # If Kirby's state is Hurt
        if self.__state == 'self.__hurt':
            # Kirby's hurt time goes down by 1 each 30th of a second
            self.__hurt_time -= 1
            
            # It loops through the list of images starting from the beginning
            if self.__frame >= len(self.__hurt_images):
                self.__frame = 0      
            else:
                self.image = self.__hurt_images[self.__frame]
                self.__frame += 1
            
            # Gradually increase or decrease Kirby's dy value to create an arched knockback
            if self.__max_y_speed > 0:
                if self.__dy <= self.__max_y_speed:
                    self.__dy += self.__max_y_speed/3
                else:
                    self.__dy -= self.__max_y_speed/6
                    
            elif self.__max_y_speed < 0:
                if self.__dy >= self.__max_y_speed:
                    self.__dy += self.__max_y_speed/3
                else:
                    self.__dy -= self.__max_y_speed/6
            
            # Gradually increase or decrease Kirby's dx value to create an arched knockback
            if self.__max_x_speed > 0:
                if self.__dx <= self.__max_x_speed:
                    self.__dx += self.__max_x_speed/3
                else:
                    self.__dx -= self.__max_x_speed/6
                    
            elif self.__max_x_speed < 0:
                if self.__dx >= self.__max_x_speed:
                    self.__dx += self.__max_x_speed/3
                else:
                    self.__dx -= self.__max_x_speed/6
            
            # If Kirby's hurt time is up, Kirby falls
            if self.__hurt_time <= 0:
                self.fall()
         
        # If Kirby's state is Right Idle
        elif self.__state == 'self.__right_idle':  
            self.image = self.__rightidle_image
            # Frame attribute set to 0 to allow Kirby to start from the first
            # image in each list
            self.__frame = 0
            
        # If Kirby's state is Left Idle
        elif self.__state == 'self.__left_idle':
            self.image = self.__leftidle_image
            self.__frame = 0
            
            
        # If Kirby's state is Walking Left   
        elif self.__state == 'self.__walking_left':
            # It loops through the list of images starting from the beginning
            if self.__frame >= len(self.__leftwalk_images):
                self.__frame = 0      
            else:
                self.image = self.__leftwalk_images[self.__frame]
                self.__frame += 1
                
        # If Kirby's state is Walking Right
        elif self.__state == 'self.__walking_right':
            if self.__frame >= len(self.__rightwalk_images):
                self.__frame = 0      
            else:
                self.image = self.__rightwalk_images[self.__frame]
                self.__frame += 1        
        
                
        # If Kirby's state is Left Jumping
        elif self.__state == 'self.__left_jumping':
            if self.__time % 2 == 0:
                if self.__frame >= len(self.__leftjump_images):
                    # If no more jumps are left, Kirby falls
                    if self.__jumps_left <= 0:
                        self.fall()
                    self.__frame = 0
                    # One jump is subtracted everytime the list of images are ran through
                    self.__jumps_left -= 1

                
                else:
                    self.image = self.__leftjump_images[self.__frame]
                    self.__frame += 1
                    
                    
        # If Kirby's state is Right Jumping        
        elif self.__state == 'self.__right_jumping':
            # Image changed every 15th of a second
            if self.__time % 2 == 0:
                if self.__frame >= len(self.__rightjump_images):
                    if self.__jumps_left <= 0:
                        self.fall()
                    self.__frame = 0
                    self.__jumps_left -= 1

                else:
                    self.image = self.__rightjump_images[self.__frame]
                    self.__frame += 1  
                                  
                    
        # If Kirby's state is Right Falling        
        elif self.__state == 'self.__right_falling':
            self.image = self.__rightfall_image
         
        # If Kirby's state is Left Falling    
        elif self.__state == 'self.__left_falling':
            self.image = self.__leftfall_image    
            
            
        # If Kirby's state is Left Basic    
        elif self.__state == 'self.__left_basic':
            if self.__time % 2 == 0:
                # Play Kirby's punch sound
                self.__punch_sound.play()
                if self.__frame >= len(self.__leftbasic_images):
                    self.__frame = 0      
                else:
                    self.image = self.__leftbasic_images[self.__frame]
                    self.__frame += 1
        
        # If Kirby's state is Right Basic  
        elif self.__state == 'self.__right_basic':
            if self.__time % 2 == 0:
                # Play Kirby's punch sound
                self.__punch_sound.play()
                if self.__frame >= len(self.__rightbasic_images):
                    self.__frame = 0      
                else:
                    self.image = self.__rightbasic_images[self.__frame]
                    self.__frame += 1    
                
                
        # If Kirby's state is Left Moving Basic         
        elif self.__state == 'self.__left_moving_basic':
            if self.__time % 3 == 0:
                if self.__frame >= len(self.__leftbasic_moving_images):
                    # Play Kirby's moving punch sound
                    self.__moving_punch_sound.play()
                    self.__frame = 0      
                else:
                    self.image = self.__leftbasic_moving_images[self.__frame]
                    self.__frame += 1
        
        # If Kirby's state is Right Moving Basic    
        elif self.__state == 'self.__right_moving_basic':
            if self.__time % 3 == 0:
                if self.__frame >= len(self.__rightbasic_moving_images):
                    # Play Kirby's moving punch sound
                    self.__moving_punch_sound.play()
                    self.__frame = 0      
                else:
                    self.image = self.__rightbasic_moving_images[self.__frame]
                    self.__frame += 1  
            
                
        # If Kirby's state is Special          
        elif self.__state == 'special':
            if self.__time % 2 == 0:
                if self.__frame >= len(self.__special_images):
                    self.image = self.__special_images[4]     
                else:
                    self.image = self.__special_images[self.__frame]
                    self.__frame += 1
            
                    
        # Check if Kirby has landed on top of the platform
        # If yes, the bottom of Kirby is set to the top of the platform
        if self.rect.bottom >= 380 and self.rect.top <= 340 and 900 >=self.rect.center[0] >=175: 
            self.rect.bottom = 380
            self.__in_air = False
            self.__jumps_left = 4
            if self.__state == 'self.__right_falling' or self.__state == 'self.__left_falling':
                self.idle()
            
        
        # Check if Kirby is underneath the platform and trying to pass through
        # If yes, the top of Kirby is set to the bottom of the platform
        elif self.rect.top <= 400 and self.rect.bottom >= 440 and 900 >=self.rect.center[0] >=175: 
            self.rect.top = 405
            self.__in_air = True
        
        else:
            self.__in_air = True
            
            
class Endzone(pygame.sprite.Sprite):
    '''This class defines the sprite for an Endzone.'''
    def __init__(self,side):
        '''This initializer method takes a string parameter to determine the side
        , which the endzone is to be placed and creates a black 1 pixel line in that 
        position.'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Create a horizontal and vertical surface attribute
        self.__line_1 = pygame.Surface((1300,1))
        self.__line_2 = pygame.Surface((1,1300))

        # Set the position of the endzone based on the side    
        if side == 'top': 
            self.image = self.__line_1
            self.__position = (-200,-150)
            
        elif side == 'bottom':
            self.image = self.__line_1
            self.__position = (-200,726)
            
        elif side == 'right':
            self.image = self.__line_2
            self.__position = (1174,-100)
            
        else:
            self.image = self.__line_2
            self.__position = (-150,-100)
        
        # Set up the image and rect attribute
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = self.__position[0]
        self.rect.top = self.__position[1]
        
            
              
class Explosion(pygame.sprite.Sprite):
    '''This class defines the sprite for an Explosion.'''
    
    def __init__(self,image,position):
        '''This initializer method takes an string argument determine which 
        explosion image, and a tuple that helps position the explosion's rect 
        attribute.'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Create a time and an explosion image attribute
        self.__time = 0
        self.__exp_image = image
        
        # Load each explosion image
        self.__endzone_top = pygame.image.load('./knockOut/knock_out_top.gif')
        self.__endzone_bottom = pygame.image.load('./knockOut/knock_out_bottom.gif')
        self.__endzone_right = pygame.image.load('./knockOut/knock_out_right.gif')
        self.__endzone_left = pygame.image.load('./knockOut/knock_out_left.gif')
        
        # Position the explosion image based on the side and position passed in
        if self.__exp_image == 'top':
            self.image = self.__endzone_top
            self.__y = -120
            self.__x = position[0]
            
        elif self.__exp_image == 'bottom':
            self.image = self.__endzone_bottom
            self.__y = 696
            self.__x = position[0]
            
        elif self.__exp_image == 'right':
            self.image = self.__endzone_right
            self.__y = position[1]
            self.__x = 1144
            
        elif self.__exp_image == 'left':
            self.image = self.__endzone_left
            self.__y = position[1]
            self.__x = -120
            
        # Set up the image and rect attribute
        self.image = self.image.convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        
        self.rect.centery = self.__y
        self.rect.centerx = self.__x
        
    def update(self):
        '''This method updates the position of the explosion and kills it after 
        a certain time.'''
        
        self.__time +=1
        if self.__time < 3:
            if self.__exp_image == 'top':
                self.rect.top += 100
            elif self.__exp_image == 'bottom':
                self.rect.top -= 100
            elif self.__exp_image == 'right':
                self.rect.left -= 100
            elif self.__exp_image == 'left':
                self.rect.left += 100
                
        elif self.__time > 6:
            if self.__exp_image == 'top':
                self.rect.top -= 30
            elif self.__exp_image == 'bottom':
                self.rect.top += 30
            elif self.__exp_image == 'right':
                self.rect.left += 30
            elif self.__exp_image == 'left':
                self.rect.left -= 30
                
        # Kill the explosion after 2 seconds
        if self.__time >60:    
            self.kill()
            
        
class Damage_Box(pygame.sprite.Sprite):
    '''This class defines the sprite for a Damage Box.'''
    
    def __init__(self,twin):
        '''This initializer method takes an integer argument to represent the Twin.
        The position of the damage box is then position based off of the Twin number.'''
        
         # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Determine the position of the Damage Box based on which twin
        # If it is Twin 1, position of the bottom left
        if twin == 1:
            self.__damage_box = pygame.image.load('./kirbyDamageBox/kirby_damage_box_1.gif')
            self.__position = (50,576)
        # If it is Twin 2, position of the bottom center
        else:
            self.__damage_box = pygame.image.load('./kirbyDamageBox/kirby_damage_box_2.gif')
            self.__position = (274,576)
            
        # Set up the image and rect attribute
        self.__damage_box = self.__damage_box.convert()
        self.__damage_box.set_colorkey((255,255,255))
        self.image = self.__damage_box
        self.rect = self.image.get_rect()
        self.rect.left = self.__position[0]
        self.rect.bottom = self.__position[1]
                

class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    
    def __init__(self,twin):
        '''This initializer takes an integer argument to set the position
        of the damage label. It also loads the system font "Number", and
        sets the player's damage to 0 and life to 3.'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the damage and life
        self.__font = pygame.font.Font("Number.ttf", 40)
        self.__player_damage = 0
        self.__life = 3
        
        # Create sound effect objects
        self.__gameover_sound = pygame.mixer.Sound("./soundEffects/Gameover.wav")
        self.__gameover_sound.set_volume(1.0) 
        
        # If it is Twin 1, the damage label is positioned to the bottom left
        if twin == 1:
            self.__position = (200, 515) 
        # If it is Twin 2, the damage label is positioned to the bottom center
        else:
            self.__position = (425, 515) 
            
    
    def new_life(self):
        '''This method sets the player damage attribute to 0.'''
        self.__player_damage = 0
        
    def player_hit(self,damage):
        '''This method takes an integer argument and adds it onto the player's damage attribute.'''
        self.__player_damage += damage
    
    def lose_life(self):
        '''This method subtracts one from the life attribute.'''
        self.__life -= 1
        
    def get_damage(self):
        '''This method returns the player's damage.'''
        return self.__player_damage
    
    def get_life(self):
        '''This method returns the player's life.'''
        return self.__life
    
    def gameover(self):
        '''This method plays a game over sound.'''
        self.__gameover_sound.play()
 
    def update(self):
        '''This method will be called automatically to display 
        the current damage at the bottom left of the game window if it is Twin
        1 and bottom center if it is Twin 2. It also prevents the damage attribute
        from passing 200.'''
        
        # If damage passed 200, set damage to 200
        if self.__player_damage > 200:
            self.__player_damage = 200
            
        # Set up the image by rendering the label and set up the rect attribute 
        self.__message = str(self.__player_damage)+'%'
        self.image = self.__font.render(self.__message, 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__position
        

class KirbyStock(pygame.sprite.Sprite):
    '''This class defines a Kirby Stock sprite.'''
    
    def __init__(self,twin,position):
        '''This initializer method takes a integer argument to determine the stock image
        for which twin, and another integer argument to position the stock image.'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # If it is Twin 1, load a red Kirby Stock image
        if twin == 1:
            kirby_stock_image = pygame.image.load('./kirbyStock./kirby_stock_twin_1.gif')
        # If it is Twin 2, load a blue Kirby Stock image
        else:
            kirby_stock_image = pygame.image.load('./kirbyStock./kirby_stock_twin_2.gif')
           
        
        # Set up the image attribute    
        self.image = kirby_stock_image
        self.image = self.image.convert()
        self.image.set_colorkey((255,255,255))
        
        # Set up the rect attribute
        self.rect = kirby_stock_image.get_rect()
        if position == 1:
            self.rect.center = (170, 550)
        elif position == 2:
            self.rect.center = (200, 550)
        elif position == 3:
            self.rect.center = (230, 550)
        elif position == 4:
            self.rect.center = (395, 550)
        elif position == 5:
            self.rect.center = (425, 550)
        elif position == 6:
            self.rect.center = (455, 550)
        

        
        

