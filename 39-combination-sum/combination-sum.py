class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue

                path.append(candidates[i])

                # i, not i + 1, because we can reuse the same number
                backtrack(i, remaining - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result