class Section:
    def __init__(self, section_range: str):
        section_range = section_range.split('-')
        self.start = int(section_range[0])
        self.end = int(section_range[1])

    def is_completely_overlapping(self, other) -> bool:
        return (self.start >= other.start and self.end <= other.end) or \
            (self.start <= other.start and self.end >= other.end)

    def is_overlapping(self, other) -> bool:
        return other.start <= self.start <= other.end or \
            self.start <= other.start <= self.end


def read_input(input_file_name: str) -> []:
    inputs = []
    with open(input_file_name) as input_file:
        for line in input_file:
            line = line.strip().split(',')
            inputs.append([Section(section) for section in line])

    return inputs


def main():
    pair_sections: [[Section]] = read_input("input.txt")
    sec1 = Section('2-3')
    sec2 = Section('4-6')
    print(sec1.is_overlapping(sec2))

    print(f"{[pair_section[0].is_completely_overlapping(pair_section[1]) for pair_section in pair_sections].count(True)}")
    print(f"{[pair_section[0].is_overlapping(pair_section[1]) for pair_section in pair_sections].count(True)}")


if __name__ == "__main__":
    main()
