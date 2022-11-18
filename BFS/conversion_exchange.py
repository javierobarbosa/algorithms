"""
BFS
Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' currency. In this case, the correct result is 1.89
"""
from typing import List


def get_conversion(rates:List[List], queries: List[List]) -> List[int]:
    adjacency_list = {}
    for rate in rates:
        to_currency = rate[0]
        from_currency = rate[1]
        currency_rate = rate[2]
        adjacency_list[to_currency] = adjacency_list.get(to_currency, []) + [(from_currency, currency_rate)]
        adjacency_list[from_currency] = adjacency_list.get(from_currency, []) + [(to_currency, 1/currency_rate)]
    result = []

    for query in queries:
        to_currency = query[0]
        from_currency = query[1]
        queue = [(to_currency, 1)]
        visited = set(to_currency)
        found = False
        if to_currency not in query or from_currency not in query:
            result.append(-1)
        else:
            while len(queue):
                node, currency_rate = queue.pop(0)
                if node == from_currency:
                    result.append(currency_rate)
                    found = True
                    break
                for neighbor, rate in adjacency_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, currency_rate * rate))
            if not found:
                result.append(-1)
    return result


if __name__ == "__main__":
    rate = get_conversion([['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]], [['GBP', 'AUD']])
    print(round(rate[0], 2))
