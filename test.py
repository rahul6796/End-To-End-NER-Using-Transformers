from pathlib import Path
import re

def read_wnut(file_path):
    file_path = Path(file_path)

    raw_text = file_path.read_text().strip()
    raw_docs = re.split(r'\n\t?\n', raw_text)
    token_docs = []
    tag_docs = []
    for doc in raw_docs:
        tokens = []
        tags = []
        for line in doc.split('\n'):
            word_token = line.split()
            tokens.append(word_token[0])
            tags.append(word_token[-1])
        token_docs.append(tokens)
        tag_docs.append(tags)

    return token_docs, tag_docs

texts, tags = read_wnut('/home/rahul/Desktop/NLP_Project/NER/End-To-End-NER-Using-Transformers/artifacts/data_ingestion/conll2003/train.txt')