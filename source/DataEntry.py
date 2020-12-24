class DataEntry(object):
    def __init__(self, order_no, pd_value, into_default_flag):
        self.order_no = order_no
        self.pd_value = pd_value
        self.into_default_flag = into_default_flag
        self.dummy_value = None