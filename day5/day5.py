import copy


class Command:
    def __init__(self, command_string: str):
        tokenized_command = command_string.strip().split(' ')

        self.num_pieces = int(tokenized_command[1])
        self.from_stack = int(tokenized_command[3])
        self.to_stack = int(tokenized_command[5])


class StackManager:
    def __init__(self):
        self.stacks: dict[int, []] = dict()
        self.saved_state: dict[int, []] = dict()

    def save_state(self):
        self.saved_state = copy.deepcopy(self.stacks)

    def load_state(self):
        self.stacks = copy.deepcopy(self.saved_state)

    def push_to_stack(self, stack_num: int, cargos: [str], bottom: bool = False):
        if stack_num not in self.stacks:
            self.stacks[stack_num] = []

        if bottom:  # only for initialization
            self.stacks[stack_num].insert(0, cargos[0])
        else:
            self.stacks[stack_num].extend(cargos)

    def pop_from_stack(self, stack_num: int, num_cargos: int):
        cargos_to_remove = self.stacks[stack_num][- num_cargos:]
        del self.stacks[stack_num][- num_cargos:]
        return cargos_to_remove

    def move_cargo(self, from_stack: int, to_stack: int, num_cargos: int):
        self.push_to_stack(to_stack, self.pop_from_stack(from_stack, num_cargos))

    def interpret_command(self, command: Command):
        for i in range(command.num_pieces):
            self.move_cargo(command.from_stack - 1, command.to_stack - 1, 1)

    def interpret_command_bulk(self, command: Command):
        self.move_cargo(command.from_stack - 1, command.to_stack - 1, command.num_pieces)

    def get_top_stacks(self) -> str:
        tops = ''
        for i in range(len(self.stacks)):
            tops += self.stacks[i][-1]

        return tops


def read_input(input_file_name: str, num_stacks: int):
    stack_manager = StackManager()
    commands: [Command] = []
    with open(input_file_name, 'r') as input_file:

        line = input_file.readline().strip()
        while line and not line.startswith("1"):
            for i in range(num_stacks):
                cargo = line[i * 4 + 1]
                if cargo != ' ':
                    stack_manager.push_to_stack(i, [cargo], True)
            line = input_file.readline().strip()

        input_file.readline()
        line = input_file.readline().strip()

        while line:
            commands.append(Command(line))
            line = input_file.readline().strip()

    return stack_manager, commands


def main():
    num_stacks = 9
    stackmanager, commands = read_input("input.txt", num_stacks)

    stackmanager.save_state()

    for command in commands:
        stackmanager.interpret_command(command)

    print(f"Top of stacks with CrateMover 9000: {stackmanager.get_top_stacks()}")

    stackmanager.load_state()

    for command in commands:
        stackmanager.interpret_command_bulk(command)

    print(f"Top of stacks with CrateMover 9001: {stackmanager.get_top_stacks()}")


if __name__ == "__main__":
    main()
