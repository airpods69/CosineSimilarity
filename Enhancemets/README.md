# Semantic Cosine Similarity

This directory consists of the enhancements done to cosine similarity measurement to remove the disadvantages present in it.
These Enhancements are from the paper: [semantic cosine similarity](https://google.com/)]

### Identified problem
The disadvantage of using cosine similarity measurement is that when two term vectors with some semantic relation on their dimensions exist, that is not considered. This results in low similarity results.

### Proposed fix
1. Dimension equalization of both term vectors
    -   This is done because cosine similarity can only be applied on vectors of the same dimensions.
2. If there are any synonym pairs with different syntax between two term vectors. Then choose the first one as dimension name for both vectors.
3. If there is a dimension in first term vector with hypernym-hyponym relation toward second term vector, choose one as dimension name.
4. Recalibrate dimension value of dimensions with hypernym-hyponym relation by the formula n = p * s .

