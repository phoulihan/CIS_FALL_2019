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
import nltk
from nltk.stem import WordNetLemmatizer 

the_path = 'C:/Users/pathouli/myStuff/academia/torhea/code/lecture/CIS_FALL_2019/data/topics/'

the_dir = os.listdir(the_path)

sw = stopwords.words('english')

the_stemmer = nltk.PorterStemmer()
the_lemma = WordNetLemmatizer()

#print (the_stemmer.stem('cycling'))
#print (the_stemmer.stem('cycle'))
#print (the_stemmer.stem('cycles'))
#
#print (the_lemma.lemmatize('cycling'))
#print (the_lemma.lemmatize('cycle'))
#print (the_lemma.lemmatize('cycles'))

the_df = pd.DataFrame()
for word in the_dir:
    the_files = os.listdir(the_path + word)
    for tmp in the_files:
        tmp_path = the_path + word + '/' + tmp
        f = open(tmp_path, 'r', encoding="ISO-8859-1")
        the_text = f.readlines()
        the_text_final = ' '.join(the_text)
        the_text_final = [my_word for my_word in the_text_final.split() if my_word not in sw]
        
        clean_text_stem_tmp = [the_stemmer.stem(my_word) for my_word in the_text_final]
        the_text_final_stem = ' '.join(clean_text_stem_tmp)
        clean_text_stem = re.sub('[^A-z]+', ' ', the_text_final_stem)
        
        clean_text_lemma = [the_lemma.lemmatize(my_word) for my_word in the_text_final]
        the_text_final_lemma = ' '.join(clean_text_lemma)
        clean_text_lemma = re.sub('[^A-z]+', ' ', the_text_final_lemma)
        
        if (len(clean_text_stem) != 0) and (len(clean_text_stem) != 0):
            the_df = the_df.append({'the_body_stem': clean_text_stem, 
                                    'the_body_lemma': clean_text_lemma,
                                    'label_value': word}, ignore_index=True)
        f.close()


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

the_label = the_df.label_value

#lemmatization and stem transformation vectorizer
vectorizer = CountVectorizer()
the_vec = vectorizer.fit_transform(the_df.the_body_lemma)
my_vec_lemma = pd.DataFrame(the_vec.toarray())
my_vec_lemma.columns = vectorizer.vocabulary_


my_vec_stem = pd.DataFrame(vectorizer.fit_transform(the_df.the_body_stem).toarray())
my_vec_stem.columns = vectorizer.vocabulary_

from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

clf = svm.SVC(gamma='scale')
#clf = RandomForestClassifier(n_estimators=32, max_depth=16, random_state=0)
clf.fit(my_vec_stem[my_vec_stem.columns.difference(['label_value'])], the_label)
#print(clf.feature_importances_)

the_text = 'machine learning is fun'

my_sample = vectorizer.transform([the_text]).toarray()

print(clf.predict(my_sample))


#lemmatization and stem transformation tf-idf
tf_idf = TfidfVectorizer()
my_tf_idf_lemma = pd.DataFrame(tf_idf.fit_transform(the_df.the_body_lemma).toarray())
my_tf_idf_lemma.columns = tf_idf.vocabulary_
my_tf_idf_lemma['label'] = the_df.label

my_tf_idf_stem = pd.DataFrame(tf_idf.fit_transform(the_df.the_body_stem).toarray())
my_tf_idf_stem.columns = tf_idf.vocabulary_


