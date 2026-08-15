class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            curr_word,length=queue.popleft()
            if curr_word == endWord:
                return length
            for i in range(len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == curr_word[i]:
                        continue
                    new_word=curr_word[:i] + c + curr_word[i+1:]
                    if new_word in wordset:
                        queue.append((new_word,length+1))
                        wordset.remove(new_word)
        return 0