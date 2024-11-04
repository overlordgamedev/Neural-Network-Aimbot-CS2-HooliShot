import json
import time


def load_config(key=None, max_retries=3, delay=1):
    attempt = 0

    while attempt < max_retries:
        try:
            with open("config.json", 'r') as file:
                config = json.load(file)

            if key:
                return config.get(key)
            return config

        except (FileNotFoundError, json.JSONDecodeError) as e:
            attempt += 1
            if attempt >= max_retries:
                raise RuntimeError(f"Не удалось загрузить конфигурацию после {max_retries} попыток. Ошибка: {e}")
            else:
                print(f"Ошибка при загрузке конфигурации: {e}. Попытка {attempt} из {max_retries}.")
                time.sleep(delay)  # Задержка перед повторной попыткой