from functools import reduce

from utils import variables
from source.DataStorage import DataStorage

class Optiparm(object):
    def __init__(self):
        self.results = []
        self.classes = range(1, variables.classes_no + 1)
        self.dummy_classes = [[] for c in self.classes]
        self.output_classes = []
        self.datastorage = DataStorage()
        self.datastorage.load_data()
        self.datastorage.sort_data()

    def init_classes(self):
        for i, c in enumerate(self.classes):
            bounds = self.get_class_bounds(i)
            self.dummy_classes[i] = self.datastorage.data[bounds[0]:bounds[1]]

    def write_output(self):
        output = self.give_output()

        for i, elem in enumerate(output):
            count = len(elem)
            lowest = min(elem, key=lambda x: x.pd_value)
            highest = max(elem, key=lambda x: x.pd_value)
            observed = reduce(lambda x, y: x.pd_value + y.pd_value, elem) / count
            print(f"{i:3} | {count:6} | {lowest:10} | {highest:10} | {observed:10}")

    def give_output(self):
        finish_flag = False
        considered_classes = self.dummy_classes
        while not finish_flag:
            finish_flag = True
            helper_list = []
            pair_scores = []
            for i in range(len(considered_classes) - 1):
                pair_scores.append(self.get_f_test_score(considered_classes[i], considered_classes[i+1]))
            lowest_test_score = min(pair_scores)

            if lowest_test_score < variables.confidence_interval:
                finish_flag = False
                helper_list = self.concacenate_classes(considered_classes, pair_scores, lowest_test_score)
            else:
                helper_list = considered_classes

            considered_classes = helper_list

        return considered_classes

    def concacenate_classes(self, considered_classes: list, pair_scores: list, lowest_test_score: float) -> list:
        concat_index = pair_scores.index(lowest_test_score)
        output_list = considered_classes[:concat_index]
        new_class = considered_classes[concat_index] + considered_classes[concat_index + 1]
        output_list.append(new_class)
        output_list.extend(considered_classes[concat_index + 2:])
        return output_list

    def get_class_bounds(self, i: int) -> tuple:
        return i * variables.classes_no, i * variables.classes_no + variables.classes_no

    def get_f_test_score(self, class_a: list, class_b: list) -> float:
        return self.get_variance(class_a) / self.get_variance(class_b)

    def get_mean(self, sample: list) -> float:
        length = len(sample)
        the_sum = sum(entry.pd_value for entry in sample)
        return the_sum / length

    def get_variance(self, sample: list) -> float:
        length = len(sample)
        mean = self.get_mean(sample)
        altered_sum = sum(map(lambda x: pow(x.pd_value - mean, 2), sample))
        return altered_sum / (length - 1)