#!/usr/bin/python3
import cmd
class mycommd(cmd.Cmd):
    def do_greet (self, person):
        """greet [person]
        Greet the named person """
        print ("Hello")
    def do_EOF(self, line):
        return True
    def postloop(self):
        print
if __name__ == "__main__":
    mycommd().cmdloop()

