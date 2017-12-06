CNT_DAYS_A_PERIOD = 20
CNT_PERIOD = 6
CNT_FEATURE_OF_UNIT = 4

N_INPUT = CNT_PERIOD * CNT_FEATURE_OF_UNIT
N_OUTPUT = 2
SHAPE = [N_INPUT,
         16,
         16,
         16,
         N_OUTPUT
         ]

MODEL_PATH = '../../model/toothless.ckpt'
SUMMARY_PATH = '../../summary/'

DATA_PATH = None
DATA_DICT = None
PERIOD_DATA_DICT = None
TRAIN_DATA_DICT = None


