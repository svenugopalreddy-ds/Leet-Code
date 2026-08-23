class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, no later value can work
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                # i + 1 because each element can be used only once
                backtrack(i + 1, remaining - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result 