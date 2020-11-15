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


def setter_method_gen(property_name, props=None):
    def set_property(self, property_value):
        print('classproperties:set_property - %s - props: %s' % (property_name, props))

        if property_value is None:
            if props is not None and 'default_value' in props:
                property_value = props['default_value']
        elif props is not None and 'prop_type' in props:
            prop_type = props['prop_type']
            property_value = prop_type(property_value)
        set_class_attribute(self, "_" + property_name, property_value)
    return set_property


def declare_props(obj, *properties_list, props=None):

    if properties_list is None:
        properties_list = []

    properties_list = list(properties_list)

    if props is not None:
        properties_list.extend(list(props.keys()))
    else:
        props = {}

    for property_name in properties_list:

        getter_method = getter_method_gen(property_name)
        setter_method = setter_method_gen(property_name, props.get(property_name, None))

        set_class_attribute(obj, "_" + property_name, None)
        set_class_attribute(obj.__class__, "_get_" + property_name, getter_method_gen)
        set_class_attribute(obj.__class__, "_set_" + property_name, setter_method_gen)
        set_class_attribute(obj.__class__, property_name, property(getter_method, setter_method))

        # Set default values when defined in props
        if property_name in props and 'default_value' in props[property_name]:
            default_value = props[property_name]['default_value']
            set_class_attribute(obj, "_" + property_name, default_value)


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
