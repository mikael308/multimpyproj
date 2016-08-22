import pygame


class Interface:
    """
    Interface facade used for specific use-cases\n
    Interface contains parts:
        * Engine - contains data and logic for the current use-case
        * Output - used for outputting the state of the current use-case
        * EventHandler - contains procedure to handle events according to current use-case

    standard use procedure:\n
    * __init__(self)
    * setup(self)
    * run(self)

    :author: Mikael Holmbom
    :version: 1.0
    """

    """
    see class Output
    """
    __output        = None
    """
    see class EventHandler
    """
    __eventhandler  = None
    """
    see class Engine
    """
    __engine        = None

    def __init__(self):
        """

        """

    def run(self):
        """
        run this interface:\n
        while this engine is running and pygame is active: render this view and handle incoming events\n
        :return: None
        """

        eventhandler    = self.get_eventhandler()
        engine          = self.get_engine()
        out             = self.get_output()

        while engine.is_running() and pygame.display.get_init():

            out.render()

            for event in pygame.event.get():
                eventhandler.handle(event)

            eventhandler.repeated_tasks()

    def shutdown(self):
        """
        shutdown this current engine, output, and quits pygame\n
        :return:
        """
        self.get_engine().shutdown()
        self.get_output().close()
        pygame.quit()

    def back(self):
        """
        shutdown this current engine\n
        :return:
        """
        self.get_engine().shutdown()

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

    def _set_engine(self, engine):
        """
        set this engine\n
        :param engine: Engine instane
        :type engine: Engine
        :return: None
        """
        self.__engine = engine

    def get_output(self):
        """
        get this engine
        :return: this engine instance
        """
        return self.__output

    def get_eventhandler(self):
        """
        get this eventhandler
        :return: this eventhandler instance
        """
        return self.__eventhandler

    def get_engine(self):
        """
        get this engine
        :return: this engine instance
        """
        return self.__engine

    def setup(self):
        """
        setup this interface
        :return:
        """
        self.get_engine().setup()
        self.get_output().setup()