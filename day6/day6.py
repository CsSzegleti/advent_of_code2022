def is_char_sequence_unique(char_seq: str):
    for char in char_seq:
        if char_seq.count(char) > 1:
            return False
    else:
        return True


def find_first_marker_idx(signal: str, packet_size: int) -> int:
    i = packet_size - 1
    first_marker_found = False
    while i < len(signal) and not first_marker_found:
        first_marker_found = is_char_sequence_unique(signal[i - (packet_size - 1): i + 1])
        i += 1

    return -1 if i >= len(signal) else i


def main():
    with open("input.txt") as input_file:
        signal = input_file.readline().strip()

    print(f"First marker after character {find_first_marker_idx(signal, 4)} with packet size of 4.")
    print(f"First marker after character {find_first_marker_idx(signal, 14)} with packet size of 14.")


if __name__ == "__main__":
    main()
