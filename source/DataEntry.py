class DataEntry(object):
    def __init__(self, order_no, pd_value, into_default_flag):
        self.order_no = int(order_no)
        self.pd_value = float(pd_value)
        self.into_default_flag = int(into_default_flag)