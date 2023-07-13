import re
import cmds
import sys


def process_line(line: str):
    """
    commands:

    create <object>
    update <id> set <field> = <value>
    delete <id>
    select <id>
    select * from <object_type>
    quit
    """

    if line == "quit":
        sys.exit(0)

    select_all_pattern = "select * from (\w*)"
    select_all_match = re.match(select_all_pattern, line)
    if select_all_match:
        object_type = select_all_match.group(1)
        cmds.select_all(object_type)
        return

    create_pattern = "create (\w*)"
    create_match = re.match(create_pattern, line)
    if create_match:
        object_type = create_match.group(1)
        cmds.create(object_type)
        return



def run_console():
    while True:
        line = input("(hbnb) ")
        print(process_line(line))


if __name__ == "__main__":
    run_console()