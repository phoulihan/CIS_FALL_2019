# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:43:59 2019

@author: pathouli
"""

import os
import re
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/code/lecture/CIS_FALL_2019/data/topics/'

the_dir = os.listdir(the_path)

sw = stopwords.words('english')

the_stemmer = nltk.PorterStemmer()
the_stemmer.stem('cycling')

the_df = pd.DataFrame()
for word in the_dir:
    the_files = os.listdir(the_path + word)
    for tmp in the_files:
        tmp_path = the_path + word + '/' + tmp
        f = open(tmp_path, 'r', encoding="ISO-8859-1")
        the_text = f.readlines()
        the_text_final = ' '.join(the_text)
        the_text_final = [my_word for my_word in the_text_final.split() if my_word not in sw]
        the_text_final = [the_stemmer.stem(my_word) for my_word in the_text_final]
        the_text_final = ' '.join(the_text_final)
        clean_text = re.sub('[^A-z]+', ' ', the_text_final)
        if (len(clean_text) != 0):
            the_df = the_df.append({'the_body': clean_text, 'label': word}, ignore_index=True)
        f.close()
