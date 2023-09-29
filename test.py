%%capture

# # install required libraries
# !pip3 install transformers[torch]                  # HuggingFace library for interacting with BERT (and multiple other models)
# !pip3 install datasets                      # HuggingFace library to process dataframes
# !pip3 install sentence-transformers         # library to use Sentence Similarity BERT
# !pip3 install bertviz                       # visualize BERT's attention weigths
# !pip3 install annoy                         # Spotify's library for finding nearest neighbours
# !pip3 install ipywidgets

# import torch
# data = [[1, 2],[3, 4]]
# x_data = torch.tensor(data)
# print(x_data)
import numpy
arr = np.array([[1,1],[2,2]])
arr.tofile('nptest.csv', sep = ',')
from spacy.lang.en import English
nlp = English()
doc = nlp('Hello world!')
row_list=[]
for token in doc:
    row_list.append([token.text])
np.array(row_list).tofile('spacytest.csv',sep=',')
