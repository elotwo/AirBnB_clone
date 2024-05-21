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
        args = arg.split()
        if len(args) == 1:
            print ("***instance id missing***")
            return
        class_name, instance_id = arg[0], arg[1]
        if isinstance(class_name, BaseModel):
            print ("*** class doesn't exist ***")
            return
        key = f"{class_name}.{instance_id}"
        if key not in BaseModel.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])




if __name__ == "__main__":
    HBNBCommand().cmdloop()
