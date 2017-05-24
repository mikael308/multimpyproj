
from testcase import TestCase
import src.tools
import tools as tools


class TestTools(TestCase):
    """
    test module tools\n

    :author: Mikael Holmbom
    :version: 1.0
    """

    def _run(self):
        self._test_dividerow()

    def _test_dividerow(self):
        """
        test the function of divide a text into rows\n
        """

        input = "klaatuveradanikto ksajflsdjf lsajdlfkjsadlkfjsa dlfkjsadflk jsdlfkjsdlfkj sdljf .ad. fsajfd .sadkjf .sd .saldkf jsdlkf sa.df asd.sajd fjsa.lkf j.sadjf .sdjf .sakldjf "

        for w in range(1, len(input) + 5):
            rows = src.tools.divide_to_rows(w, input)

            str_res = ""
            for row in rows:
                str_res += row

            if not input == str_res:
                raise ValueError("malformed result max_width:" + str(w) + " : " + str(str_res))




