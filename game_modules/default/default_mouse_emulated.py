import time
import win32api
import win32con
from config_initialization import load_config


def aim(dx, dy):
    if 0 > win32api.GetKeyState(win32con.VK_LBUTTON):
        aim_step_x = dx / load_config("aim_step")
        aim_step_y = dy / load_config("aim_step")

        for i in range(load_config("aim_step")):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(aim_step_x), int(aim_step_y), 0, 0)
            time.sleep(load_config("aim_time_sleep"))


def anti_recoil():
    while True:
        if 0 > win32api.GetKeyState(win32con.VK_LBUTTON):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int(load_config("anti_recoil_px")), 0, 0)
            time.sleep(load_config("anti_recoil_time_sleep"))
