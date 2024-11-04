import os
import threading
import cv2
import pygame
import torch
import win32api
import win32con
from ultralytics import YOLO
import dxcam
from config_initialization import load_config
from game_modules.cs2.cs2_mouse_emulated import aim, anti_recoil
from game_modules.cs2.cs2_visualization import pygame_initialization, screen, draw_box, draw_fov, draw_fps


def cuda_initialization():
    global model
    # Определение устройства (GPU или CPU)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    if torch.cuda.is_available():
        print("Используется CUDA")
    else:
        print("Используется CPU")

    model = YOLO(os.path.abspath("models\\cs2_model.pt"))
    model.to(device)
    print("Запущена нейронная сеть для игры CS2")


def screenshot():
    # load_config("cs2_screen_width") // 2 центр экрана по x
    # load_config("cs2_screen_height") // 2 центр экрана по y
    # load_config("cs2_screen_width") // 2 - load_config("cs2_fov_width") // 2 центр fov по x
    # load_config("cs2_screen_height") // 2 - load_config("cs2_fov_height") // 2 центр fov по y
    cuda_initialization()
    camera = dxcam.create()
    pygame_initialization()

    while True:
        # Обработка событий с окном, например клик по нему или закрытие, это нужно чтобы не крашило
        pygame.event.pump()
        frame = camera.grab(region=(load_config("cs2_screen_width") // 2 - load_config("cs2_fov_width") // 2,
                                    load_config("cs2_screen_height") // 2 - load_config("cs2_fov_height") // 2,
                                    load_config("cs2_screen_width") // 2 - load_config("cs2_fov_width") // 2 +
                                    load_config("cs2_fov_width"), load_config("cs2_screen_height") // 2 -
                                    load_config("cs2_fov_height") // 2 + load_config("cs2_fov_height")))

        if frame is None:
            continue
        # Вызывается функция детекции
        detection(frame)


def detection(frame):
    start_timer = cv2.getTickCount()
    results = model.predict(frame, verbose=False)[0]
    screen.fill((0, 0, 0))
    if len(results.boxes) > 0:
        for box in results.boxes:
            if box.cls[0].item() in load_config("cs2_obj_detection"):
                box_cord = box.xyxy[0].tolist()
                center_x_obj = (box_cord[0] + box_cord[2]) / 2
                center_y_obj = (box_cord[1] + box_cord[3]) / 2
                center_x_obj += load_config("cs2_screen_width") // 2 - load_config("cs2_fov_width") // 2
                center_y_obj += load_config("cs2_screen_height") // 2 - load_config("cs2_fov_height") // 2
                center_y_obj -= (box_cord[3] - box_cord[1]) * load_config("cs2_aim_target")
                dx = center_x_obj - load_config("cs2_screen_width") // 2
                dy = center_y_obj - load_config("cs2_screen_height") // 2
                if 0 > win32api.GetKeyState(win32con.VK_LBUTTON):
                    aim(dx, dy)
                if load_config("cs2_draw_box_valid"):
                    draw_box(box_cord)
    if load_config("cs2_draw_fov_valid"):
        draw_fov()
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - start_timer)
    if load_config("cs2_draw_fps_valid"):
        draw_fps(str(int(fps)))
    pygame.display.update()


def start_game():
    anti_recoil_thread = threading.Thread(target=anti_recoil)
    anti_recoil_thread.start()
    screenshot()
