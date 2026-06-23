class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for num in range(left, right + 1):
            n = num
            self_divide = True

            while n > 0:
                digit = n % 10

                if digit == 0 or num % digit != 0:
                    self_divide = False
                    break

                n //= 10

            if self_divide:
                res.append(num)

        return res