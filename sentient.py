from transformers import pipeline
import os
import json
import unicodedata


import pandas as pd
import numpy as np

import en_core_web_sm
nlp = en_core_web_sm.load()

# Importing hugging face model
sentiment_pipeline = pipeline("sentiment-analysis")
specific_model = pipeline(
    model="finiteautomata/bertweet-base-sentiment-analysis")
