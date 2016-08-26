from src.activable import Activable


class EventHandler(Activable):
    """
    EventHandler defines procedures of handling incoming pygame.event.Event instances and parse them into use-case logic\n
    Depending on the incoming event, the EventHandler can deligate tasks to a Controller instance\n
    :See: _get_interface()

    :author: Mikael Holmbom
    :version: 1.0
    """

    __controller        = None

    def __init__(self):
        """

        :param interface:
        :type interface: src.interface.Interface
        """
        self.start()

    def handle(self, event):
        """
        handle a incoming event if this eventhandler is active\n
        :param event: single event to handle
        :type event: pygame.event.Event
        :return: None
        """
        if not self.is_active():
            return

    def repeated_tasks(self):
        """
        tasks which proceed independent of events\n
        :return:
        """
        pass

    def set_controller(self, controller):
        """
        set this controller\n
        :param controller:
        :return:
        """
        self.__controller = controller


    def get_controller(self):
        """
        get this controller\n
        :return:
        """
        return self.__controller