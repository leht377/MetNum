from numpy import array


def gaussJordan_args_transform_np_array(fn):
    def wrapper(*args):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        # Verificando shape de algunos args (b,x0) y haciendo reshape
        if tempList[1].ndim == 1:
            tempList[1] = tempList[1].reshape(tempList[1].shape[0], 1)

        argsModified = tuple(tempList)
        return fn(*argsModified)

    return wrapper
