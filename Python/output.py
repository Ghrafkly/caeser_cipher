def encode_output(pt: str, shift: int, et: str):
    # pt_width = et_width
    width = len(pt)

    if len("encoded_text") > width:
        width = len("encoded_text")

    col_headers = ["plain_text", "shift value", "encoded_text"]
    col_data = [pt, shift, et]

    print(f"{col_headers[0]}".center(width) + " | " + f"{col_headers[1]}".center(11) + " | " + f"{col_headers[2]}".center(width))
    print("-" * ((width * 2) + 17))
    print(f"{col_data[0]}".center(width) + " | " + f"{col_data[1]}".center(11) + " | " + f"{col_data[2]}".center(width))
    print("-" * ((width * 2) + 17))


def decode_output(decoded_arr: []):
    encoded_text = ''.join(decoded_arr[len(decoded_arr) - 1])

    width = len(encoded_text)

    if len("encoded_text") > width:
        width = len("encoded_text")

    print(f"encoded_text".center(width) + " : " + f"{encoded_text}".center(width))
    print("-" * ((width * 2) + 2))
    for i, decoded in enumerate(decoded_arr):
        print(f"{i + 1}".rjust(width) + " : " + f"{''.join(decoded)}".center(width))
