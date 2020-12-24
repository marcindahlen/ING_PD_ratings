import math

from utils import variables
from source.DataStorage import DataStorage

class Optiparm(object):
    def __init__(self):
        self.results = []
        self.classes = range(1, variables.classes_no + 1)
        self.datastorage = DataStorage()
        self.datastorage.load_data()
        self.datastorage.sort_data()

    def init_classes(self):
        entries_amount = len(self.datastorage)
        for i in range(entries_amount):
            self.datastorage.data[i].dummy_value = self.get_class(i)

    def perform_f_tests(self):
        pass

    def give_output(self):
        pass

    def get_class(self, i):
        return math.floor(i / variables.classes_no) + 1