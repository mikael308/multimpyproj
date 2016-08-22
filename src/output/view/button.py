import src.resource.resource as resource
from src.output.view.gameobjects.gameobject import GameObject


class Button(GameObject):
    """
    Visual object representing a clickable button\n
    When clicked: call function defined by set_on_click_listener(self, on_click)\n

    :author: Mikael Holmbom
    :version: 1.0
    """
    # function to call on this button click
    __on_click          = None

    def __init__(self, surface_layer, dimen=resource.get_dimen("button")):
        """

        """
        GameObject.__init__(self, surface_layer, dimen)

    def set_on_click_listener(self, on_click):
        """
        set function to call when this button is clicked\n
        :see: self.click()\n
        :param on_click: function to call when button is clicked
        :type on_click: function
        :return: this button instance
        """
        self.__on_click = on_click
        return self

    def click(self):
        """
        calls on_click function defined by set_on_click_listener(self, on_click_listener)\n
        :return: None
        """
        if self.__on_click is not None:
            self.__on_click()