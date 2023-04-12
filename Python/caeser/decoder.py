def decoder(char_et: chr) -> []:
    results = []

    for i in range(0, 96):
        attempt = []
        for char in char_et:
            attempt.append(chr((ord(char) - 32 + i) % 95 + 32))
        results.append(attempt)

    return results
