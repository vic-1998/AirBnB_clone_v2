#!/usr/bin/python3
""" module console.py"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

atri = {"BaseModel": BaseModel, "User": User, "City": City, "State": State,
        "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """class console command"""
    prompt = "(hbnb) "
    class_list = {"BaseModel"}

    def do_quit(self, args):
        """Command to quit the program"""
        quit()

    def do_EOF(self, args):
        """EOF command to exit the program"""
        quit()

    def emptyline(self):
        return

    def do_create(self, line):
        """Create new instance"""
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in atri:
            instance = atri[arg[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, line):
        '''print the string representation of an
        instance based on the class name'''
        arg = shlex.split(line)
        odic = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
        if len(arg) < 2:
            print("** instance id missing **")
        else:
            key = arg[0] + "." + arg[1]
            if key in odic:
                obj = odic[key]
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] not in self.class_list:
            print("** class doesn't exist **")
        if len(arg) < 2:
            print("** instance id missing **")
        else:
            odic = storage.all()
            for key, value in odic.items():
                if value.id == arg[1] and value.__class__.__name__ == arg[0]:
                    del(odic[key])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        ''' Prints all string representation of all
        instances based or not on the class name'''
        arg = shlex.split(line)
        odic = []
        if len(arg) == 0:
            for value in models.storage.all().values():
                odic.append(str(value))
            print("[", end="")
            print(", ".join(odic), end="")
            print("]")
        elif odic[0] in atri:
            for k in models.storage.all():
                if arg[0] in k:
                    odic.append(str(models.storage.all()[k]))
            print("[", end="")
            print(", ".join(odic), end="")
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
        elif args[0] in atri:
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
