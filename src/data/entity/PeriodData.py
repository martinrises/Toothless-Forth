class PeriodData:
    def __init__(self, datas):
        self.datas = datas

    @property
    def open(self):
        return self.datas[0].open

    @property
    def close(self):
        return self.datas[-1].close

    @property
    def high(self):
        return max([data.high for data in self.datas])

    @property
    def low(self):
        return min([data.low for data in self.datas])

    @property
    def features(self):
        return [self.open, self.close, self.high, self.low]

    @property
    def is_up(self):
        return bool(self.close > self.open)