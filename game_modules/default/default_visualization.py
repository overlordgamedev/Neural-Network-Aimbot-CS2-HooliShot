import pygame
import win32api
import win32con
import win32gui

from config_initialization import load_config

screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE)


def pygame_initialization():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((load_config("screen_width"), load_config("screen_height")), pygame.HWSURFACE)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def draw_box(box_cord):
    x1, y1, x2, y2 = map(int, box_cord)
    pygame.draw.rect(
        screen,
        (load_config("box_color")['r'], load_config("box_color")['g'], load_config("box_color")['b']),
        [
            x1 + load_config("screen_width") // 2 - load_config("fov_width") // 2,
            y1 + load_config("screen_height") // 2 - load_config("fov_height") // 2,
            x2 - x1,
            y2 - y1
        ],
        1
    )


def draw_fov():
    pygame.draw.rect(
        screen,
        (load_config("fov_color")['r'], load_config("fov_color")['g'], load_config("fov_color")['b']),
        [load_config("screen_width") // 2 - load_config("fov_width") // 2,
         load_config("screen_height") // 2 - load_config("fov_height") // 2,
         load_config("fov_width"), load_config("fov_height")],
        1)


# Функция для отрисовки текста (FPS)
def draw_fps(fps):
    font = pygame.font.Font('freesansbold.ttf', 32)
    font_text = font.render(
        'FPS: ' + fps,
        True,
        (load_config("fps_color")['r'], load_config("fps_color")['g'], load_config("fps_color")['b']),
        (0, 0, 0))
    text_rect = font_text.get_rect()
    text_rect.center = (75, 25)
    screen.blit(font_text, text_rect)

