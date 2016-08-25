import src.settings.settings as settings
from src.output.output import Output
from src.output.screen.game_screen import GameScreen
from src.output.sound.sound_controller import SoundController


class GameOutput(Output):
    """
    output facade used for use-case game\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def __init__(self, game_controller):
        Output.__init__(self)
        self._set_screen(GameScreen())
        self.get_screen().set_game_controller(game_controller)
        self.get_screen().get_infopanel().set_player(game_controller.get_player())

        self.get_btns()["SOUND"].set_on_click_listener(self.switch_sound_enabled)

        self._set_soundcontroller(SoundController())

    def level_up(self):
        """
        outputs level up
        :return:
        """
        self.get_soundcontroller().play("level_up")

    def score(self):
        """
        outputs score
        :return:
        """
        self.get_soundcontroller().play("score")

    def wrong_cpu(self):
        """
        outputs wrong cpu
        :return:
        """
        self.get_soundcontroller().play("wrong_cpu")

    def buffer_overflow(self):
        """
        outputs buffer overflow
        :return:
        """
        self.get_soundcontroller().play("buffer_overflow")

    def switch_sound_enabled(self):
        """
        switch the settings value of soundfc enabled
        :return:
        """
        self.get_btns()["SOUND"].switch()
        settings.switch_soundfx_enabled()
