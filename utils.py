# Environment utilies

import os

from django.core.exceptions import ImproperlyConfigured

# gets an environmet variable or catches a key error
# Contracts:
    # variable_name is a STRING
def get_env_variable(variable_name):
    try:
        return os.environ[variable_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % variable_name
        raise ImproperlyConfigured(error_msg)


# not super important but cleans up code that otherwise looks like this:
#   DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# now that looks like this:
#   DIR = nth_parent_directory(3, __file__)
#
# Much cleaner :)
def nth_parent_directory(n, child):
    dirname = os.path.abspath(child)
    for i in range(n):
        dirname = os.path.dirname(dirname)

    return dirname
