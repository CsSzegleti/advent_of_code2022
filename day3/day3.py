class Rucksack:
    def __init__(self, items: str):
        self.first_compartment: str = items[:int(len(items)/2)]
        self.second_compartment: str = items[int(len(items)/2):]

    def get_items(self):
        return self.first_compartment + self.second_compartment

    def find_common_items(self) -> [str]:
        common_items = ''

        for item in self.first_compartment:
            if item in self.second_compartment and item not in common_items:
                common_items += item

        return common_items


def read_input(input_file_name: str) -> []:
    rucksacks = []
    with open(input_file_name) as input_file:
        for line in input_file:
            rucksacks.append(Rucksack(line.strip()))

    return rucksacks


def find_badge_of_group(rucksacks: [Rucksack]) -> str:
    for item in rucksacks[0].get_items():
        if item in rucksacks[1].get_items() and item in rucksacks[2].get_items():
            return item


def sum_items_priorities(common_items: str):
    item_priorities = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    item_priorities.extend([chr(x) for x in range(ord('A'), ord('Z') + 1)])

    return sum(item_priorities.index(item) + 1 for item in common_items)


def main():
    rucksacks = read_input("input.txt")
    # pt 1
    sum_priorities = sum(sum_items_priorities(rucksack.find_common_items()) for rucksack in rucksacks)
    print(f"Sum of all item common to both compartments: {sum_priorities}")

    # pt 2
    sum_badges = 0
    for group_rucksacks in [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]:
        sum_badges += sum_items_priorities(find_badge_of_group(group_rucksacks))

    print(f"Sum of all badges: {sum_badges}")


if __name__ == '__main__':
    main()
