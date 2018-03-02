# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:13:28 2018

@author: Biswajit Roy
"""

#program to read pdf

import PyPDF2
import gensim
import nltk
from nltk.tokenize import word_tokenize

#import gensim.models.word2vec as w2v



"""
stopword = []
with open('english','r') as stopword_file:
    stopword = stopword_file.read()
    
stopword = stopword.split('\n')
stopword = stopword[:len(stopword) - 1]
print(stopword)

"""

corpus_raw = u""
with open('2.pdf', 'rb') as pdf_file:
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    no_of_page = pdfReader.numPages
    print("Number of Pages in PDF = ",no_of_page)
    i = 0
    
    while i < no_of_page:
        pageObj = pdfReader.getPage(i)
        text = pageObj.extractText().replace('\n', ' ')
        i += 1
                      
        corpus_raw = corpus_raw + text
        
#    print(corpus_raw)
    
    
    """
    result  = word_tokenize(corpus_raw)
    print(result)
    
    """



    
model=gensim.models.Word2Vec(corpus_raw, min_count=3, size=1000)
#print(model.vocab())
print(model.most_similar("a"))      




        