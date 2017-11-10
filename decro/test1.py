def log(fn):
    def wrapper(*args, **kwargs):
        print fn.__name__
        return fn(*args, **kwargs)

    return wrapper

@log
def test(name):
    print 'hello %s' %name

test('papapa')


@log
def test2(name, str):
    print 'hello %s! welcom to %s' %(name, str)


test2('heihei', 'papapa')


@log
def test3(name, str, sexy='111'):
    print 'hello %s! welcom to %s,%s' % (name, str, sexy)

test3('haha', 'heihei', 'man')


class Foo(object):
    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
         print self._fn.__name__
         self._fn()
         print 222222


@Foo
def test4():
    print 000

test4()