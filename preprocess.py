import yaml
from data_process.data_process import data_process

config = yaml.load(open('config.yml'))
data_process(config)