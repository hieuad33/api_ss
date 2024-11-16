
import numpy as np
import pandas as pd
import re

def remove_punctuations(data):
    punct_tag=re.compile(r'[^\w\s]')
    data=punct_tag.sub(r'',data)
    return data


#Removes HTML syntaxes
def remove_html(data):
    html_tag=re.compile(r'<.*?>')
    data=html_tag.sub(r'',data)
    return data

#Removes URL data
def remove_url(data):
    url_clean= re.compile(r"https://\S+|www\.\S+")
    data=url_clean.sub(r'',data)
    return data
# Removes space
def remove_extra_spaces(s):
    s=s.strip()
    return re.sub(r'\s+', ' ', s)
#Removes Emojis
def remove_emoji(data):
    emoji_clean= re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    data=emoji_clean.sub(r'',data)
    url_clean= re.compile(r"https://\S+|www\.\S+")
    data=url_clean.sub(r'',data)
    return data

def Data_ex(z):
    z= remove_punctuations(z)
    z= remove_html(z)
    z= remove_url(z)
    z= remove_emoji(z)
    z= remove_extra_spaces(z)
    return z

from tokenmodel import Tokenizer
class datatoken:
   

    def __init__(self):
        tk= Tokenizer()
        self.model=tk.getmodel()       
    # Các phương thức
    def tokenize(self,data,max_len = 256):
        if (type(data)==str):
            encoded = self.model.encode_plus(data,
                                add_special_tokens = True,
                                max_length = max_len,
                                is_split_into_words=True,
                                return_attention_mask=True,
                                padding = 'max_length',
                                truncation=True,return_tensors = 'np')
        
            input_ids=encoded['input_ids']
            attention_mask=encoded['attention_mask']
        else:
            for i in tqdm(range(len(data))):
                encoded = self.model.encode_plus(data[i],
                                                add_special_tokens = True,
                                                max_length = max_len,
                                                is_split_into_words=True,
                                                return_attention_mask=True,
                                                padding = 'max_length',
                                                truncation=True,return_tensors = 'np')


                input_ids.append(encoded['input_ids'])
                attention_mask.append(encoded['attention_mask'])

        return np.vstack(input_ids),np.vstack(attention_mask)





from tqdm import tqdm
def tokenize(data,tokenizer,max_len = 256):
    y=np.array(data[target_cols])
    data=data.text
   
    input_ids = list()
    attention_mask = list()
    for i in tqdm(range(len(data))):
        encoded = tokenizer.encode_plus(data[i],
                                        add_special_tokens = True,
                                        max_length = MAX_LEN,
                                        is_split_into_words=True,
                                        return_attention_mask=True,
                                        padding = 'max_length',
                                        truncation=True,return_tensors = 'np')


        input_ids.append(encoded['input_ids'])
        attention_mask.append(encoded['attention_mask'])
    return np.vstack(input_ids),np.vstack(attention_mask),y