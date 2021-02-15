def raise_exception(ExceptionType):
    raise ExceptionType('My Exception')


try:
    raise_exception(TypeError)
except TypeError as err:
    print('Handled with TypeError:', err)
except ValueError:
    print('Handled with ValueError')
except Exception:
    print('Handled with Exception')
except:
    print('Handled in except')
print('Working')

