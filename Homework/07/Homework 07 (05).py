# hamming_7_4.py
# Hamming(7,4) implementation using generator and parity-check matrices

def bits_to_str(bits):
    return ''.join(str(int(b)) for b in bits)

def encode_7_4(data_bits):
    """Encode 4-bit list into 7-bit Hamming(7,4) codeword.
       data_bits: list of 4 bits [d1,d2,d3,d4] (0/1)"""
    d1, d2, d3, d4 = data_bits
    # Standard systematic Hamming(7,4) mapping (positions 1..7)
    # We'll use positions: 1-indexed: [p1,p2,d1,p3,d2,d3,d4]
    p1 = (d1 ^ d2 ^ d4) & 1
    p2 = (d1 ^ d3 ^ d4) & 1
    p3 = (d2 ^ d3 ^ d4) & 1
    code = [p1, p2, d1, p3, d2, d3, d4]
    return code

# parity-check H matrix mapping (syndrome bit order p1 p2 p3)
SYNDROME_TO_ERRPOS = {
    (0,0,0): None,
    (0,0,1): 4,  # bit position 4 (1-indexed): p3
    (0,1,0): 2,
    (0,1,1): 6,
    (1,0,0): 1,
    (1,0,1): 3,
    (1,1,0): 5,
    (1,1,1): 7
}

def syndrome(code):
    # code is 7-bit list in order [p1,p2,d1,p3,d2,d3,d4]
    p1,p2,d1,p3,d2,d3,d4 = code
    s1 = (p1 ^ d1 ^ d2 ^ d4) & 1  # parity check 1
    s2 = (p2 ^ d1 ^ d3 ^ d4) & 1  # parity check 2
    s3 = (p3 ^ d2 ^ d3 ^ d4) & 1  # parity check 3
    return (s1, s2, s3)

def decode_7_4(code):
    """Decode possibly corrupted 7-bit codeword. Return corrected data bits and info."""
    s = syndrome(code)
    errpos = SYNDROME_TO_ERRPOS.get(s)
    corrected = code.copy()
    if errpos is not None:
        # flip bit at position errpos (1-indexed)
        corrected[errpos-1] ^= 1
    # extract data bits [d1,d2,d3,d4] from corrected code:
    d1 = corrected[2]
    d2 = corrected[4]
    d3 = corrected[5]
    d4 = corrected[6]
    return [d1,d2,d3,d4], corrected, errpos

if __name__ == "__main__":
    # demo
    data = [1,0,1,1]
    code = encode_7_4(data)
    print("data:", data, "encoded:", bits_to_str(code))

    # introduce a single-bit error at position 5 (1-indexed)
    noisy = code.copy()
    noisy[4] ^= 1
    print("noisy:", bits_to_str(noisy))
    decoded, corrected, errpos = decode_7_4(noisy)
    print("decoded data:", decoded)
    print("corrected code:", bits_to_str(corrected))
    print("error position (1-indexed):", errpos)
