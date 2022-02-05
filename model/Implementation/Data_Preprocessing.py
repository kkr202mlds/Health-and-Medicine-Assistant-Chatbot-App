from Data_load_with_file import intents
from nltk_utils import tokenize, stem, bag_of_words


all_words = []
tags = []
xy = []
sentences = []
true_tags = []

for intent in intents['intents']:
    tag = intent['tags']
    tags.append(tag)
    for pattern in intent['patterns']:
        sentences.append(pattern)
        true_tags.append(tag)
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '.', '!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(len(xy), "patterns")
print(len(tags), "tags:", tags)
print(len(sentences), "sentences:", sentences)
print(len(true_tags), "true_tags:", true_tags)
print(len(all_words), "unique stemmed words:", all_words)


tag_samples = {}

for w, tag in xy:
  if tag in tags:
    if tag not in tag_samples.keys():
      tag_samples[tag] = 1
    else:
      tag_samples[tag] += 1
print (tag_samples)


import pandas as pd
sample_f = pd.DataFrame.from_dict(tag_samples, orient='index', columns=['no_samples'])
sample_f.head()
