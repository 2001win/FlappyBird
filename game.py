import pygame, sys, random
# tao ham
def draw_floor():
    screen.blit(floor, (floor_x_pos,650))
    screen.blit(floor, (floor_x_pos+432,650))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos - 650))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement*4, 1)
    new_bird = pygame.transform.scale2x(new_bird)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'main game':
        score_suface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_suface.get_rect(center = (216,100))
        screen.blit(score_suface, score_rect)
    if game_state == 'game_over':
        score_suface = game_font.render(f'Score: {int(high_score)}',True,(255,255,255))
        score_rect = score_suface.get_rect(center = (216,100))
        screen.blit(score_suface, score_rect)

        high_score_suface = game_font.render(f'High score: {int(score)}',True,(255,255,255))
        high_score_rect = high_score_suface.get_rect(center = (216,610))
        screen.blit(high_score_suface, high_score_rect)

pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('04B_19.ttf',40)
# tao cac bien
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
# chen background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# chen san
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
# # chen chim
bird_down = pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
bird_mid = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird_up = pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))

# tao timer
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)
# tao ong
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
# tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)
pipe_height = [200, 300, 400]
# loop cua game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -11
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index+=1
            else:
                bird_index=0
            bird, bird_rect = bird_animation()

    if game_active:
        #chim
        screen.blit(bg, (0,0))
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active=check_collision(pipe_list)
        #ong
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score+=0.01
        score_display('main game')
    else:
        score_display('game_over')
    #san
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)




