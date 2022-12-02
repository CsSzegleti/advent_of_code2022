class Elf:
    def __init__(self):
        self.foods = []

    def get_total_calories(self) -> int:
        return sum(self.foods)
    

def read_input(input_file_name: str) -> [Elf]:
    elves = []
    with open(input_file_name) as input_file:
        current_elf: Elf = Elf()
        for line in input_file:
            line = line.strip()
            if line != '':
                current_elf.foods.append(int(line))
            else:
                elves.append(current_elf)
                current_elf = Elf()

    return elves


def find_top(num: int, elves: [Elf]):
    sorted_elves = elves.copy()
    sorted_elves.sort(reverse=True, key=Elf.get_total_calories)

    return sum(elf.get_total_calories() for elf in sorted_elves[:num])


def main():
    elves = read_input("day1/input.txt")
    print(f"Max calories of an elf: {find_top(1, elves)}")
    print(f"Max calories of the top three elves: {find_top(3, elves)}")


if __name__ == "__main__":
    main()
