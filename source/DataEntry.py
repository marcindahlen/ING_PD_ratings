class DataEntry(object):
    def __init__(self, order_no, pd_value, into_default_flag):
        self.order_no = int(order_no) if type(order_no) is int else order_no
        self.pd_value = float(pd_value) if type(pd_value) is float else pd_value
        self.into_default_flag = int(into_default_flag) if type(into_default_flag) is int else into_default_flag
        self.dummy_value = None