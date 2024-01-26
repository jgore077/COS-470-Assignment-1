from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = BertModel.from_pretrained("bert-base-cased")
sentence="Because they know that no Sicilian will refuse a request on his daughter's wedding day."
tokens = tokenizer.wordpiece_tokenizer.tokenize(sentence)
print(f'WordPiece Tokenization of "{sentence}"')
print(tokens)

