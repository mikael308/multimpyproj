from src.activable import Activable


class EventHandler(Activable):
    """
    EventHandler defines procedures of handling incoming pygame.event.Event instances and parse them into use-case logic\n
    Depending on the incoming event, the EventHandler can deligate tasks to a Interface\n
    :See: _get_interface()

    :author: Mikael Holmbom
    :version: 1.0
    """

    __interface         = None

    def __init__(self, interface):
        """

        :param interface:
        :type interface: src.interface.Interface
        """
        self.__interface = interface
        self.start()

    def _get_interface(self):
        """
        gets this interface\n
        :return:
        """
        return self.__interface

    def handle(self, event):
        """
        handle a incoming event\n
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
