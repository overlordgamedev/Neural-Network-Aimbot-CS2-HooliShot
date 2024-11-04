import json
from flask import Flask, render_template, request, jsonify
from config_initialization import load_config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cs2')
def cs2():
    return render_template('cs2.html')


@app.route('/default')
def default():
    return render_template('default.html')


# Маршрут для получения конфигурации
@app.route('/get_config', methods=['GET'])
def get_config():
    return jsonify(load_config()), 200


# Маршрут для обновления конфигурации
@app.route('/update_config', methods=['POST'])
def update_config():
    # Открытие файла конфига и его чтение
    config_data = load_config()

    # Обновление значений в конфигурации, если они есть в запросе
    config_data['game'] = request.json.get('game', config_data['game'])

    config_data['screen_width'] = int(request.json.get('screen_width', config_data['screen_width']))
    config_data['screen_height'] = int(request.json.get('screen_height', config_data['screen_height']))

    config_data['fov_width'] = int(request.json.get('fov_width', config_data['fov_width']))
    config_data['fov_height'] = int(request.json.get('fov_height', config_data['fov_height']))

    config_data['aim_step'] = int(request.json.get('aim_step', config_data['aim_step']))
    config_data['aim_time_sleep'] = float(request.json.get('aim_time_sleep', config_data['aim_time_sleep']))
    config_data['aim_target'] = float(request.json.get('aim_target', config_data['aim_target']))

    config_data['anti_recoil_px'] = int(request.json.get('anti_recoil_px', config_data['anti_recoil_px']))
    config_data['anti_recoil_time_sleep'] = float(
        request.json.get('anti_recoil_time_sleep', config_data['anti_recoil_time_sleep']))

    config_data['draw_box_valid'] = bool(request.json.get('draw_box_valid', config_data['draw_box_valid']))
    config_data['box_color'] = {
        'r': int(request.json.get('box_color', {}).get('r', config_data['box_color']['r'])),
        'g': int(request.json.get('box_color', {}).get('g', config_data['box_color']['g'])),
        'b': int(request.json.get('box_color', {}).get('b', config_data['box_color']['b']))
    }

    config_data['draw_fov_valid'] = bool(request.json.get('draw_fov_valid', config_data['draw_fov_valid']))
    config_data['fov_color'] = {
        'r': int(request.json.get('fov_color', {}).get('r', config_data['fov_color']['r'])),
        'g': int(request.json.get('fov_color', {}).get('g', config_data['fov_color']['g'])),
        'b': int(request.json.get('fov_color', {}).get('b', config_data['fov_color']['b']))
    }

    config_data['draw_fps_valid'] = bool(request.json.get('draw_fps_valid', config_data['draw_fps_valid']))
    config_data['fps_color'] = {
        'r': int(request.json.get('fps_color', {}).get('r', config_data['fps_color']['r'])),
        'g': int(request.json.get('fps_color', {}).get('g', config_data['fps_color']['g'])),
        'b': int(request.json.get('fps_color', {}).get('b', config_data['fps_color']['b']))
    }

    config_data['cs2_screen_width'] = int(request.json.get('cs2_screen_width', config_data['cs2_screen_width']))
    config_data['cs2_screen_height'] = int(request.json.get('cs2_screen_height', config_data['cs2_screen_height']))

    config_data['cs2_fov_width'] = int(request.json.get('cs2_fov_width', config_data['cs2_fov_width']))
    config_data['cs2_fov_height'] = int(request.json.get('cs2_fov_height', config_data['cs2_fov_height']))

    config_data['cs2_aim_step'] = int(request.json.get('cs2_aim_step', config_data['cs2_aim_step']))
    config_data['cs2_aim_time_sleep'] = float(request.json.get('cs2_aim_time_sleep', config_data['cs2_aim_time_sleep']))
    config_data['cs2_aim_target'] = float(request.json.get('cs2_aim_target', config_data['cs2_aim_target']))

    config_data['cs2_obj_detection'] = request.json.get('cs2_obj_detection', config_data['cs2_obj_detection'])

    config_data['cs2_macros_gun'] = request.json.get('cs2_macros_gun', config_data['cs2_macros_gun'])
    config_data['cs2_macros_ak_47_adjustment'] = float(
        request.json.get('cs2_macros_ak_47_adjustment', config_data['cs2_macros_ak_47_adjustment']))

    config_data['cs2_draw_box_valid'] = bool(request.json.get('cs2_draw_box_valid', config_data['cs2_draw_box_valid']))
    config_data['cs2_box_color'] = {
        'r': int(request.json.get('cs2_box_color', {}).get('r', config_data['cs2_box_color']['r'])),
        'g': int(request.json.get('cs2_box_color', {}).get('g', config_data['cs2_box_color']['g'])),
        'b': int(request.json.get('cs2_box_color', {}).get('b', config_data['cs2_box_color']['b']))
    }

    config_data['cs2_draw_fov_valid'] = bool(request.json.get('cs2_draw_fov_valid', config_data['cs2_draw_fov_valid']))
    config_data['cs2_fov_color'] = {
        'r': int(request.json.get('cs2_fov_color', {}).get('r', config_data['cs2_fov_color']['r'])),
        'g': int(request.json.get('cs2_fov_color', {}).get('g', config_data['cs2_fov_color']['g'])),
        'b': int(request.json.get('cs2_fov_color', {}).get('b', config_data['cs2_fov_color']['b']))
    }

    config_data['cs2_draw_fps_valid'] = bool(request.json.get('cs2_draw_fps_valid', config_data['cs2_draw_fps_valid']))
    config_data['cs2_fps_color'] = {
        'r': int(request.json.get('cs2_fps_color', {}).get('r', config_data['cs2_fps_color']['r'])),
        'g': int(request.json.get('cs2_fps_color', {}).get('g', config_data['cs2_fps_color']['g'])),
        'b': int(request.json.get('cs2_fps_color', {}).get('b', config_data['cs2_fps_color']['b']))
    }

    # Перезапись файла конфигурации
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

    # Возвращаем JSON-ответ с обновленными данными
    return jsonify(config_data), 200
