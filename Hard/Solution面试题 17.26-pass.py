# 面试题 17.26、稀疏相似度
from typing import List


def form(index1: int, index2: int, similarity: float) -> str:
    similarity = round(similarity + 1e-9, 4)
    if similarity == 0.0:
        return ''
    similarity = str(similarity)
    while len(similarity) < 6:
        similarity += '0'
    return f"{index1},{index2}: {similarity}"


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        docs = tuple(map(lambda x: set(x), docs))
        l = len(docs)
        res = []
        for index1 in range(l - 1):
            i = docs[index1]
            for index2 in range(index1 + 1, l):
                j = docs[index2]
                s = form(index1, index2, len(i.intersection(j)) / len(i.union(j)))
                if s:
                    res.append(s)
        return res
