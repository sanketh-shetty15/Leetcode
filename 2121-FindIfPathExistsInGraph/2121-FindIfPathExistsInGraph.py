# Last updated: 20/07/2026, 18:37:36
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        parents = list(range(n))

        for a, b in edges:
            while parents[a] != a:
                a = parents[a]

            while parents[b] != b:
                b = parents[b]
            if a > b:
                parents[a] = b
            else:
                parents[b] = a

        while parents[source] != source:
            source = parents[source]

        while parents[destination] != destination:
            destination = parents[destination]

        return source == destination