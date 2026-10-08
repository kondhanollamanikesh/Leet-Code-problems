class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = set([startGene])

        genes = ['A', 'C', 'G', 'T']

        while queue:

            current, mutations = queue.popleft()

            if current == endGene:
                return mutations

            for i in range(8):

                for gene in genes:

                    if gene == current[i]:
                        continue

                    new_gene = current[:i] + gene + current[i + 1:]

                    if new_gene in bank and new_gene not in visited:

                        visited.add(new_gene)

                        queue.append((new_gene, mutations + 1))

        return -1