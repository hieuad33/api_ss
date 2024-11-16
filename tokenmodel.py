from transformers import AutoModel, AutoTokenizer

class Tokenizer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
    def getmodel(self):
        return self.tokenizer