"""
    Module for handling generation of class properties

"""
from pyutils.cli.flags import verify_flag, get_flag


get_class_attribute = getattr
set_class_attribute = setattr


def getter_method_gen(property_name):
    def get_property(self):
        return get_class_attribute(self, "_" + property_name)
    return get_property


def setter_method_gen(property_name):
    def set_property(self, property_value):
        set_class_attribute(self, "_" + property_name, property_value)
    return set_property


def declare_props(obj, *properties_list, **properties_data):
    for property_name in properties_list:
        set_class_attribute(obj, "_" + property_name, None)
        set_class_attribute(obj, "_get_" + property_name, getter_method_gen(property_name))
        set_class_attribute(obj, "_set_" + property_name, setter_method_gen(property_name))
        set_class_attribute(obj.__class__, property_name,
                            property(getter_method_gen(property_name),
                                     setter_method_gen(property_name)))

    def properties_setter_gen(props):
        def set_properties(self, properties_dict):
            for property_name in properties_dict:
                setter = get_class_attribute(self, "_set_" + property_name)
                setter(properties_dict[property_name])
                # set_class_attribute(self, "_" + property_name, properties_dict[property_name])
        return set_properties

    set_class_attribute(obj, 'class_properties', properties_list)
    set_class_attribute(obj.__class__, 'set_properties', properties_setter_gen(properties_list))


def set_properties_from_flags(class_object):
    if get_flag("--help"):
        print("Current available flags:")
        for property_name in class_object.class_properties:
            print("--" + property_name)
        exit(0)
    for property_name in class_object.class_properties:
        if verify_flag("--" + property_name):
            set_class_attribute(class_object, "_" + property_name, get_flag("--" + property_name))
