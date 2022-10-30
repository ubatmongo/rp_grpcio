from typing import List


class Calculator:
    def __init__(self):
        self.results: List[float] = [0.0]

    def add(self, number: float) -> float:
        last_result: float = self.results[-1]
        add_result: float = last_result + number
        self.results.append(add_result)
        return add_result
