from caeser import decoder as d
from caeser import encoder as e
import output as out


def encode_cc(plain_text: str, shift: int):
    plain_text = plain_text.lower()
    char_pt = list(plain_text)
    encoded = e.encoder(char_pt, shift % 95)
    return ''.join(encoded)


def decode_cc(encoded_text: str) -> []:
    decoded = d.decoder(encoded_text)
    return decoded


def encode():
    shift = 1

    plain_text = "Hello World"

    encoded = encode_cc(plain_text, shift)

    out.encode_output(plain_text, shift, encoded)


def decode():
    shift = 1

    plain_text = "Hello World"

    encoded = encode_cc(plain_text, shift)

    out.decode_output(decode_cc(encoded))


def main():
    encode()
    decode()


if __name__ == '__main__':
    main()
