# Semantic Cosine Similarity

Implementation of semantic cosine similarity from the paper: https://www.researchgate.net/publication/262525676_Semantic_Cosine_Similarity

### To-Do List
- [x] - Dimension Equalization
- [x] - Check for Hypernym Hyponym Pair
- [x] - Check for Synonym Pairs and replace it
- [ ] - Recalibrate Dimension Values
- [ ] - Fix IndexError when strings are of different length

#### How does Synonym Pair work?
For finding the Synonyms, I approached the solution by going through https://thesaurus.com for finding synoyms then, picking up only the relevant ones which are needed and present in s1
Then I replaced the words

#### Hypernym Pairing
Hypernym pairing works using nltk-wordnet
