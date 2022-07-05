from scipy import special
import itertools


def probabilaty_selector(selector: list, amount: int, maxface: int, target: int):
    if len(selector) == 1:
        return wahrscheinlichkeit(selector[0], amount, maxface, target)
    transitionlist = selector.copy()
    transitionlist.pop(0)
    summation = 0
    for k in range(1, min(maxface + 1,
                          target)):  # keine +1 nötig da wenn der erste würfel target zeigt der zweite würfel Null zeigen müsste
        print(f"{target - k}+{k}")
        print(
            f"{wahrscheinlichkeit(selector[0], amount, maxface, k)}*{conditional(selector, amount, maxface, k, target - k)}")
        summation = summation + (wahrscheinlichkeit(selector[0], amount, maxface, k)
                                 * conditional(selector, amount, maxface, k, target - k))

    return summation


def wahrscheinlichkeit(selector: int, amount: int, maxface: int, target: int) -> float:
    if target > maxface:
        return 0
    if target == 0:
        return 0
    return 1 - under(selector, amount, maxface, target) - over(selector, amount, maxface, target)


def conditional(selector: list, amount: int, maxface: int, target_past: int, target_present: int):
    return wahrscheinlichkeit(selector[1], selector[0] - 1, target_past, target_present)


def under(selector: int, amount: int, maxface: int, target: int):
    summation = 0
    for k in range(selector, amount + 1):  # range läuft solange es kleiner ist als der obere Wert => darum +1
        summation = summation + binomialformula(amount, (target - 1) / maxface, k)
    return summation


def over(selector: int, amount: int, maxface: int, target: int, ):
    summation = 0
    for k in range(amount - selector + 1,
                   amount + 1):  # range läuft solange es kleiner ist als der obere Wert => darum +1
        summation = summation + binomialformula(amount, (maxface - target) / maxface, k)
    return summation


def binomialformula(n, p, k):
    return special.binom(n, k) * (p ** k) * ((1 - p) ** (n - k))


def maßfunction():
    for i in range(5):

        p = [range(1, 6) for _ in range(i + 1)]

        for quant in itertools.product(*p):
            vec = [j + 1 for j in range(i + 1)]

            if sum(quant) == 5:

                while vec[0] < 10 - i:
                    quant_kopie = list(quant)
                    q = []
                    if vec[i] < 10:
                        vec[i] += 1

                    else:
                        if vec[i - 1] < 10-1:
                            vec[i - 1] += 1
                            vec[i] = vec[i - 1] + 1

                        else:
                            if vec[i - 2] < 10-2:
                                vec[i - 2] += 1
                                vec[i - 1] = vec[i - 2] + 1
                                vec[i] = vec[i - 1] + 1

                            else:
                                if vec[i - 3] < 10-3:
                                    vec[i - 3] += 1
                                    vec[i - 2] = vec[i - 3] + 1
                                    vec[i - 1] = vec[i - 2] + 1
                                    vec[i] = vec[i - 1] + 1

                                else:
                                    if vec[i - 4] < 10-4:
                                        vec[i - 4] += 1
                                        vec[i - 3] = vec[i - 4] + 1
                                        vec[i - 2] = vec[i - 3] + 1
                                        vec[i - 1] = vec[i - 2] + 1
                                        vec[i] = vec[i - 1] + 1

                    #print(vec)
                    for m in range(i+1):

                        while quant_kopie[m] > 0:
                            q.append(vec[m])

                            quant_kopie[m] -= 1
                    print(q)


if __name__ == "__main__":
    #maßfunction()
     a = 0
     for j in range(5,6):
       for amount, maxface, target, selector in itertools.product(range(10, 11), range(10, 11), range(1, 11), [j]):
         a = a + wahrscheinlichkeit(selector, amount, maxface, target)
         print(f"{selector}@{amount}d{maxface}={target}:{wahrscheinlichkeit(selector, amount, maxface, target) * 100 :.3f}")
     print(a * 100)
     a = 0
     print(probabilaty_selector([3, 2], 5, 10, 9))
