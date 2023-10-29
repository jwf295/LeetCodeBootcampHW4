class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        candidate_1 = edges[0][0]
        candidate_2 = edges[0][1]
        if edges[1][0] == candidate_1 or edges[1][1] == candidate_1:
            return candidate_1
        return candidate_2
