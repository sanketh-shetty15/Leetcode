# Last updated: 20/07/2026, 18:38:10
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        stack=[0]
        while stack:
            i=stack.pop()

            if i not in visited:
                visited.add(i)

                for c in rooms[i]:
                    if c not in stack:
                        stack.append(c)

        return len(visited)==len(rooms)
       
        
        
        
       


        