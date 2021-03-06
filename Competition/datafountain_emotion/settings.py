# create by fanfan on 2020/3/13 0013
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
Data_path = os.path.join(PROJECT_ROOT,"data")
Output_path = os.path.join(PROJECT_ROOT,'output')
Model_save_path = os.path.join(Output_path,'tf_models')

train_origin_data_path = os.path.join(Data_path,'nCoV_100k_train.labled.csv')
test_origin_data_path = os.path.join(Data_path,"nCov_10k_test.csv")


train_data_path = os.path.join(Output_path,"train.csv")
dev_data_path = os.path.join(Output_path,'dev.csv')
test_data_path = os.path.join(Output_path,'test.csv')
submit_data_path = os.path.join(Output_path,'submit.csv')

label_list = ["-1","0","1"]

train_tfrecord_path = os.path.join(Output_path,'train.tf_record')
dev_tfrecord_path = os.path.join(Output_path,"dev.tf_record")
test_tfrecord_path = os.path.join(Output_path,'test.tf_record')



class ParamsModel():
    def __init__(self):
        self.max_seq_length = 150  #句子最大长度
        self.do_lower_case = True #是否区别大小写
        self.do_train = True
        self.do_eval = True
        self.do_predict = False
        self.num_train_steps = 20000
        self.warmup_step = 200
        self.save_checkpoints_steps = 300 #每训练多少步，保存一次模型
        self.max_steps_without_decrease = 2000 #最大多少步没有提升就退出
        self.learning_rate = 0.0001
        self.use_one_hot_embeddings= False
        self.optimizer = 'adamw'


        self.train_batch_size = 128
        self.buffer_size = self.train_batch_size * 300

        self.num_tags = len(label_list)

        self.vocab_size = None
        self.embedding_size = None
        self.dropout = 0.8


        # bi lstm
        self.hidden_size = 256
        self.layer_num = 1
        self.use_attention = True
        self.attention_size = 256


import sys
if 'win' in sys.platform:
    bert_model_path = r'E:\nlp-data\nlp_models\albert_tiny_zh_google'
else:
    bert_model_path = r'/data/python_project/qiufengfeng/albert_zh/prev_trained_model/albert_tiny_zh_google'
bert_model_vocab_path = os.path.join(bert_model_path,'vocab.txt')
bert_model_init_path = os.path.join(bert_model_path,'albert_model.ckpt')
bert_model_config_path = os.path.join(bert_model_path,"albert_config_tiny_g.json")