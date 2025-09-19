import random
import pandas as pd
import numpy as np
import json
from src.encryption_schemes import ENCRYPTION_SCHEMES
from src.encryptor import Encryptor

#generate a dataset
with open("data/words_dictionary.json") as f:
    words_dict = json.load(f)
corpus = pd.DataFrame(list(words_dict.keys()), columns=["word"])

def main():
    idx = 0
    for row in corpus.itertuples(index=False):
        word = str(row.word)
        seed = random.randint(1,20)
        encryptor = Encryptor(schemes=ENCRYPTION_SCHEMES,seed=seed)
        ciphed = encryptor.encrypt(word)

        corpus["cipher"] = ciphed
        idx += 1
        print(f"{idx}th word")

    print(corpus.head)

main()
