class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def swap(str, i, j):

            ls = list(str)
            ls[i], ls[j] = ls[j], ls[i]
            return "".join(ls)
        
        target = "123450"
        start = "".join(str(cell) for row in board for cell in row)

        queue = deque()
        queue.append([start, start.index('0'), 0])

        visited = set(start)

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        while queue:
            current_state, pos, steps = queue.popleft()

            if current_state == target:
                return steps

            for neighor in neighbors[pos]:
                new_state = swap(current_state, pos, neighor)

                if new_state not in visited:
                    queue.append([new_state, neighor, steps+1])
                    visited.add(new_state)
                    
        return -1