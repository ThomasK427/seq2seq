import yaml
import os
from trainer.trainer import train

config = yaml.load(open('config.yml'))
os.environ["CUDA_VISIBLE_DEVICES"] = str(config['train']['gpu'])
train(config)