# Word_Vocab_Chk
The outcome of this work is to make a product to check plagiarism in documents submitted towards innovation hackathons.

Technologies employed in developing this product:

- Web Development
- RabinKarp String Search Algorithm
- Machine Learning


## Installation 



## Requirements

- Install Anaconda Prompt

#### Make sure you have these libraries before proceeding

- PyPDF2
- gensim
- nltk
- run an additional code as below on `IPython Console Window in Spyder` as:
      
      import nltk
      nltk.download('punkt')


## Modifications

In order to read and work with a custom pdf file, please proceed as follows :

1. Fetch the code `with open('2.pdf', 'rb') as pdf_file:` in `pdf-parser.py`
2. Replace the path of the PDF file with `2.pdf`. Make sure to put on quotes.


