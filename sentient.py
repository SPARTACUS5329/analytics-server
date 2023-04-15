# from transformers import pipeline
import numpy as np
import pandas as pd
import os
import json
import unicodedata


global A, B
A, B = 0.0026223464946062386, -0.017333561945556908


import en_core_web_sm
nlp = en_core_web_sm.load()

# Importing hugging face model
from transformers import pipeline
#sentiment_pipeline = pipeline("sentiment-analysis")
specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

rootdir = './FMP'


def sentient(symbol):
    result = []
    for i in os.listdir(rootdir):
        if i == symbol:
            for subdir, dirs, files in os.walk(rootdir + "/" + symbol):
                for file in files:
                    if file[-4:] == "json":
                        file_path = os.path.join(subdir, file)
                        data = json.load(open(file_path))
                        main = data['content']
                        main = str(unicodedata.normalize(
                            'NFKD', main).encode('ascii', 'ignore'))
                        text = nlp(main).ents
                        output = " ".join([str(x) for x in text])
                        final_score = 0
                        for i in range(len(output)//100):
                            res = specific_model(output[i*100:(i+1)*100])[0]
                            if res["label"] == 'POS':
                                final_score += (A * res['score'])
                            elif res["label"] == 'NEG':
                                final_score += (B * res['score'])
                        result.append([[subdir[-4:]] ,[final_score]])
            return (result)
    return ("Invalid Token")

