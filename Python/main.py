import output as out
import read_file as rf
import ranker as r

from caeser import decoder as d
from caeser import encoder as e


def encode(plain_text: [], shift: int):
    encoded = e.encoder(plain_text, shift % 95)
    return ''.join(encoded)


def decode(encoded_text: str) -> []:
    decoded = d.decoder(encoded_text)
    return decoded


def create_dict():
    words = rf.read_file()
    return rf.load_dictionary(words)


def main():
    # Creates the dictionary in the Trie data structure
    tt = create_dict()

    # Plain text/user input & shift value (to the right)
    plain_text = "The quick brown fox jumps over the lazy dog!?"
    shift = 40

    # Encode the text, and decode it
    encoded = encode(list(plain_text.lower()), shift)
    decoded = decode(encoded)

    # Clean up decoded list for printing
    for i, dec in enumerate(decoded):
        decoded[i] = ''.join(dec)

    # Determine ranking of the decoded values for printing
    # ranking = dict(sorted(r.rank(decoded, tt).items(), key=lambda x: x[1], reverse=True))
    ranking = sorted(r.rank(decoded, tt).items(), key=lambda x: x[1], reverse=True)

    # Print results
    # out.encode_output(plain_text, shift, encoded)
    # out.decode_output(decoded)
    out.ranking_output(ranking, decoded)


if __name__ == '__main__':
    main()
