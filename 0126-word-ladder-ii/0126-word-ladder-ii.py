class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)

        if endWord not in wordset:
            return []

        queue = deque([beginWord])

        parent = defaultdict(list)
        distance = {beginWord: 0}

        found = False

        while queue and not found:

            used = set()

            for _ in range(len(queue)):

                curr_word = queue.popleft()

                for i in range(len(curr_word)):

                    for c in "abcdefghijklmnopqrstuvwxyz":

                        if c == curr_word[i]:
                            continue

                        new_word = curr_word[:i] + c + curr_word[i + 1:]

                        if new_word not in wordset:
                            continue

                        # First time reaching this word
                        if new_word not in distance:

                            distance[new_word] = distance[curr_word] + 1
                            parent[new_word].append(curr_word)

                            queue.append(new_word)
                            used.add(new_word)

                            if new_word == endWord:
                                found = True

                        # Another shortest path
                        elif distance[new_word] == distance[curr_word] + 1:

                            parent[new_word].append(curr_word)

            # Remove after processing the whole level
            for word in used:
                wordset.remove(word)

        if endWord not in distance:
            return []

        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for p in parent[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)

        return result