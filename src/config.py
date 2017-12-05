CNT_DAYS_A_PERIOD = 5
CNT_PERIOD = 20
CNT_FEATURE_OF_UNIT = 4

N_INPUT = CNT_PERIOD * CNT_FEATURE_OF_UNIT
N_OUTPUT = 2
SHAPE = [N_INPUT,
         96,
         128,
         144,
         144,
         144,
         128,
         96,
         64,
         32,
         16,
         8,
         4,
         N_OUTPUT
         ]

MODEL_PATH = '/model/toothless.ckpt'
SUMMARY_PATH = '../../summary/'

DATA_PATH = None
DATA_DICT = None
PERIOD_DATA_DICT = None
TRAIN_DATA_DICT = None


