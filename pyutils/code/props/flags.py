from .base import set_class_attribute

from pyutils.cli.flags import verify_flag, get_flag


def set_properties_from_flags(class_object):
    if get_flag("--help"):
        print("Current available flags:")
        for property_name in class_object.class_properties:
            print("--" + property_name)
        exit(0)
    for property_name in class_object.class_properties:
        if verify_flag("--" + property_name):
            set_class_attribute(class_object, "_" + property_name, get_flag("--" + property_name))
