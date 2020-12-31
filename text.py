import pygame as pyg
# The Screen is 1440x900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (25, 230, 230)
GOLD = (230, 230, 25)
DARKGREEN = (0, 153, 0)
DARKERGREEN = (0, 128, 0 )
DIE_SURFACE =   (204, 0, 0)
DIE_OUTLINE = (153, 0, 0)
PIP_COLOR = (224, 224, 235)
PIP_OUTLINE_COLOR = (193, 193, 215)

GRID = LIGHTBLUE

pyg.init()
clock = pyg.time.Clock()

screen = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)

font = pyg.font.Font("Oswald-Regular.ttf", 72)



x_cord = 20.5
y_cord = 18

done = False


def draw_grid():
    pyg.draw.line(screen, GRID, (720, 0), (720, 900), 3)
    pyg.draw.line(screen, GRID, (0, 450), (1440, 450), 3)
    horizontal = 0
    verticle = 0
    for x in range(50):
        pyg.draw.line(screen, GRID, (0, horizontal), (1440, horizontal))
        horizontal += 18
    for x in range(71):
        pyg.draw.line(screen, GRID, (verticle, 0), (verticle, 900))
        verticle += 20.57


def no_grid():
    pyg.draw.line(screen, DARKGREEN, (720, 0), (720, 900), 3)
    pyg.draw.line(screen, DARKGREEN, (0, 450), (1440, 450), 3)
    horizontal = 0
    verticle = 0
    for x in range(50):
        pyg.draw.line(screen, DARKGREEN, (0, horizontal), (1440, horizontal))
        horizontal += 18
    for x in range(71):
        pyg.draw.line(screen, DARKGREEN, (verticle, 0), (verticle, 900))
        verticle += 20.57


def draw_layout():
    # HIGH / LOW
    pyg.draw.rect(screen, GOLD, ((x_cord * 3), (y_cord * 2), (x_cord * 15 + 2.5), (y_cord * 10)), 5)  # HIGH
    font = pyg.font.Font("Oswald-Regular.ttf", 80)
    text = font.render('HIGH', True, WHITE)
    screen.blit(text, [x_cord * 6.8, y_cord * 3])
    font = pyg.font.Font("Oswald-Regular.ttf", 36)
    text = font.render('OVER 10', True, WHITE)
    screen.blit(text, [x_cord * 7.9, y_cord * 8])
    pyg.draw.rect(screen, GOLD, ((x_cord * 18), (y_cord * 2), (x_cord * 15 + 5), (y_cord * 10)), 5)  # LOW
    font = pyg.font.Font("Oswald-Regular.ttf", 80)
    text = font.render('LOW', True, WHITE)
    screen.blit(text, [x_cord * 22.2, y_cord * 3])
    font = pyg.font.Font("Oswald-Regular.ttf", 36)
    text = font.render('UNDER 11', True, WHITE)
    screen.blit(text, [x_cord * 22.1, y_cord * 8])

    # EVEN / ODD
    pyg.draw.rect(screen, GOLD, ((x_cord * 37 + 2.5), (y_cord * 2), (x_cord * 15 + 2.5), (y_cord * 10)), 5)  # EVEN
    font = pyg.font.Font("Oswald-Regular.ttf", 80)
    text = font.render('EVEN', True, WHITE)
    screen.blit(text, [x_cord * 41, y_cord * 3])
    pyg.draw.rect(screen, GOLD, ((x_cord * 52 + 2.5), (y_cord * 2), (x_cord * 15 + 5), (y_cord * 10)), 5)  # ODD
    font = pyg.font.Font("Oswald-Regular.ttf", 80)
    text = font.render('ODD', True, WHITE)
    screen.blit(text, [x_cord * 56.5, y_cord * 3])

    # FIELD
    pyg.draw.polygon(screen, GOLD, [[x_cord * 2, y_cord * 15],
                                    [x_cord * 68 + 5, y_cord * 15],
                                    [x_cord * 68 + 5, y_cord * 24],
                                    [x_cord * 45 + 5, y_cord * 24],
                                    [x_cord * 35 + 2.5, y_cord * 16],
                                    [x_cord * 25, y_cord * 24],
                                    [x_cord * 2, y_cord * 24]], 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 40)
    text = font.render('FIELD', True, WHITE)
    text = pyg.transform.rotate(text, 90)
    screen.blit(text, [x_cord * 2, y_cord * 17])
    font = pyg.font.Font("Oswald-Regular.ttf", 25)
    text = font.render('PAYS 1:1', True, WHITE)
    text = pyg.transform.rotate(text, 90)
    screen.blit(text, [x_cord * 4.3, y_cord * 16.8])
    font = pyg.font.Font("Oswald-Regular.ttf", 40)
    text = font.render('FIELD', True, WHITE)
    text = pyg.transform.rotate(text, -90)
    screen.blit(text, [x_cord * 65.8, y_cord * 17])
    font = pyg.font.Font("Oswald-Regular.ttf", 25)
    text = font.render('PAYS 1:1', True, WHITE)
    text = pyg.transform.rotate(text, -90)
    screen.blit(text, [x_cord * 64.6, y_cord * 16.8])
    font = pyg.font.Font("Oswald-Regular.ttf", 99)
    text = font.render('5  6  7  8                 13 14 15 16', True, WHITE)
    screen.blit(text, [x_cord * 8, y_cord * 15.5])
    pyg.draw.circle(screen, WHITE, (235, 345), 6)
    pyg.draw.circle(screen, WHITE, (333, 345), 6)
    pyg.draw.circle(screen, WHITE, (413, 345), 6)
    pyg.draw.circle(screen, WHITE, (983, 345), 6)
    pyg.draw.circle(screen, WHITE, (1098, 345), 6)
    pyg.draw.circle(screen, WHITE, (1213, 345), 6)

    # TRIPLE
    pyg.draw.polygon(screen, GOLD, [[x_cord * 45 + 5, y_cord * 24],
                                    [x_cord * 35 + 2.5, y_cord * 16],
                                    [x_cord * 25, y_cord * 24],
                                    [x_cord * 35 + 2.5, y_cord * 32],
                                    [x_cord * 45 + 5, y_cord * 24]], 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 55)
    text = font.render('ANY', True, WHITE)
    screen.blit(text, [x_cord * 33, y_cord * 17])
    font = pyg.font.Font("Oswald-Regular.ttf", 70)
    text = font.render('TRIPLE', True, WHITE)
    screen.blit(text, [x_cord * 30.8, y_cord * 20])
    font = pyg.font.Font("Oswald-Regular.ttf", 35)
    text = font.render('PAYS', True, WHITE)
    screen.blit(text, [x_cord * 33.5, y_cord * 25])
    font = pyg.font.Font("Oswald-Regular.ttf", 35)
    text = font.render('30 to 1', True, WHITE)
    screen.blit(text, [x_cord * 33, y_cord * 27])

    #1
    pyg.draw.rect(screen, GOLD, ((x_cord * 5), (y_cord * 24), (x_cord * 10 + 2.5), (y_cord * 20)), 5)  # BOX OUTLINE
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('1', True, WHITE)
    screen.blit(text, [x_cord * 8, y_cord * 25])
    #2
    pyg.draw.rect(screen, GOLD, ((x_cord * 15), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('2', True, WHITE)
    screen.blit(text, [x_cord * 18, y_cord * 25])
    #3
    pyg.draw.polygon(screen, GOLD, [[x_cord * 25, y_cord * 24],
                                    [x_cord * 35 + 2.5, y_cord * 32],
                                    [x_cord * 35 + 2.5, y_cord * 43.95],
                                    [x_cord * 25, y_cord * 43.95]], 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('3', True, WHITE)
    screen.blit(text, [x_cord * 28, y_cord * 28])
    #4
    pyg.draw.polygon(screen, GOLD, [[x_cord * 35 + 2.5, y_cord * 32],
                                    [x_cord * 45 + 2.5, y_cord * 24 + 1],
                                    [x_cord * 45 + 2.5, y_cord * 43.95],
                                    [x_cord * 35 + 2.5, y_cord * 43.95]], 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('4', True, WHITE)
    screen.blit(text, [x_cord * 38, y_cord * 28])
    #5
    pyg.draw.rect(screen, GOLD, ((x_cord * 45 + 2.5), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('5', True, WHITE)
    screen.blit(text, [x_cord * 48, y_cord * 25])
    #6
    pyg.draw.rect(screen, GOLD, ((x_cord * 55 + 2.5), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
    font = pyg.font.Font("Oswald-Regular.ttf", 200)
    text = font.render('6', True, WHITE)
    screen.blit(text, [x_cord * 58, y_cord * 25])


def one_picked(times=1):
    if times == 1:
        # single
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('1', True, WHITE)
        screen.blit(text, [x_cord * 8, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 8.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 8.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [5.8, 6, 6, 10.2, 10.4, 10.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('1', True, WHITE)
        screen.blit(text, [x_cord * 8, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 5.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 6),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 6),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 10.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 10.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 10.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [5.4, 5.6, 5.6, 8.6, 8.6, 11.6,11.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('5', True, WHITE)
        screen.blit(text, [x_cord * 48, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 5.4),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 5.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 5.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 8.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 8.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 11.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 11.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        # 1
        pyg.draw.rect(screen, GOLD, ((x_cord * 5), (y_cord * 24), (x_cord * 10 + 2.5), (y_cord * 20)), 5)  # BOX OUTLINE
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('1', True, WHITE)
        screen.blit(text, [x_cord * 8, y_cord * 25])


def two_picked(times=1):
    if times == 1:
        # single dice_x_cords = [18, 18.2, 18.2]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('2', True, WHITE)
        screen.blit(text, [x_cord * 18, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 18),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 18.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 18.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [15.8, 16, 16, 20.2, 20.4, 20.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('2', True, WHITE)
        screen.blit(text, [x_cord * 18, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 15.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 16),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 16),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 20.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 20.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 20.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [15.4, 15.6, 15.6, 18.6, 18.6, 21.6, 21.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('2', True, WHITE)
        screen.blit(text, [x_cord * 18, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 15.4),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 15.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 15.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 18.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 18.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 21.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 21.6),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        # 2
        pyg.draw.rect(screen, GOLD, ((x_cord * 15), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('2', True, WHITE)
        screen.blit(text, [x_cord * 18, y_cord * 25])


def three_picked(times=1):
    if times == 1:
        # single dice_x_cords = [28, 28.2, 28.2]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('3', True, WHITE)
        screen.blit(text, [x_cord * 28, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 28),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 28.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 28.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [25.8, 26, 26, 30.2, 30.4, 30.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('3', True, WHITE)
        screen.blit(text, [x_cord * 28, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 25.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 26),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 26),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 30.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 30.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 30.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [25.4, 25.6, 25.6, 28.6, 28.6, 31.6, 31.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('3', True, WHITE)
        screen.blit(text, [x_cord * 28, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 25.4 + 3),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 25.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 25.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 28.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 28.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 31.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 31.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        pyg.draw.polygon(screen, GOLD, [[x_cord * 25, y_cord * 24],
                                        [x_cord * 35 + 2.5, y_cord * 32],
                                        [x_cord * 35 + 2.5, y_cord * 43.95],
                                        [x_cord * 25, y_cord * 43.95]], 5)
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('3', True, WHITE)
        screen.blit(text, [x_cord * 28, y_cord * 28])


def four_picked(times=1):
    if times == 1:
        # single dice_x_cords = [38, 38.2, 38.2]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('4', True, WHITE)
        screen.blit(text, [x_cord * 38, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 38),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 38.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 38.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [35.8, 36, 36, 40.2, 40.4, 40.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('4', True, WHITE)
        screen.blit(text, [x_cord * 38, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 35.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 36),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 36),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 40.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 40.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 40.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [35.4, 35.6, 35.6, 38.6, 38.6, 41.6, 41.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('4', True, WHITE)
        screen.blit(text, [x_cord * 38, y_cord * 28])
        pyg.draw.rect(screen, GOLD, ((x_cord * 35.4 + 4),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 35.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 35.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 38.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 38.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 41.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 41.6 + 4),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        # 4
        pyg.draw.polygon(screen, GOLD, [[x_cord * 35 + 2.5, y_cord * 32],
                                        [x_cord * 45 + 2.5, y_cord * 24 + 1],
                                        [x_cord * 45 + 2.5, y_cord * 43.95],
                                        [x_cord * 35 + 2.5, y_cord * 43.95]], 5)
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('4', True, WHITE)
        screen.blit(text, [x_cord * 38, y_cord * 28])


def five_picked(times=1):
    if times == 1:
        # single dice_x_cords = [48, 48.2, 48.2]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('5', True, WHITE)
        screen.blit(text, [x_cord * 48, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 48),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 48.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 48.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [45.8, 46, 46, 50.2, 50.4, 50.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('5', True, WHITE)
        screen.blit(text, [x_cord * 48, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 45.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 46),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 46),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 50.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 50.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 50.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [45.4, 45.6, 45.6, 48.6, 48.6, 51.6, 51.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('5', True, WHITE)
        screen.blit(text, [x_cord * 48, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 45.4 + 3),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 45.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 45.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 48.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 48.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 51.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 51.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        # 5
        pyg.draw.rect(screen, GOLD, ((x_cord * 45 + 2.5), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('5', True, WHITE)
        screen.blit(text, [x_cord * 48, y_cord * 25])

def six_picked(times=1):
    if times == 1:
        # single dice_x_cords = [58, 58.2, 58.2]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('6', True, WHITE)
        screen.blit(text, [x_cord * 58, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 58),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 58.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 58.2),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 2:
        # double [55.8, 56, 56, 60.2, 60.4, 60.4]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('6', True, WHITE)
        screen.blit(text, [x_cord * 58, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 55.8),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 56),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 56),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
        pyg.draw.rect(screen, GOLD, ((x_cord * 60.2),
                                     (y_cord * 42), (x_cord * 4 + 3), (y_cord * 4.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 60.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 60.4),
                                            (y_cord * 42.3), (x_cord * 3.75), (y_cord * 4.25)), 4)
    elif times == 3:
        # triple [55.4, 55.6, 55.6, 58.6, 58.6, 61.6, 61.6]
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('6', True, WHITE)
        screen.blit(text, [x_cord * 58, y_cord * 25])
        pyg.draw.rect(screen, GOLD, ((x_cord * 55.4 + 3),
                                     (y_cord * 42), (x_cord * 9.25), (y_cord * 3.75)))
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 55.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 55.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 58.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 58.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
        pyg.draw.rect(screen, DIE_SURFACE, ((x_cord * 61.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)))
        pyg.draw.rect(screen, DIE_OUTLINE, ((x_cord * 61.6 + 3),
                                            (y_cord * 42.3), (x_cord * 2.75), (y_cord * 3.25)), 4)
    else:
        # 6
        pyg.draw.rect(screen, GOLD, ((x_cord * 55 + 2.5), (y_cord * 24), (x_cord * 10), (y_cord * 20)), 5)
        font = pyg.font.Font("Oswald-Regular.ttf", 200)
        text = font.render('6', True, WHITE)
        screen.blit(text, [x_cord * 58, y_cord * 25])


while not done:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            done = True
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                done = True
            if event.key == pyg.K_g:
                grid_on = True

        screen.fill(DARKGREEN)



        draw_layout()

    pyg.display.flip()
    clock.tick(60)

pyg.quit()
