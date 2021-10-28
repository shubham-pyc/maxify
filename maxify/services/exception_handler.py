import sys
import traceback


class ExceptionHander:
    def __init__(self):
        pass

    def handle_exception(self, exception):
        exc_type, exc_value, exc_tb = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_tb)
        # traceback.print_exception(file=sys.stdout)
        print(exception)
