from scipy import special
from itertools import product


def probabilaty_selector(selector: list, amount: int, maxface: int, target: int ):
    if len(selector) == 1:
        return wahrscheinlichkeit(selector[0], amount, maxface, target )
    transitionlist = selector.copy()
    transitionlist.pop(0)
    summation = 0
    for k in range(1, min(maxface, target) + 1):
        print(k)
        print(wahrscheinlichkeit( selector[0],amount, maxface, k)* wahrscheinlichkeit(selector[1], selector[0]-1, k, target-k))
        summation = summation + wahrscheinlichkeit( selector[0],amount, maxface, k) * probabilaty_selector(transitionlist, selector[0]-1, k, target-k)
    return summation


def wahrscheinlichkeit(selector: int, amount: int, maxface: int, target: int ) -> float:
    if target > maxface:
        return 0
    if target ==0:
        return 0
    return 1 - under(selector, amount, maxface, target ) - over(selector, amount, maxface, target)


def under( selector: int, amount: int, maxface: int, target: int):
    summation = 0
    for k in range(selector, amount + 1):
        summation = summation + binomialformula(amount, (target - 1) / maxface, k)
    return summation


def over(selector: int, amount: int, maxface: int, target: int, ):
    summation = 0
    for k in range(amount - selector + 1, amount + 1):
        summation = summation + binomialformula(amount, (maxface - target) / maxface, k)
    return summation


def binomialformula(n, p, k):
    return special.binom(n, k) * (p ** k) * ((1 - p) ** (n - k))


if __name__ == "__main__":
    a = 0
    for amount, maxface, target, selector in product(range(5, 6), range(10, 11), range(1, 11), range(1, 2)):
        a = a + wahrscheinlichkeit(selector, amount, maxface, target)
        print(f"{selector}@{amount}d{maxface}={target}:{wahrscheinlichkeit(selector, amount, maxface, target) * 100}")
    print(a*100)
    print(probabilaty_selector([3, 2], 5, 10, 5 ))
