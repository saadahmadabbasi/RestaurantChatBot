from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.components import ComponentBuilder
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

builder = ComponentBuilder(use_cache=True)

def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file), builder)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='foodienlu')

def run_nlu():
    interpretor = Interpreter.load('models/nlu/default/foodienlu', builder)
    print(interpretor.parse('Can you suggest some hotels in Bangalore'))

if __name__ == '__main__':
    train_nlu('data/data.json', 'config_spacy.json', 'models/nlu')
    run_nlu()