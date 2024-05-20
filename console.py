#!/usr/bin/python3
"""
 This is console.py
 A python script for a command processor
"""
import cmd
from tests.models.base_model import BaseModel
import uuid


class HBNBCommand(cmd.Cmd):
    """
    this is a command console for a simple command
    processor
    """
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

    def do_create(self, arg):
        if not arg:
            print ("**class name missing**")
            return
        try:
            model = BaseModel()
            model.save()
            print(model.id)
        except NameError:
          print ("** class doesn't exist **")

    def do_show(self, arg):
        if not arg:
            print ("**class name missing**")
            return
        elif model != "BaseModel":
           print ("** class doesn't exist **")
           return
        elif not model.id:
            print ("** instance id missing **")
            return
        else:
            print ("model.name")
            print ("model.id")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
