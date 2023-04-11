import pandas as pd

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
    headers_one = ["Encoded Text"]
    rows_one = [([decoded[-1]])]

    table_one = tabulate(rows_one, headers_one, tablefmt="heavy_outline", stralign="center")
    print(table_one)

    original = {}
    for i, d in enumerate(decoded):
        original[d] = i

    df = pd.DataFrame(ranking, columns=["Decoded", "Weight"])
    df['r'] = df['Weight'].rank(method='min', ascending=False).astype(int)
    values = list(df.itertuples(index=False, name=None))

    headers_two = ["#", "Decoded", "Weight", "Rank"]
    rows_two = []

    for i, (decoded, weight, rank) in enumerate(values):
        rows_two.append([original[decoded] + 1, decoded, weight, rank])

    table = tabulate(rows_two, headers_two, tablefmt="heavy_outline", stralign="center")
    print(table)
