import pygame
import classes
import csv


## Initialize ##

pygame.init()
clock = pygame.time.Clock()


## Constants ##
CLICK_RECT = []
run_start = True
run_main_game = True
color_constants = {"red": (255, 0, 0), "yellow": (255, 255, 0), "black": (0, 0, 0), "blue": (0, 0, 255), "gray": (128, 128, 128), "green": (0, 255, 0), "orange": (255, 165, 0)}
if run_start:
    ## Create Window ##
    window = pygame.display.set_mode([722, 822])
    window.fill((255, 255, 255))
    pygame.display.set_caption("Menu")
    font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 25)
    font_small = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 20)
    text_col = (0, 0, 0)


    ## Test ##

    toggle_click = False
    settings_button = classes.Button("Settings", window.get_width() / 2 - 100, 466)
    #gamemode_button = classes.Button('Gamemode', window.get_width() / 2 - 150, 400)
    play_button = classes.Button("Play", window.get_width() / 2 - 100, 334)
    toggle_button = classes.Button("Arrow", window.get_width() / 2 - 140, 50)
    buttons = [settings_button, play_button]
    phrases = ["Play", "Settings", "Gamemode"]
    connect4 = ["C", "o", "n", "n", "e", "c", "t", " ", "F", "o", "u", "r"]
    colorloop = [(234, 23, 42), (0, 255, 255), (255, 255, 0), (255, 0, 255), (255, 255, 255), (0, 150, 0), (0, 0, 150)]


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))
def settings(button_inst, button_inst2, font, text_col, x, y):
    global toggle_click
    pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and button_inst.rect.collidepoint(pos):
        window.fill((173,216,230))
        button_inst2.draw(window)
        posit = pygame.mouse.get_pos()
        if button_inst2.button_click():

            toggle_click = True
            return toggle_click


## Main Loop 1, Menu ##
main_menu = True
active1 = False ## For Settings Color
active2 = False ## For Settings Color
color_inactive = (255, 255, 255)
color_active = (90, 90, 255)
current_color1 = color_inactive
current_color2 = color_inactive
text_color1 = "red"
text_color2 = "yellow"
while main_menu:
    mouse_pos = pygame.mouse.get_pos()
    mainmenu = classes.MainMenu(toggle_button, settings_button, play_button)
    mainmenu.settings_scene()
    while mainmenu.show_settings:
        mouse_pos = pygame.mouse.get_pos()
        ## Back Arrow ##
        arrow = pygame.image.load("images/arrow2.png")
        arrow = pygame.transform.scale(arrow, (80, 80))
        window.fill((173, 216, 230))
        window.blit(arrow, (0, 50))
        mainmenu.back_scene()

        ## Input Color Settings ##
        input_rect1 = pygame.Rect((window.get_width() / 2 - 150, 200), (300, 100))
        input_rect2 = pygame.Rect((window.get_width() / 2 - 150, 400), (300, 100))

        pygame.draw.rect(window, current_color1, input_rect1)
        pygame.draw.rect(window, current_color2, input_rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    current_color1 = color_active
                else:
                    active1 = False
                current_color1 = color_active if active1 else color_inactive
                if input_rect2.collidepoint(event.pos):
                    active2 = True
                    current_color2 = color_active
                else:
                    active2 = False
                current_color2 = color_active if active2 else color_inactive
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_BACKSPACE:
                        text_color1 = text_color1[:-1]
                    else:
                        text_color1 += event.unicode
                if active2:
                    if event.key == pygame.K_BACKSPACE:
                        text_color2 = text_color2[:-1]
                    else:
                        text_color2 += event.unicode
        txt_surface1 = font.render(text_color1, True, (0, 0, 0))
        width = max(100, txt_surface1.get_width())
        input_rect1.w = width
        window.blit(txt_surface1, (window.get_width() / 2 - input_rect1.w + 50, 225))

        txt_surface2 = font.render(text_color2, True, (0, 0, 0))
        width = max(100, txt_surface2.get_width())
        input_rect2.w = width
        window.blit(txt_surface2, (window.get_width() / 2 - input_rect2.w + 50, 425))

        choose_a_color = font.render("Choose a color", True, (0, 0, 0))
        valid_colors = font_small.render("red   yellow   black   blue", True, (0, 0, 0))
        valid_colors2 = font_small.render("gray   green   orange", True, (0, 0, 0))
        window.blit(choose_a_color, (window.get_width() / 2 - 180, 550))
        window.blit(valid_colors, (window.get_width() / 2 - 300, 620))
        window.blit(valid_colors2, (window.get_width() / 2 - 300, 670))
        pygame.display.flip()
    window.fill((173,216,230))
    titlefont = pygame.font.Font("fonts/GameCrack-5yWeV.ttf", 50)
    font_x, font_y = font.size("titlefont")
    for i in range(len(connect4)):
        if i >= 6:

            draw_text(connect4[i], titlefont, colorloop[i - 5], (window.get_width() / 2 - (font_x )) + (i * 35),
                      50)
        else:
            draw_text(connect4[i], titlefont, colorloop[i], window.get_width() / 2 - (font_x ) + (i * 35), 50)
    run = play_button.play(window)
    for button in buttons:
        if button.draw(window):
            if button.text == "Play":
                main_menu = False
    play_button.draw_text(window, font, text_col, button.x + 25 * 2, button.y + 13)
    settings_button.draw_text(window, font, text_col, button.x + 3, button.y + 145)


    if settings_button.button_click():
        tog = settings(settings_button, toggle_button, font, text_col, toggle_button.x, toggle_button.y)
        if tog:
            toggle_button.draw(window)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            tog = settings(settings_button, toggle_button, font, text_col, toggle_button.x, toggle_button.y)
            if event.type == pygame.K_SPACE:
                print("Pause")
        if event.type == pygame.QUIT:
            main_menu = False
            run_main_game = False
    pygame.display.flip()

player1_color = None
player2_color = None
player1_shown = None
player2_shown = None

try:
    player1_color = color_constants[text_color1]
    player1_shown = "images/" + text_color1 + "_piece.jpg"
except:
    player1_color = color_constants["red"]
    player1_shown = "images/red_piece.jpg"
    text_color1 = "red"
try:
    player2_color = color_constants[text_color2]
    player2_shown = "images/" + text_color2 + "_piece.jpg"
except:
    player2_color = color_constants["yellow"]
    player2_shown = "images/yellow_piece.jpg"
    text_color2 = "yellow"
def place_and_update_piece(player):
    mouse_pos = pygame.mouse.get_pos()
    for rect in CLICK_RECT:
        if rect[0].collidepoint(mouse_pos):
            for surface in classes.UPDATE_SURFACE:
                for i in range(5, -1, -1):
                    if 212 + i * 100 == surface[1][1] and rect[0][0] == surface[1][0] and not surface[0].modified:
                        x= rect[1][0]
                        y = surface[1][1]
                        if player == 1:
                            surface[0].update_image(player, x, y, player1_color, player2_color)
                            return True
                        if player == 2:
                            surface[0].update_image(player, x, y, player1_color, player2_color)
                            return True

def check_win(player):
    for surface in classes.UPDATE_SURFACE:
        ## Horizontal
        ind = classes.UPDATE_SURFACE.index(surface)
        x = surface[1][0]
        y = surface[0].y
        color = surface[0].color
        hor = False
        if surface[0].modified:
            hor = True
        hor2 = False
        hor3 = False
        hor4 = False
        for next in classes.UPDATE_SURFACE:
            next_x = next[1][0]
            next_y = next[0].y
            match = next[0].color
            if next_x == classes.UPDATE_SURFACE[ind][1][0] + 100 and next_y == y and next[0].modified and match == color:
                hor2 = True
            elif next_x == classes.UPDATE_SURFACE[ind][1][0] + 200 and next_y == y and next[0].modified and match == color:
                hor3 = True
            elif next_x == classes.UPDATE_SURFACE[ind][1][0] + 300 and next_y == y and next[0].modified and match == color:
                hor4 = True
        if hor and hor2 and hor3 and hor4:
            end_game(surface[0].color, player)
            return True

        ## Vertical
        vert = False
        if surface[0].modified:
            vert = True
        vert2 = False
        vert3 = False
        vert4 = False
        for next in classes.UPDATE_SURFACE:
            next_x = next[1][0]
            next_y = next[0].y
            match = next[0].color
            if next_y == classes.UPDATE_SURFACE[ind][0].y + 100 and next_x == x and next[0].modified and match == color:
                vert2 = True
            elif next_y == classes.UPDATE_SURFACE[ind][0].y + 200 and next_x == x and next[0].modified and match == color:
                vert3 = True
            elif next_y == classes.UPDATE_SURFACE[ind][0].y + 300 and next_x == x and next[0].modified and match == color:
                vert4 = True
        if vert and vert2 and vert3 and vert4:
            end_game(surface[0].color, player)
            return True

        ## Diagnol
        dia = False
        if surface[0].modified:
            dia = True
        dia2 = False
        dia3 = False
        dia4 = False
        for next in classes.UPDATE_SURFACE:
            x = next[1][0]
            y = next[0].y
            match = next[0].color
            if (x == classes.UPDATE_SURFACE[ind][1][0] + 100 or x == classes.UPDATE_SURFACE[ind][1][0] - 100) and y == classes.UPDATE_SURFACE[ind][0].y + 100 and next[0].modified and match == color:
                dia2 = True
            elif (x == classes.UPDATE_SURFACE[ind][1][0] + 200 or x == classes.UPDATE_SURFACE[ind][1][0] - 200) and y == classes.UPDATE_SURFACE[ind][0].y + 200 and next[0].modified and match == color:
                dia3 = True
            elif (x == classes.UPDATE_SURFACE[ind][1][0] + 300 or x == classes.UPDATE_SURFACE[ind][1][0] - 300) and y == classes.UPDATE_SURFACE[ind][0].y + 300 and next[0].modified and match == color:
                dia4 = True
        if dia and dia2 and dia3 and dia4:
            end_game(surface[0].color, player)
            return True
    return False

def update_scores():
    data = []
    with open ("player_scores.csv") as score:
        score_list = csv.reader(score)
        for x in score_list:
            data.append(x)

    request_player1 = input("Write your glorious name winner! ")
    request_player2 = input("Write your name loser :| ")
    total_names = []
    total_row = []
    first = True
    for row in data:
        if first:
            total_row.append(row)
            first = False
        else:
            total_names.append(row[0])
            total_names.append(row[3])
            if request_player1 == row[0] and request_player2 == row[3]:
                get_player1_data = [row[0], str(int(row[1]) + 1), row[2]]
                get_player2_data = [row[3], row[4], str(int(row[5]) + 1)]
                total_matches = [str(int(row[-1]) + 1)]
                total_row.append(get_player1_data + get_player2_data + total_matches)
            elif request_player1 == row[3] and request_player2 == row[0]:
                get_player1_data = [row[3], str(int(row[4]) + 1), row[5]]
                get_player2_data = [row[0], row[1], str(int(row[2]) + 1)]
                total_matches = [str(int(row[-1]) + 1)]
                total_row.append(get_player1_data + get_player2_data + total_matches)
            else:
                get_player1_data = [row[0], row[1], row[2]]
                get_player2_data = [row[3], row[4], row[5]]
                total_matches = [row[-1]]
                total_row.append(get_player1_data + get_player2_data + total_matches)

    if request_player1 not in total_names:
        get_player1_data = [request_player1, "1", "0"]
        get_player2_data = [request_player2, "0", "1"]
        total_matches = ["1"]
        total_row.append(get_player1_data + get_player2_data + total_matches)
    elif request_player2 not in total_names:
        get_player1_data = [request_player1, "1", "0"]
        get_player2_data = [request_player2, "0", "1"]
        total_matches = ["1"]
        total_row.append(get_player1_data + get_player2_data + total_matches)

    with open ("player_scores.csv", "w", newline='') as score:
        write = csv.writer(score)
        write.writerows(total_row)

def end_game(winner_color, player):
    if pygame.time.get_ticks() >= win_time + 100:
        global play
        play = False
        if winner_color == player1_color:
            winner = text_color1
            player = 1
        elif winner_color == player2_color:
            winner = text_color2
            player = 2
        win_sfx.play()
        print("\nPlayer", player, winner.upper(), "Wins!\n")
        update_scores()
        reset = input("\nReset round? (y/n)")
        if reset == "y":
            reset_round()
        else:
            quit()
def reset_round():
    for surface in classes.UPDATE_SURFACE:
        surface[0].reset()
    global play
    global win_time
    global player
    global turn
    play = True
    win_time = 0
    player = 1
    turn = 1
    print("\nBegin!\n" + "Turn", "(" + text_color1.upper() + ")", "(Red)")

if run_main_game:
    ## Main Loop 2, Game Normal##
    confirm = True
    play = True
    win_time = 0
    player = 1
    turn = 1
    print("\nBegin!\n" + "Turn", turn, "(" + text_color1.upper() + ")")

    ## Turn Counter ##
    show_turn = font.render("Turn:", True, (0, 0, 0))
    show_turn_number = font.render(str(turn), True, player1_color)

    piece = classes.Piece()
    piece.shown()
    game_board = classes.GameBoard(7, 6)
    place_sfx = pygame.mixer.Sound("sfx/chips1.ogg")
    win_sfx = pygame.mixer.Sound("sfx/win.ogg")
    bg_sfx = pygame.mixer.Sound("sfx/notBalatro.mp3")
    bg_sfx.play(-1)
    while run_main_game:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play:
                if place_and_update_piece(player):
                    if player == 1:
                        player = 2
                    else:
                        player = 1
                    turn += 1
                    print("Turn", turn, end=" ")
                    if player == 1:
                        print("(" + text_color1.upper() + ")")
                    elif player == 2:
                        print("(" + text_color2.upper() + ")")
        if play:
            x,y = pygame.mouse.get_pos()
            window.fill((255, 255, 255))

        ## Invisible Pieces for Collision
        if confirm:
            for surface in classes.INV_CLASS:
                r = window.blit(surface[0].surface, surface[1])
                if r not in CLICK_RECT:
                    CLICK_RECT.append((r, surface[1]))
            else:
                window.blits(classes.INV_SURFACE)


        ## Places Pieces & Game Board ##
        for surface in classes.UPDATE_SURFACE:
            #window.blit(surface[0].piece, (surface[0].x, surface[0].y))
            if surface[0].y < surface[0].max_y:
                window.blit(surface[0].piece, (surface[0].x, surface[0].y + 100 * ((surface[0].max_y - surface[0].y) / surface[0].max_y)))
                surface[0].y += 15
                if surface[0].y >= surface[0].max_y:
                    surface[0].y = surface[0].max_y
                    place_sfx.play()
            else:
                window.blit(surface[0].piece, (surface[0].x, surface[0].y))


        if turn % 2 == 1:
            show_turn_number = font.render(str(turn), True, player1_color)
        elif turn % 2 == 0:
            show_turn_number = font.render(str(turn), True, player2_color)
        window.blit(game_board.board, (0,200))
        ## Currect Piece ##
        piece.update_shown(player, player1_shown, player2_shown)
        window.blit(piece.piece, (x - piece.piece.get_width()/ 2, piece.piece.get_width()/ 2 - 20))
        if play and not check_win(player):
            win_time = pygame.time.get_ticks()
        window.blit(show_turn, (10,10))
        window.blit(show_turn_number, (130, 10))
        pygame.display.flip()
