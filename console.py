#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_help(self, arg):
        """Help cammand list about a command"""
        super().do_help(arg)
    def emptyline(self):
        pass 
    def do_EOF(self, arg):
        """this signal the end of File"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
