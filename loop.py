from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Jika jumlah kurung buka dan tutup sudah sama dengan n
            if len(current) == 2 * n:
                result.append(current)
                return

            # Tambahkan kurung buka jika jumlahnya masih kurang dari n
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            # Tambahkan kurung tutup jika jumlahnya kurang dari kurung buka
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
