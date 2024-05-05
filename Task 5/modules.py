from statistics import mean
import math

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def average_grade(scores: list[int]) -> float:
    return mean(scores)

def sberbank_shares(amount: float) -> int:
    share_price = 317.20
    return int(amount / share_price)

