from numpy import array, ndarray
from functools import wraps


def args_transform_from_list_to_ndarray(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):

        tempArgs = list(args)
        tempArgs = [array(arg, dtype=float) if isinstance(
            arg, list) else arg for arg in tempArgs]

        # Verificando shape de algunos args y haciendo reshape

        # for i in range(len(tempArgs)):
        #     if (isinstance(tempArgs[i], ndarray)):
        #         if tempArgs[i].ndim == 1:
        #             tempArgs[i] = tempArgs[i].reshape(tempArgs[i].shape[0], 1)

        argsModified = tuple(tempArgs)
        return fn(*argsModified, **kwargs)

    return wrapper
