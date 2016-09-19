import pygame


class Interface:
    """
    Interface facade used for specific use-cases\n
    Interface contains parts:
        * Controller - contains data and logic for the current use-case
        * Output - used for outputting the state of the current use-case
        * EventHandler - contains procedure to handle events according to current use-case

    standard use procedure:\n
    * __init__(self)
    * setup(self)
    * run(self)
    * shutdown(self)


    :author: Mikael Holmbom
    :version: 1.0
    """

    __output        = None

    __eventhandler  = None

    __controller        = None

    def __init__(self):
        """

        """
        pass

    def display(self):
        """
        display this interface\n
        :return: None
        """
        self.setup()
        self.run()

    def maindisplay(self):
        """
        display this interface, then shut down window\n
        :return: None
        """
        self.display()
        self.shutdown()

    def run(self):
        """
        run this interface:\n
        while this controller is running and pygame is active: render this view and handle incoming events\n
        :return: None
        """

        eventhandler    = self.get_eventhandler()
        controller      = self.get_controller()
        out             = self.get_output()

        while controller.is_active()\
                and eventhandler.is_active()\
                and out.is_active()\
                and pygame.display.get_init():

            out.render()

            for event in pygame.event.get():
                eventhandler.handle(event)

            eventhandler.repeated_tasks()

    def shutdown(self):
        """
	shutdown this current controller, output\n
	:return: None
        """
        self.get_controller().shutdown()
        self.get_output().shutdown()

    def _set_output(self, output):
        """
        set this view\n
        :param output: Output instance
        :type output: Output
        :return: None
        """
        self.__output = output

    def _set_eventhandler(self, eventhandler):
        """
        set this eventhandler\n
        :param eventhandler: EventHandler instance
        :type eventhandler: EventHandler
        :return: None
        """
        self.__eventhandler = eventhandler

    def _set_controller(self, controller):
        """
        set this controller\n
        :param controller: Controller instane
        :type controller: Controller
        :return: None
        """
        self.__controller = controller

    def get_output(self):
        """
        get this controller
        :return: this controller instance
        """
        return self.__output

    def get_eventhandler(self):
        """
        get this eventhandler
        :return: this eventhandler instance
        """
        return self.__eventhandler

    def get_controller(self):
        """
        get this controller
        :return: this controller instance
        """
        return self.__controller

    def setup(self):
        """
        setup this interface
        :return:
        """
        self.get_controller().setup()
        self.get_output().setup()
