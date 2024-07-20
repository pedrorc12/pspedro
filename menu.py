import subprocess
import pygame
import time
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                 pygame.FULLSCREEN | pygame.SCALED
                                 )
pygame.display.set_caption('Pygame Menu Template')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (100, 100, 255)

# Font
font = pygame.font.Font(None, 74)

# Menu options
menu_options = ["Emulation Station", "Steam", "Firefox", "Exit"]
selected_option = 0

# Initialize joystick
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None


def draw_menu():
    screen.fill(BLACK)
    for i, option in enumerate(menu_options):
        if i == selected_option:
            color = HIGHLIGHT
            text = font.render(option, True, color)
            rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, rect)
        else:
            color = WHITE
            offset = i - selected_option
            text = font.render(option, True, color)
            rect = text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + offset * 100))
            screen.blit(text, rect)


def handle_input():
    global selected_option
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                execute_option()
        elif event.type == pygame.JOYBUTTONDOWN:
            # Assuming button 0 is the select button
            if joystick.get_button(0):
                execute_option()
        elif event.type == pygame.JOYHATMOTION:
            hat = joystick.get_hat(0)
            if hat[1] == 1:  # Up
                selected_option = (selected_option - 1) % len(menu_options)
            elif hat[1] == -1:  # Down
                selected_option = (selected_option + 1) % len(menu_options)


def execute_option():
    if menu_options[selected_option] == "Emulation Station":
        subprocess.run("es-de")
    elif menu_options[selected_option] == "Steam":
        subprocess.run("steam -gamepadui")
    elif menu_options[selected_option] == "Firefox":
        subprocess.run("firefox")
    elif menu_options[selected_option] == "Exit":
        pygame.quit()
        sys.exit()


def main():
    clock = pygame.time.Clock()
    while True:
        handle_input()
        draw_menu()
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
