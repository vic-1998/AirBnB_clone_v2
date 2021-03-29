#!/usr/bin/python3
"""
Contains the entry point of the command
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel": BaseModel, "City": City, "State": State,
           "Amenity": Amenity, "User": User, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand(cmd.Cmd):"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exit console"""
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def method_key_value(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                values = arg.split('=', 1)
                key = values[0]
                value = values[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, args):
        """ Create an object of any class"""
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in classes:
            new_dict = self.method_key_value(arg[1:])
            instance = classes[arg[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints string rep. of an instance based"""
        burger = shlex.split(arg)
        if len(burger) == 0:
            print("** class name missing **")
            return False
        if burger[0] in classes:
            if len(burger) > 1:
                beer = burger[0] + "." + burger[1]
                if beer in models.storage.all():
                    print(models.storage.all()[beer])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        burger = shlex.split(arg)
        beer = []
        if len(burger) == 0:
            for value in models.storage.all().values():
                beer.append(str(value))
            print("[", end="")
            print(", ".join(beer), end="")
            print("]")
        elif burger[0] in classes:
            for pizza in models.storage.all():
                if burger[0] in pizza:
                    beer.append(str(models.storage.all()[pizza]))
            print("[", end="")
            print(", ".join(beer), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
