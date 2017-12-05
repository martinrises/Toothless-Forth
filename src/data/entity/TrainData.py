from src.data.entity.PeriodData import PeriodData
import src.config as config


class TrainData:
    def __init__(self, data, next_data):
        self.data = data
        self.next_data = next_data

        self.period_data = []
        for i in range(len(self.data) - 1, -1, -config.CNT_DAYS_A_PERIOD):
            self.period_data.append(PeriodData(self.data[i - config.CNT_DAYS_A_PERIOD + 1: i + 1]))

    @property
    def features(self):
        features_arr = []
        for data in self.period_data:
            features_arr += data.features
        std_feature = self.data[-1].close
        return list(map(lambda f: f/std_feature, features_arr))

    @property
    def label(self):
        return [0, 1] if self.next_data[-1].close > self.data[-1].close else [1, 0]
