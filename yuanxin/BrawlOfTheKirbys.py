''' Name: Yuanxin Xue

    Date: May 7, 2015
    
    Description: This program is a Brawl of the Kirbys, two player fighting game.
'''

# I - IMPORT AND INITIALIZE
import pygame, BrawlSprites
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1024, 576))
 
def start_screen():
    '''This function defines the start screen of the game.'''
    # D - DISPLAY
    pygame.display.set_caption("Brawl of The Kirbys")
     
    # E - ENTITIES
    background = pygame.image.load('start_screen.gif')
    screen.blit(background, (0, 0))
    
    # Create font objects for the start screen
    title_font = pygame.font.Font('SuperSmashFont.ttf', 50)
    instruction_font = pygame.font.Font('SuperSmashFont.ttf', 30)
    
    # Render the text using the different font objects
    title = title_font.render('BRAWL OF THE KIRBYS', 1, (0,0,0))
    instruction = instruction_font.render('Press any Button to Continue',1,((0,0,0)))
    
    # Load the background music, set it to maximum volume, and play it repeatedly
    pygame.mixer.music.load("./backgroundMusic/Main Theme.ogg")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    
    
    #A - ACTION
    clock = pygame.time.Clock()
    keepGoing = True
    
    # LOOP
    while keepGoing:
        
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                # The player continues onto the instruction screen when a button is pressed
                pygame.mixer.music.fadeout(2000)
                pygame.time.delay(2000)
                return 'continue'
            
        # REFRESH SCREEN
        screen.blit(title,(200,250))
        screen.blit(instruction,(270,430))
        pygame.display.flip()
    
    # Close the game window
    pygame.quit()
    
    
def instruction_screen():
    '''This function defines the instruction screen of the game.'''
    # D - DISPLAY
    pygame.display.set_caption("Brawl of The Kirbys")
     
    # E - ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0)) 
    screen.blit(background, (0, 0))
    
    # Create font object
    instruction_font = pygame.font.Font('Number.ttf', 30)
    
    # Render instruction text using font object
    instruction_label = instruction_font.render('INSTRUCTIONS', 1, (0,255,0))
    player_label = instruction_font.render('Player 1'+' '*31 +'Player 2', 1, (255,0,0))
    moves_1_label = instruction_font.render('To Move: Arrow Keys' + ' '*11 +'To Move: WASD', 1, (255,255,255))
    moves_2_label = instruction_font.render('Basic Attack: 7' + ' '*21 +'Basic Attack: H', 1, (255,255,255))
    moves_3_label = instruction_font.render('Special Attack: 8' + ' '*18 +'Special Attack: J', 1, (255,255,255))
    continue_label = instruction_font.render('Press any Button to Brawl', 1, (0,255,0))
    
    # Load the background music, set it to maximum volume and play it repeatedly
    pygame.mixer.music.load("./backgroundMusic/Instruction Theme.ogg")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    
    
    #A - ACTION
    clock = pygame.time.Clock()
    keepGoing = True
    
    # LOOP
    while keepGoing:

        # TIME
        clock.tick(30)
     
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                # Player begins the fight when a button is pressed
                pygame.mixer.music.fadeout(2000)
                pygame.time.delay(2000)
                return 'start'
            
        # REFRESH SCREEN
        screen.blit(instruction_label,(20, 100))
        screen.blit(player_label,(20, 200))
        screen.blit(moves_1_label,(20, 240))
        screen.blit(moves_2_label,(20, 280))
        screen.blit(moves_3_label,(20, 320))
        screen.blit(continue_label,(20, 450))
        pygame.display.flip()
     
    # Close the game window
    pygame.quit()
    
def brawl():
    '''This function defines the fighting part of the game.'''
      
    # D - DISPLAY
    pygame.display.set_caption("Brawl of The Kirbys")
     
    # E - ENTITIES
    background = pygame.image.load('Background.gif')
    background = background.convert()
    screen.blit(background, (0, 0))
    
    # Create sprites: Kirby_Twin_1, Kirby_Twin_2, Endzones, Damage Boxes and Damage 
    # Percentage for each twin, Stock Lives for each twin
    Kirby_Twin_1 = BrawlSprites.Kirby(1)
    Kirby_Twin_2 = BrawlSprites.Kirby(2)
    
    top_endzone = BrawlSprites.Endzone('top')
    bottom_endzone = BrawlSprites.Endzone('bottom')
    right_endzone = BrawlSprites.Endzone('right')
    left_endzone = BrawlSprites.Endzone('left')
    
    Twin_1_damage_box = BrawlSprites.Damage_Box(1)
    Twin_2_damage_box = BrawlSprites.Damage_Box(2)
    
    Twin_1_damage_percentage = BrawlSprites.ScoreKeeper(1)
    Twin_2_damage_percentage = BrawlSprites.ScoreKeeper(2)
    
    Twin_1_stock_1 = BrawlSprites.KirbyStock(1,1)
    Twin_1_stock_2 = BrawlSprites.KirbyStock(1,2)
    Twin_1_stock_3 = BrawlSprites.KirbyStock(1,3)
    
    Twin_2_stock_1 = BrawlSprites.KirbyStock(2,4)
    Twin_2_stock_2 = BrawlSprites.KirbyStock(2,5)
    Twin_2_stock_3 = BrawlSprites.KirbyStock(2,6)
    
    # Create sprite group
    twin1stocks = [Twin_1_stock_1,Twin_1_stock_2,Twin_1_stock_3]
    twin2stocks = [Twin_2_stock_1,Twin_2_stock_2,Twin_2_stock_3]
    kirbyGroup = pygame.sprite.Group(Kirby_Twin_1,Kirby_Twin_2)
    damageBoxGroup = pygame.sprite.Group(Twin_1_damage_box,Twin_2_damage_box)
    damagePercentageGroup = pygame.sprite.Group(Twin_1_damage_percentage,Twin_2_damage_percentage)
    endzoneGroup = pygame.sprite.Group(top_endzone,bottom_endzone, right_endzone,left_endzone)
    
    # Create a sprite group containing all the sprites
    allSprites = pygame.sprite.OrderedUpdates(damageBoxGroup,damagePercentageGroup,\
                                              twin1stocks,twin2stocks,\
                                              kirbyGroup,endzoneGroup)
    
    # Load the background music, set the volume and play it repeatedly
    pygame.mixer.music.load("./backgroundMusic/Final Destination.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
       
    # A - ACTION
    
    # ASSIGN VALUES
    clock = pygame.time.Clock()
    keepGoing = True
    
    # Create a list to hold each player's keys
    kirbyTwin_1Keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_KP7, pygame.K_KP8]
    kirbyTwin_2Keys = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_h, pygame.K_j]
    
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
    
    
    # LOOP
    while keepGoing:

        # TIME
        clock.tick(30)
     
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.fadeout(2000)
                keepGoing = False
                
            if event.type == pygame.KEYDOWN:
                
                # Player allowed to move only when they are not hurt
                if Kirby_Twin_1.get_state() != 'self.__hurt':
                    
                    # Kirby Twin 1's Moves
                    if event.key == pygame.K_LEFT:
                        Kirby_Twin_1.left_walk()
    
                    elif event.key == pygame.K_RIGHT:
                        Kirby_Twin_1.right_walk()
    
                    elif event.key == pygame.K_UP:
                        Kirby_Twin_1.jump()
                    
                    elif event.key == pygame.K_7:
                        if Kirby_Twin_1.get_moving():
                            Kirby_Twin_1.moving_basic_attack()
                        else:
                            Kirby_Twin_1.stationary_basic_attack()
    
                    elif event.key == pygame.K_8:
                        Kirby_Twin_1.special_attack()
                        
                        
                if Kirby_Twin_2.get_state() != 'self.__hurt':
                    # Kirby Twin 2's Moves            
                    if event.key == pygame.K_a:
                        Kirby_Twin_2.left_walk()
    
                    elif event.key == pygame.K_d:
                        Kirby_Twin_2.right_walk()
                    
                    elif event.key == pygame.K_w:
                        Kirby_Twin_2.jump()
                    
                    elif event.key == pygame.K_h:
                        if Kirby_Twin_2.get_moving():
                            Kirby_Twin_2.moving_basic_attack()
                        else:
                            Kirby_Twin_2.stationary_basic_attack()
                            
                    elif event.key == pygame.K_j:
                        Kirby_Twin_2.special_attack()

            
            if event.type == pygame.KEYUP:
                # Kirby Twin 1 Falling and Idling
                if event.key in kirbyTwin_1Keys:
                    if Kirby_Twin_1.get_in_air() == True:
                        Kirby_Twin_1.fall()
                    else:
                        Kirby_Twin_1.idle()

                # Kirby Twin 2 Falling and Idling  
                if event.key in kirbyTwin_2Keys:    
                    if Kirby_Twin_2.get_in_air() == True:
                        Kirby_Twin_2.fall()
                    else:
                        Kirby_Twin_2.idle()

       
        # Play a gameover message and stop the game loop       
        if twin1stocks == [] or twin2stocks == []:
            Twin_1_damage_percentage.gameover()
            keepGoing = False
            
        # Check if Kirby 1 has collided with Kirby 2 and reposition accordingly    
        if Kirby_Twin_1.rect.colliderect(Kirby_Twin_2.rect):
            if Kirby_Twin_1.get_facing() != Kirby_Twin_2.get_facing():
                Kirby_Twin_1.collide_player(Kirby_Twin_1.get_facing())
                Kirby_Twin_2.collide_player(Kirby_Twin_2.get_facing())
            else:
                if Kirby_Twin_1.get_position()[0] < Kirby_Twin_2.get_position()[0]:
                    Kirby_Twin_1.collide_player('right')
                    Kirby_Twin_2.collide_player('left')
                else:
                    Kirby_Twin_1.collide_player('left')
                    Kirby_Twin_2.collide_player('right')
                    
                    
        # Check if Kirby 1 has hit an endzone             
        Kirby_Twin_1_endzones_hit = pygame.sprite.spritecollide(Kirby_Twin_1, endzoneGroup, False)
        # If Kirby 1 has hit an endzone, create an explosion based on where Kirby 1 collided
        if Kirby_Twin_1_endzones_hit:
            pos = Kirby_Twin_1.get_position()
            if top_endzone in Kirby_Twin_1_endzones_hit:
                exp = BrawlSprites.Explosion('top',pos)
                
            elif bottom_endzone in Kirby_Twin_1_endzones_hit:
                exp = BrawlSprites.Explosion('bottom',pos)
                
            elif right_endzone in Kirby_Twin_1_endzones_hit:
                exp = BrawlSprites.Explosion('right',pos)
                
            elif left_endzone in Kirby_Twin_1_endzones_hit:
                exp = BrawlSprites.Explosion('left',pos)
            
            # Decrease Kirby 1's lives by 1, reset damage taken to 0 and revive
            twin1stocks[-1].kill()
            del twin1stocks[-1]
            allSprites.add(exp)
            Kirby_Twin_1.revive()
            Twin_1_damage_percentage.new_life()
            
            
        # Check if Kirby 2 has hit an endzone      
        Kirby_Twin_2_endzones_hit = pygame.sprite.spritecollide(Kirby_Twin_2, endzoneGroup, False)
        # If Kirby 2 has hit an endzone, create an explosion based on where Kirby 2 collided
        if Kirby_Twin_2_endzones_hit:
            pos = Kirby_Twin_2.get_position()
            if top_endzone in Kirby_Twin_2_endzones_hit:
                exp = BrawlSprites.Explosion('top',pos)
                
            elif bottom_endzone in Kirby_Twin_2_endzones_hit:
                exp = BrawlSprites.Explosion('bottom',pos)
                
            elif right_endzone in Kirby_Twin_2_endzones_hit:
                exp = BrawlSprites.Explosion('right',pos)
                
            elif left_endzone in Kirby_Twin_2_endzones_hit:
                exp = BrawlSprites.Explosion('left',pos)
            
            # Decrease Kirby 2's lives by 1, reset damage taken to 0 and revive
            twin2stocks[-1].kill()
            del twin2stocks[-1]
            allSprites.add(exp)
            Kirby_Twin_2.revive() 
            Twin_2_damage_percentage.new_life()
            
                    
        # Check if Kirby 1 is attacking    
        if Kirby_Twin_1.get_attacking() == True:
            # If Kirby 1 is facing right, check if Kirby 2 is beside Kirby 1
            if Kirby_Twin_1.get_facing() == 'right':
                if (Kirby_Twin_1.rect.right) < Kirby_Twin_2.rect.centerx < (Kirby_Twin_1.rect.right + 50)\
                   and Kirby_Twin_2.rect.bottom > Kirby_Twin_1.rect.centery > (Kirby_Twin_2.rect.bottom - 50):
                    
                    # Determine which attack is used and Kirby 2 flys and takes damage accordingly
                    if Kirby_Twin_1.get_state() == 'self.__right_basic':
                        damage = 2
                        knock_back = (5*Twin_2_damage_percentage.get_damage()/10,4*Twin_2_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_1.get_state() == 'self.__right_moving_basic':
                        damage = 1
                        knock_back = (5*Twin_2_damage_percentage.get_damage()/10,4*Twin_2_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_1.get_state() == 'special':
                        damage = 5
                        knock_back = (4,4*Twin_2_damage_percentage.get_damage()/10)
                    
                    # Kirby 2 is knocked back and takes damage
                    Kirby_Twin_2.player_hit(knock_back)
                    Twin_2_damage_percentage.player_hit(damage)
                    
            # If Kirby 1 is facing left, check if Kirby 2 is beside Kirby 1        
            elif Kirby_Twin_1.get_facing() == 'left':
                if (Kirby_Twin_1.rect.left) > Kirby_Twin_2.rect.centerx > (Kirby_Twin_1.rect.left - 50)\
                   and Kirby_Twin_2.rect.bottom > Kirby_Twin_1.rect.centery > (Kirby_Twin_2.rect.bottom - 50):
                    
                    # Determine which attack is used and Kirby 2 flys and takes damage accordingly
                    if Kirby_Twin_1.get_state() == 'self.__left_basic':
                        damage = 1
                        knock_back = (-5*Twin_2_damage_percentage.get_damage()/10,4*Twin_2_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_1.get_state() == 'self.__left_moving_basic':
                        damage = 1
                        knock_back = (-5*Twin_2_damage_percentage.get_damage()/10,4*Twin_2_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_1.get_state() == 'special':
                        damage = 5
                        knock_back = (-4,4*Twin_2_damage_percentage.get_damage()/10)
                     
                    # Kirby 2 is knocked back and takes damage
                    Kirby_Twin_2.player_hit(knock_back)
                    Twin_2_damage_percentage.player_hit(damage)
                    
                    
        # Check if Kirby 2 is attacking             
        if Kirby_Twin_2.get_attacking() == True:
            # If Kirby 1 is facing right, check if Kirby 2 is beside Kirby 1
            if Kirby_Twin_2.get_facing() == 'right':
                if (Kirby_Twin_2.rect.right) < Kirby_Twin_1.rect.centerx < (Kirby_Twin_2.rect.right + 50)\
                   and Kirby_Twin_2.rect.bottom > Kirby_Twin_1.rect.centery > (Kirby_Twin_2.rect.bottom - 50):
                    
                    # Determine which attack is used and Kirby 1 flys and takes damage accordingly
                    if Kirby_Twin_2.get_state() == 'self.__right_basic':
                        damage = 2
                        knock_back = (5*Twin_1_damage_percentage.get_damage()/20,4*Twin_1_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_2.get_state() == 'self.__right_moving_basic':
                        damage = 1
                        knock_back = (5*Twin_1_damage_percentage.get_damage()/20,4*Twin_1_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_2.get_state() == 'special':
                        damage = 5
                        knock_back = (4,4*Twin_1_damage_percentage.get_damage()/10)
                    
                    # Kirby 1 is knocked back and takes damage
                    Kirby_Twin_1.player_hit(knock_back)
                    Twin_1_damage_percentage.player_hit(damage)
                    
            # If Kirby 1 is facing left, check if Kirby 2 is beside Kirby 1        
            elif Kirby_Twin_2.get_facing() == 'left':
                if (Kirby_Twin_2.rect.left) > Kirby_Twin_1.rect.centerx > (Kirby_Twin_2.rect.left - 50)\
                   and Kirby_Twin_2.rect.bottom > Kirby_Twin_1.rect.centery > (Kirby_Twin_2.rect.bottom - 50):
                    
                    # Determine which attack is used and Kirby 1 flys and takes damage accordingly
                    if Kirby_Twin_2.get_state() == 'self.__left_basic':
                        damage = 2
                        knock_back = (-5*Twin_1_damage_percentage.get_damage()/20,4*Twin_1_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_2.get_state() == 'self.__left_moving_basic':
                        damage = 1
                        knock_back = (-5*Twin_1_damage_percentage.get_damage()/20,4*Twin_1_damage_percentage.get_damage()/40)
                        
                    elif Kirby_Twin_2.get_state() == 'special':
                        damage = 5
                        knock_back = (-4,4*Twin_1_damage_percentage.get_damage()/10)
                    
                    # Kirby 1 is knocked back and takes damage
                    Kirby_Twin_1.player_hit(knock_back)
                    Twin_1_damage_percentage.player_hit(damage)            
                    
               
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
         
    # Unhide the mouse pointer and close the game window after 3 seconds
    pygame.mouse.set_visible(True)
    pygame.time.delay(3000)
    pygame.quit()     
     
# Determine if the user has pressed a button to continue from one screen to the next
if start_screen() == 'continue':
    if instruction_screen() == 'start':
        brawl()
