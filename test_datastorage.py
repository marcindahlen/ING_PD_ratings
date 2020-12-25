from source.DataStorage import DataStorage

datastorage = DataStorage()

datastorage.load_data()

datastorage.sort_data()

if datastorage.data[0].pd_value < datastorage.data[1].pd_value:
    print("test datastorage OK")
else:
    print("test datastorage FAIL")