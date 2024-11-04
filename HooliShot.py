import asyncio
import threading
from config_initialization import load_config
from flask_initialization import app
from game_modules.cs2 import cs2
from game_modules.default import default



def game_initialization():
    if load_config("game") == "default":
        default.start_game()
    if load_config("game") == "cs2":
        cs2.start_game()


if __name__ == "__main__":
    flask_thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port="228", debug=True, use_reloader=False))
    flask_thread.start()

    game_initialization()
