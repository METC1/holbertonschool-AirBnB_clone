#!/usr/bin/python3
"""
console.py contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines all common attributes/methods for command
    interpreter
    """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        Typing quit will exit the console
        """
        quit()

    def do_EOF(self, line):
        """
        Typing EOF will exit the console
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER won't execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
