from source.DataEntry import DataEntry
from utils import variables


class DataStorage(object):
    def __init__(self):
        self.data = []

    def load_data(self):
        with open(variables.datafile) as file_input:
            for line in file_input:
                if line == "\n":
                    continue
                line_content = line.split(',')
                if line_content[0] == '' or line_content[1] == '' or line_content[2] == '':
                    continue
                self.data.append(DataEntry(line_content[0], line_content[1], line_content[2]))
        self.data.pop(0)   # remove data header
        self.data.pop(-1)   # remove empty line at the end

    def sort_data(self):
        self.data = sorted(self.data, key=lambda entry: entry.pd_value)