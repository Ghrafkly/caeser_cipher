from tabulate import tabulate


def encode_output(pt: str, shift: int, et: str):
    headers = ["Plain Text", "Shift Value", "Encoded"]
    rows = [([pt, shift, et])]

    table = tabulate(rows, headers=headers, tablefmt="heavy_outline", colalign=("center", "center", "center"))
    print(table)


def decode_output(decoded_arr: []):
    headers = ["#", "Decoded"]
    rows = []

    for i, e in enumerate(decoded_arr):
        rows.append([i + 1, ''.join(decoded_arr[i])])

    table = tabulate(rows, headers=headers, tablefmt="heavy_outline", colalign=("right", "center"))
    print(table)


def ranking_output(ranking, decoded):
    original = {}
    for i, d in enumerate(decoded):
        original[d] = i

    headers = ["#", "Decoded", "Weight", "Rank"]
    rows = []

    for i, (encoded, weight) in enumerate(ranking.items()):
        rows.append([original[encoded] + 1, encoded, weight, i + 1])

    table = tabulate(rows, headers=headers, tablefmt="heavy_outline", colalign=("right", "center", "right", "right"))
    print(table)
