import time
import win32api
import win32con
from config_initialization import load_config
from game_modules.cs2 import cs2_macros_list

anti_recoil_x = 0
anti_recoil_y = 0


def aim(dx, dy):
    dx += anti_recoil_x
    dy += anti_recoil_y

    aim_step_x = dx / load_config("cs2_aim_step")
    aim_step_y = dy / load_config("cs2_aim_step")

    for i in range(load_config("cs2_aim_step")):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(aim_step_x), int(aim_step_y), 0, 0)
        time.sleep(load_config("cs2_aim_time_sleep"))


def anti_recoil():
    global anti_recoil_x, anti_recoil_y
    # Создаем словарь для хранения данных
    macros_dict = {}

    # Получаем все переменные и их значения из cs2_macros_list и записываем их в словарь
    for weapon in dir(cs2_macros_list):
        macros_dict[weapon] = getattr(cs2_macros_list, weapon)

    # Основной цикл антиотдачи
    while True:
        # Если в словаре (macros_dict) берется ключ с названием как в переменной load_config("cs2_macros_gun"), то
        # значения этого ключа записываются в переменные x, y, delay"""
        for x, y, delay in macros_dict[load_config("cs2_macros_gun")]:
            x = round(x * load_config(f"cs2_macros_{load_config('cs2_macros_gun')}_adjustment"))
            y = round(y * load_config(f"cs2_macros_{load_config('cs2_macros_gun')}_adjustment"))
            """Проверка на нажатие левой кнопки мыши"""
            if 0 > win32api.GetKeyState(win32con.VK_LBUTTON):
                anti_recoil_x += x
                anti_recoil_y += y
                """Пауза на время указанное в переменной delay для антиотдачи"""
                time.sleep(delay)  # Используем задержку из антиотдачи
            else:
                # Сбрасываем смещение антиотдачи, когда кнопка отпущена
                anti_recoil_x = 0
                anti_recoil_y = 0
                break  # Прерываем цикл, если кнопка мыши была отпущена
