from src.output.view.view_object import ViewObject


class Button(ViewObject):
    """
    Visual object representing a clickable button\n
    When clicked: call function defined by set_on_click_listener(self, on_click)\n

    :author: Mikael Holmbom
    :version: 1.0
    """
    dimen               = None
    # function to call on this button click
    __on_click          = None

    def __init__(self, surface_layer, dimen=None):
        """

        """
        ViewObject.__init__(self, surface_layer)
        self.__dimen = dimen
        if dimen.x is not None and dimen.y is not None:
            self.set_pos(dimen.x, dimen.y)

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

