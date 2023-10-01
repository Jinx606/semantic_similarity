import spacy

# Load the smaller language model 'en_core_web_sm'
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("_" * 100, "\n")  # This is for readability

tokens = nlp('cat monkey apple banana horse carrot rabbit')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("_" * 100, "\n")  # This is for readability

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

'''
These are my findings and as such i prefer md as it is more accurate:
- Smaller Model Size: 'en_core_web_sm' is a smaller and less complex model compared to 'en_core_web_md', which means it loads faster and consumes less memory.
- Lower Accuracy: The 'en_core_web_sm' model may have lower accuracy in tasks that require fine-grained semantic understanding and entity recognition compared to 'en_core_web_md', as it has a smaller vocabulary and fewer word vectors.
- Similarity Differences: You may observe differences in similarity scores between words and sentences. Smaller models like 'en_core_web_sm' might provide lower similarity scores for certain word pairs and sentences compared to 'en_core_web_md', reflecting the reduced representation capacity.
- Faster Execution: Due to its smaller size, 'en_core_web_sm' is expected to execute your code faster than 'en_core_web_md'. This is a given when working with a smaller program in general.
- I have also noticed a slower understand from sm when it comes to capitalisation
'''
