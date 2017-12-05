class OriginRecord:
    def __init__(self, date, open, close, high, low, total_turnover, volume, limit_up, limit_down):
        self.date = date
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.total_turnover = total_turnover
        self.volume = volume
        self.limit_up = limit_up
        self.limit_down = limit_down
