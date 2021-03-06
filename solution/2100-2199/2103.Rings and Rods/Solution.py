class Solution:
    def countPoints(self, rings: str) -> int:
        mp = defaultdict(set)
        for i in range(1, len(rings), 2):
            c = int(rings[i])
            mp[c].add(rings[i - 1])
        return sum(1 for v in mp.values() if len(v) == 3)
