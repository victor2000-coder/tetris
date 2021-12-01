import random

import pygame

import Buttons

pygame.init()

# magic integers
# rotations

NORTH, WEST, SOUTH, EAST = 1, 2, 3, 4

# tetra variables
HEIGHT, WIDTH, STATE, X_POS, Y_POS, SPEED, KIND, TET_IMAGE, Y_POS_IN_CONCRETE_CEIL = \
    tuple(range(1, 10))

# tetra kinds
S, Z, O, L, J, T, I = tuple(range(1, 8))

# Game Global variables
COMFORTABLE_TIME_STOP, SCORE, WIDTH_OF_FIELD, HEIGHT_OF_FIELD, CEIL_WIDTH, CEIL_HEIGHT, PAUSE, STANDARD_SPEED, \
BG_COLOR, COLOR_OF_FALLEN_TETRA, i_counter = \
    tuple(range(1, 12))

contains = {
    NORTH: 0,
    WEST: 0,
    EAST: 450,
    SOUTH: 900
}

other_data = {
    COMFORTABLE_TIME_STOP: 100,
    SCORE: 0,
    WIDTH_OF_FIELD: 10,
    HEIGHT_OF_FIELD: 20,
    CEIL_WIDTH: 40,
    CEIL_HEIGHT: 40,
    PAUSE: True,
    STANDARD_SPEED: 1,
    BG_COLOR: (0, 108, 135),
    COLOR_OF_FALLEN_TETRA: (254, 251, 137),
    i_counter: 0
}

# falling tetra state
tetra_data = {
    HEIGHT: 40,
    WIDTH: 40,
    STATE: NORTH,
    X_POS: 3,
    Y_POS: 0,
    SPEED: 1,
    KIND: S,
    TET_IMAGE: pygame.image.load('tet_tet_4.png'),
    Y_POS_IN_CONCRETE_CEIL: 0
}

# sound magic integers

DEFEAT, BTN_SOUND = 1, 2

sound_lib = {
    DEFEAT: pygame.mixer.Sound('defeat.mp3'),
    BTN_SOUND: pygame.mixer.Sound('button.mp3'),
}

play_field = [[0 for i in range(other_data[WIDTH_OF_FIELD])] for i in range(other_data[HEIGHT_OF_FIELD] + 4)]
tetris = {
    S: {
        NORTH: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
        ],
        WEST: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
        ],
        EAST: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
        ]
    },

    Z: {

        NORTH: [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        WEST: [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
        ],
        EAST: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
        ]
    },

    O: {
        NORTH: [
            [1, 1],
            [1, 1],
        ],
        WEST: [
            [1, 1],
            [1, 1],
        ],
        SOUTH: [
            [1, 1],
            [1, 1],
        ],
        EAST: [
            [1, 1],
            [1, 1],
        ],
    },

    L: {
        NORTH: [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        WEST: [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
        ],
        EAST: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
        ],
    },

    J: {
        NORTH: [
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        WEST: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 1, 0],
        ],
        EAST: [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ],
    },

    T: {
        NORTH: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        WEST: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
        ],
        EAST: [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
        ],
    },

    I: {
        NORTH: [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        WEST: [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ],
        SOUTH: [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        EAST: [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
        ],
    },
}


# change difficult menu
def set_running():
    other_data[PAUSE] = False
    if not is_tetra_falling():
        tetra_data[SPEED] = other_data[STANDARD_SPEED]
        generate_tetra()
        init_tetris()
    pygame.mixer.music.play()


def set_easy_difficult():
    other_data[STANDARD_SPEED] = 1
    pygame.mixer.music.load("Original 'Tetris Theme' (Extended Version).mp3")
    other_data[BG_COLOR] = (0, 254, 234)
    tetra_data[TET_IMAGE] = pygame.transform.scale(pygame.image.load('tet_tet_4.png'),
                                                   (other_data[CEIL_WIDTH], other_data[CEIL_HEIGHT]))
    other_data[COLOR_OF_FALLEN_TETRA] = (254, 251, 137)
    window.fill(other_data[BG_COLOR])
    set_running()


def set_normal_difficult():
    other_data[STANDARD_SPEED] = 2
    pygame.mixer.music.load("Original 'Tetris Theme' (Extended Version).mp3")
    other_data[BG_COLOR] = (0, 108, 135)
    tetra_data[TET_IMAGE] = pygame.transform.scale(pygame.image.load('tet_tet_4.png'),
                                                   (other_data[CEIL_WIDTH], other_data[CEIL_HEIGHT]))
    other_data[COLOR_OF_FALLEN_TETRA] = (254, 251, 137)
    window.fill(other_data[BG_COLOR])
    set_running()


def set_hard_difficult():
    other_data[STANDARD_SPEED] = 9
    pygame.mixer.music.load('Tetris 99 50 Players Remaining - Extended.mp3')
    other_data[BG_COLOR] = (0, 0, 0)
    window.fill(other_data[BG_COLOR])
    tetra_data[TET_IMAGE] = pygame.transform.scale(pygame.image.load('tetro.png'),
                                                   (other_data[CEIL_WIDTH], other_data[CEIL_HEIGHT]))
    other_data[COLOR_OF_FALLEN_TETRA] = (177, 21, 21)
    set_running()


def set_monster_difficult():
    other_data[STANDARD_SPEED] = 9
    pygame.mixer.music.load('Techno - Tetris (Remix).mp3')
    other_data[BG_COLOR] = (0, 108, 135)
    window.fill(other_data[BG_COLOR])
    set_running()


select_mode_btn = Buttons.ButtonsSet()

easy_difficult_btn = Buttons.ButtonWithMessage(
    active_color=(0, 254, 234), inactive_color=(139, 249, 254), clicked_color=(0, 254, 234),
    contains=(325, 50),
    message='FIRST TIME PLAY TETRIS', action=set_easy_difficult, title='TRAINING', sound=sound_lib[BTN_SOUND])
normal_difficult_btn = Buttons.ButtonWithMessage(
    active_color=(0, 108, 135), inactive_color=(139, 249, 254), clicked_color=(0, 108, 135),
    contains=(325, 50),
    message='JUST NORMAL', action=set_normal_difficult, title='NORMAL', sound=sound_lib[BTN_SOUND])
hard_difficult_btn = Buttons.ButtonWithMessage(
    active_color=(255, 17, 0,), inactive_color=(139, 249, 254), clicked_color=(255, 17, 0,),
    contains=(325, 50),
    message='VERY HARD', action=set_hard_difficult, title='HARD', sound=sound_lib[BTN_SOUND])
monster_difficult_btn = Buttons.ButtonWithMessage(
    active_color=(0, 0, 0), inactive_color=(139, 249, 254), clicked_color=(193, 17, 24), text_color=(177, 21, 21),
    contains=(325, 50),
    message='COMING SOON', action=set_monster_difficult, title='MONSTER', sound=sound_lib[BTN_SOUND])
select_mode_btn.add_component(component=easy_difficult_btn)
select_mode_btn.add_component(component=normal_difficult_btn)
select_mode_btn.add_component(component=hard_difficult_btn)
select_mode_btn.add_component(component=monster_difficult_btn)


def init_tetris():
    tetra_data[TET_IMAGE] = pygame.transform.scale(tetra_data[TET_IMAGE],
                                                   (other_data[CEIL_WIDTH], other_data[CEIL_HEIGHT]))


def generate_tetra():
    pygame.time.delay(100)
    tetra_index = random.randint(1, 7)

    # i_counter - variable, that quickens emergence of I tetra
    if other_data[i_counter] == 0:
        tetra_index = I
        other_data[i_counter] = 5
    if tetra_data == I:
        other_data[i_counter] = 5
    other_data[i_counter] -= 1

    tetra_rotation = random.randint(1, 4)
    other_data[CEIL_WIDTH] = contains[EAST] / other_data[WIDTH_OF_FIELD]
    other_data[CEIL_HEIGHT] = contains[SOUTH] / other_data[HEIGHT_OF_FIELD]
    tetra_data[HEIGHT] = int(other_data[CEIL_HEIGHT] * len(tetris[tetra_index][tetra_rotation]))
    tetra_data[WIDTH] = int(other_data[CEIL_WIDTH] * len(tetris[tetra_index][tetra_rotation][0]))
    tetra_data[X_POS] = 3
    tetra_data[Y_POS] = 0
    tetra_data[STATE] = tetra_rotation
    tetra_data[KIND] = tetra_index
    tetra_data[Y_POS_IN_CONCRETE_CEIL] = 0
    tetra_data[SPEED] = other_data[STANDARD_SPEED]
    for line_index in range(len(tetris[tetra_index][tetra_rotation])):
        temp_line = play_field[line_index][:2]
        for ceil in tetris[tetra_index][tetra_rotation][line_index]:
            temp_line += [ceil]
        temp_line += play_field[line_index][2 + len(tetris[tetra_index][tetra_rotation][line_index]):]
        play_field[line_index] = temp_line
        draw()

    other_data[COMFORTABLE_TIME_STOP] = 200


def draw():
    for line in range(3, len(play_field)):
        for ceil in range(len(play_field[line])):
            if play_field[line][ceil] == 2:
                pygame.draw.rect(window, other_data[COLOR_OF_FALLEN_TETRA],
                                 (ceil * other_data[CEIL_WIDTH], (line - 4) * other_data[CEIL_HEIGHT],
                                  other_data[CEIL_WIDTH],
                                  other_data[CEIL_HEIGHT]))
    for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
        for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][line])):
            if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                window.blit(tetra_data[TET_IMAGE],
                            (tetra_data[X_POS] * other_data[CEIL_WIDTH] + ceil * other_data[CEIL_WIDTH],
                             (tetra_data[Y_POS] - 4) * other_data[CEIL_HEIGHT] + line * other_data[CEIL_HEIGHT] +
                             tetra_data[Y_POS_IN_CONCRETE_CEIL],
                             other_data[CEIL_WIDTH], other_data[CEIL_HEIGHT]))
    font = pygame.font.SysFont("Comic Sans MS", 30)
    label = font.render(str(other_data[SCORE]), 1, (255, 255, 255))
    window.blit(label, (0, 0))


def check_is_line_ready():
    for line_index in range(len(play_field)):
        if play_field[line_index] == [2 for i in range(other_data[WIDTH_OF_FIELD])]:
            return line_index
    return -1


def check_is_tetra_fallen():
    for line in range(len(play_field)):
        for ceil in range(len(play_field[line])):
            if play_field[line][ceil] == 1 and \
                    (line == other_data[HEIGHT_OF_FIELD] + 3 or play_field[line + 1][ceil] == 2):
                return False
    return True


def check_is_game_ended():
    if 2 in play_field[4]:
        return True
    return False


def is_tetra_falling():
    for line in range(len(play_field)):
        for ceil in range(len(play_field[line])):
            if play_field[line][ceil] == 1:
                return True
    return False


def can_be_transformed():
    for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
        for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][line])):
            if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1 and \
                    ((play_field[tetra_data[Y_POS] + line][tetra_data[X_POS] + ceil] == 2) or
                     (play_field[tetra_data[Y_POS] + line + 1][tetra_data[X_POS] + ceil] == 2 and
                      tetra_data[Y_POS_IN_CONCRETE_CEIL] > 5)):
                return False
    return True


def position_of_first_falling_square(rotation):
    if rotation == WEST:
        def get_line_with_first():
            for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][0])):
                for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
                    if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                        return ceil

        return get_line_with_first() + tetra_data[X_POS]
    elif rotation == NORTH:
        def get_line_with_first():
            for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
                for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][line])):
                    if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                        return line

        return get_line_with_first() + tetra_data[Y_POS]
    elif rotation == EAST:
        def get_line_with_first():
            for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][0]) - 1, -1, -1):
                for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
                    if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                        return ceil

        return get_line_with_first() + tetra_data[X_POS]
    else:
        def get_line_with_first():
            for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]]) - 1, -1, -1):
                for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][line])):
                    if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                        return line

        return get_line_with_first() + tetra_data[Y_POS]


# don't toch
def turn():
    old_rotate = tetra_data[STATE]
    if tetra_data[STATE] == NORTH:
        tetra_data[STATE] = EAST
    elif tetra_data[STATE] == EAST:
        tetra_data[STATE] = SOUTH
    elif tetra_data[STATE] == SOUTH:
        tetra_data[STATE] = WEST
    elif tetra_data[STATE] == WEST:
        tetra_data[STATE] = NORTH
    other_data[CEIL_WIDTH] = contains[EAST] / other_data[WIDTH_OF_FIELD]
    other_data[CEIL_HEIGHT] = contains[SOUTH] / other_data[HEIGHT_OF_FIELD]
    tetra_data[HEIGHT] = int(other_data[CEIL_HEIGHT] * len(tetris[tetra_data[KIND]][tetra_data[STATE]]))
    tetra_data[WIDTH] = int(other_data[CEIL_WIDTH] * len(tetris[tetra_data[KIND]][tetra_data[STATE]][0]))
    if position_of_first_falling_square(EAST) >= other_data[WIDTH_OF_FIELD]:
        tetra_data[X_POS] -= (position_of_first_falling_square(EAST) - other_data[WIDTH_OF_FIELD] + 1)
    elif position_of_first_falling_square(WEST) < 0:
        tetra_data[X_POS] -= position_of_first_falling_square(WEST)
    if not can_be_transformed():
        tetra_data[STATE] = old_rotate
        other_data[CEIL_WIDTH] = contains[EAST] / other_data[WIDTH_OF_FIELD]
        other_data[CEIL_HEIGHT] = contains[SOUTH] / other_data[HEIGHT_OF_FIELD]
        tetra_data[HEIGHT] = int(other_data[CEIL_HEIGHT] * len(tetris[tetra_data[KIND]][tetra_data[STATE]]))
        tetra_data[WIDTH] = int(other_data[CEIL_WIDTH] * len(tetris[tetra_data[KIND]][tetra_data[STATE]][0]))
        if tetra_data[X_POS] + tetra_data[WIDTH] / other_data[CEIL_WIDTH] > other_data[WIDTH_OF_FIELD]:
            tetra_data[X_POS] = int((contains[EAST] - tetra_data[WIDTH]) / other_data[CEIL_WIDTH])
    window.fill(other_data[BG_COLOR])
    draw()


def delete_line(index: int):
    other_data[SCORE] += 1
    for line_index in range(index, 0, -1):
        for ceil_index in range(other_data[WIDTH_OF_FIELD]):
            play_field[line_index][ceil_index] = play_field[line_index - 1][ceil_index]
    another_one_line = check_is_line_ready()
    if another_one_line != -1:
        delete_line(another_one_line)


def reset_tetris_field():
    if check_is_tetra_fallen():
        for line in range(len(play_field)):
            for ceil in range(len(play_field[line])):
                if play_field[line][ceil] == 1:
                    play_field[line][ceil] = 0
        for line in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]])):
            for ceil in range(len(tetris[tetra_data[KIND]][tetra_data[STATE]][line])):
                if tetris[tetra_data[KIND]][tetra_data[STATE]][line][ceil] == 1:
                    play_field[line + tetra_data[Y_POS]][ceil + tetra_data[X_POS]] = 1
    else:
        for line in range(len(play_field)):
            for ceil in range(len(play_field[line])):
                if play_field[line][ceil] == 1:
                    play_field[line][ceil] = 2
        line_index = check_is_line_ready()

        if line_index != -1:
            delete_line(line_index)

        generate_tetra()


def finish_game():
    global play_field
    play_field = [[0 for i in range(other_data[WIDTH_OF_FIELD])] for i in range(other_data[HEIGHT_OF_FIELD] + 4)]
    other_data[PAUSE] = True
    other_data[SCORE] = 0
    pygame.mixer.music.pause()
    sound_lib[DEFEAT].play()
    start_game()


def start_game():
    is_game_running = True
    while is_game_running:

        # draw
        window.fill(other_data[BG_COLOR])

        draw()
        if other_data[PAUSE]:
            select_mode_btn.draw(window, position=(int((contains[EAST] - 325) / 2), int(contains[SOUTH] - 150) / 2))

        pygame.display.update()

        # quit
        for user_action in pygame.event.get():
            if user_action.type == pygame.QUIT:
                is_game_running = False
                pygame.QUIT()

        # is player defeted
        if check_is_game_ended():
            is_game_running = False

        # actions
        keys = pygame.key.get_pressed()
        if other_data[COMFORTABLE_TIME_STOP] >= 100:
            is_action_done = False
            if not other_data[PAUSE]:
                if keys[pygame.K_LEFT] and position_of_first_falling_square(WEST) > 0:
                    tetra_data[X_POS] -= 1
                    if not can_be_transformed():
                        tetra_data[X_POS] += 1
                    is_action_done = True
                if keys[pygame.K_RIGHT] and position_of_first_falling_square(EAST) < other_data[WIDTH_OF_FIELD] - 1:
                    tetra_data[X_POS] += 1
                    if not can_be_transformed():
                        tetra_data[X_POS] -= 1
                    is_action_done = True
                if keys[pygame.K_UP]:
                    is_action_done = True
                    turn()
            if keys[pygame.K_p]:
                if other_data[PAUSE]:
                    other_data[PAUSE] = False
                    pygame.mixer.music.unpause()
                else:
                    other_data[PAUSE] = True
                    pygame.mixer.music.pause()
                pygame.time.delay(350)
            if is_action_done:
                window.fill(other_data[BG_COLOR])
                draw()
                pygame.display.update()
                pygame.time.delay(250)
                continue
        if keys[pygame.K_DOWN] and not other_data[PAUSE]:
            other_data[COMFORTABLE_TIME_STOP] = 0
            tetra_data[SPEED] = 20
        # fall
        if position_of_first_falling_square(SOUTH) < other_data[HEIGHT_OF_FIELD] + 3 \
                and not other_data[PAUSE]:
            tetra_data[Y_POS_IN_CONCRETE_CEIL] += tetra_data[SPEED]
            if tetra_data[Y_POS_IN_CONCRETE_CEIL] >= other_data[CEIL_HEIGHT]:
                tetra_data[Y_POS] += 1
                tetra_data[Y_POS_IN_CONCRETE_CEIL] = 0

        if not other_data[PAUSE]:
            reset_tetris_field()

        pygame.time.delay(other_data[COMFORTABLE_TIME_STOP] // 10)
    finish_game()


window = pygame.display.set_mode((contains[EAST], contains[SOUTH]))
pygame.display.set_caption('tetris')

start_game()
