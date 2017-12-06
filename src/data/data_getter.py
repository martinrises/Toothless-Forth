import pandas as pd
from src.data.entity.OriginRecord import OriginRecord
from src.data.entity.TrainData import TrainData
import os
import src.config as config


def get_origin_data_dict(path="../../data/origin/"):
    if path == config.DATA_PATH and config.DATA_DICT is not None:
        return config.DATA_DICT
    else:
        config.DATA_PATH = path

    file_list = os.listdir(path)
    data_dict = {}
    for csv_file in file_list:
        df = pd.read_csv(os.path.join(path, csv_file))
        df.columns = ['date', 'open', 'close', 'high', 'low', 'total_turnover', 'volume', 'limit_up', 'limit_down']
        length = df.shape[0]
        records = []
        for i in range(length):
            records.append(OriginRecord(df.date[i],
                                        df.open[i],
                                        df.close[i],
                                        df.high[i],
                                        df.low[i],
                                        df.total_turnover[i],
                                        df.volume[i],
                                        df.limit_up[i],
                                        df.limit_down[i]
                                        ))
        data_dict[csv_file] = records
        print('get_origin_data_dict ,progress >>> {:.2f}%'.format(len(data_dict.keys()) * 100 / len(file_list)))
        config.DATA_DICT = data_dict
    return data_dict


def convert_origin_data_to_training_data(origin_datas, weeks):
    training_data = []
    for i in range(weeks * config.CNT_DAYS_A_PERIOD - 1, len(origin_datas)-config.CNT_DAYS_A_PERIOD):
        training_data.append(TrainData(origin_datas[i - weeks * config.CNT_DAYS_A_PERIOD + 1:i+1],
                                       origin_datas[i+1: i+config.CNT_DAYS_A_PERIOD+1]))
    return training_data


def get_train_data_dict(path="../../data/origin/", weeks=config.CNT_PERIOD):
    if path == config.DATA_PATH and config.TRAIN_DATA_DICT is not None:
        return config.TRAIN_DATA_DICT
    else:
        config.DATA_PATH = path
    origin_data_dict = get_origin_data_dict(path)
    train_data_dict = {order_id: convert_origin_data_to_training_data(data_list, weeks) for order_id, data_list in
                       origin_data_dict.items()}
    config.TRAIN_DATA_DICT = train_data_dict
    return train_data_dict


def get_test_ids(bind_data_dict):
    items = bind_data_dict.items()
    items = list(sorted(items, key=lambda item: len(item[1])))
    test_ids = []
    test_data_size = 0
    for i in range(-1, -len(items), -1):
        if test_data_size >= 2000:
            break
        test_data_size += len(items[i][1])
        test_ids.append(items[i][0])
    return test_ids


def get_all_data_set(weeks, path="../../data/origin/"):
    train_data_dict = get_train_data_dict(path, weeks)
    all_data = []
    for _, datas in train_data_dict.items():
        all_data += datas
    return [data.features for data in all_data], [data.label for data in all_data]


def get_training_data_set(weeks, path="../../data/origin/"):
    train_data_dict = get_train_data_dict(path, weeks)
    test_ids = get_test_ids(train_data_dict)
    training_data = []
    for id, datas in train_data_dict.items():
        if id not in test_ids:
            training_data += datas
    return [data.features for data in training_data], [data.label for data in training_data]


def get_test_data_set(weeks, path="../../data/origin/"):
    train_data_dict = get_train_data_dict(path, weeks)
    test_ids = get_test_ids(train_data_dict)
    test_data = []
    for id, datas in train_data_dict.items():
        if id in test_ids:
            test_data += datas
    return [data.features for data in test_data], [data.label for data in test_data]


if __name__ == "__main__":
    tmp = get_test_data_set(config.CNT_PERIOD)
    print(tmp[1])

