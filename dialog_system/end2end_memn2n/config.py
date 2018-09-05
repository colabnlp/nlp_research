# create by fanfan on 2018/8/31 0031
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
edim = 20 #internal state dimension [20]")
nhop = 3 #number of hops [3]")
mem_size = 50 #maximum number of sentences that can be encoded into memory [50]")
batch_size = 32 #batch size to use during training [32]")
nepoch = 200 #number of epoch to use during training [100]")
anneal_epoch = 25 #anneal the learning rate every <anneal_epoch> epochs [25]")
babi_task = 1 #index of bAbI task for the network to learn [1]")
init_lr = 0.01 #initial learning rate [0.01]")
anneal_rate = 0.5 #learning rate annealing rate [0.5]")
init_mean = 0. #weight initialization mean [0.]")
init_std = 0.1 #weight initialization std [0.1]")
max_grad_norm = 40 #clip gradients to this norm [40]")
data_dir = os.path.join(ROOT_DIR,"data/bAbI/en-valid") #dataset directory [./bAbI/en_valid]")
checkpoint_dir = os.path.join(ROOT_DIR,"checkpoints") #checkpoint directory [./checkpoints]")
lin_start = False #True for linear start training, False for otherwise [False]")
is_test = True #True for testing, False for training [False]")
show_progress = False #print progress [False]")