#!/usr/bin/python3
"""
Contains the entry point of the command
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand(cmd.Cmd):"""
    prompt = '(hbnb)'

    valid_classes = ["BaseModel", "User", "State",
                     "City", "Amenity", "Place", "Review"]

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
                valu = arg.split('=', 1)
                key = valu[0]
                value = valu[1]
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
        if len(args) == 0:
            print("** class name missing **")
            return False
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            if len(args) > 1:
                new_dict = dict(arg.split('=') for arg in args[1:])
                for key, value in new_dict.items():
                    if hasattr(new_instance, key):
                        if '_' in value:
                            value = value.replace('_', ' ')
                            try:
                                value = eval(value)
                            except Exception:
                                pass
                        setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)

        except Exception:
            print("** class doesn't exist **")

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
