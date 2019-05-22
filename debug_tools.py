from functools import wraps

# This methods sole purpose is to get the class name of the calling method
# debugging purposes only 
# - get_class_that_defined_method():
#   ---- Inputs ----
#   method or functino is inputted into the arguments
#   ---- Outputs ----
#   The name of the class object that the function is a member of is outputted
##############################################################################################################
def get_class_that_defined_method(meth):
    import inspect
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
           if cls.__dict__.get(meth.__name__) is meth:
                return cls
        meth = meth.__func__  # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        cls = getattr(inspect.getmodule(meth),
                      meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)



# The logger is going to wrap all main functions in the class heirarchy and can be used for debugging 
# purposes in legacy projects
# - functionLogger():
#   ---- Inputs ----
#   Function to be decorated
#   ---- Outputs ----
#   Decorated function.  In this case, the function is decorated to log output of the function called, th class it
#   called from and the time it was called. 
##############################################################################################################
def functionLogger(outputFunction, argument=None):
    import logging
    logging.basicConfig(
        filename="debug.log",
        level=logging.INFO,
        format='%(asctime)s %(message)s'
    )

    # This will log the name of the function and the class to which it belongs
    # in the case of 
    @wraps(outputFunction)
    def logWrapper(*args, **kwargs):
        # args_repr = [repr(a) for a in args]                      
        # kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] 
        # signature = ", ".join(args_repr + kwargs_repr)
        logging.info(
            "Ran {} from class: {} using the arguments:{}".format(
                outputFunction.__name__,
                get_class_that_defined_method(outputFunction),
                repr(argument)
        ))
        return outputFunction(*args, **kwargs)
    return logWrapper