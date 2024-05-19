#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):

        """greet [person]
        Greet the named person """
        if person:

            print("hi,", person)
        else:
            print("hi")
    def do_EOF(self, line):
        return quit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
