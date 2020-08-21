import os
import numpy as np
from collections import Counter
from sklearn import svm
from sklearn.metrics import accuracy_score

def make_Dictionary(root_dir):
    all_words = []
    emails = [os.path.join(root_dir,f) for f in os.listdir(root_dir)]
    for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words
    dictionary = Counter(all_words)
    list_to_remove = list(dictionary)

    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]

    dictionary = dictionary.most_common(3000)
    return dictionary

def extract_features(mail_dir):
    files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
    features_matrix = np.zeros((len(files),3000))
    train_labels = np.zeros(len(files))
    docID = 0
    for fil in files:
        with open(fil) as fi:
            for i,line in enumerate(fi):
                if i == 2:
                    words = line.split()
                    for word in words:
                        wordID = 0
                        for i,d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID,wordID] = words.count(word)

            filepathTokens = fil.split('/')
            lastToken = filepathTokens[len(filepathTokens)-1]
            if lastToken.startswith("spmsg"):
                train_labels[docID] = 1;

            docID += 1
    return features_matrix, train_labels

TRAIN_DIR = "../train-mails"
TEST_DIR = "../test-mails"

dictionary = make_Dictionary(TRAIN_DIR)

print("reading and processing emails from file")
features_matrix, labels = extract_features(TRAIN_DIR)
test_feature_matrix, test_labels = extract_features(TEST_DIR)
#default values of tuning parameters (kernel = linear, C = 1 and gamma =1)
model = svm.SVC()

print("TRAINING MODEL")
model.fit(features_matrix, labels)
predicted_labels = model.predict(test_feature_matrix)

print("Accuracy score :", end=" ")
print(accuracy_score(test_labels,predicted_labels))
