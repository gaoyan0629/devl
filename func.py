from __future__ import print_function
import pandas as pd
import pathlib2 as Path
# this is example of how to use super in version 2.7
class CustomDictOne(pd.DataFrame):
    def __init__(self,name,*arg,**kw):
      super(CustomDictOne, self).__init__(*arg, **kw)
      self.name = name
    def myFun():
        pass


class Person():
    name = 'Victor' # global class variable
    def __init__(self,age = 90):
        self._age = age
    def say(self, what):
        print(self.name, what)


    @property # you can person.age = 10
    def age():
        def fget(self):
            return self._age
        def fset(self, person):
            if isinstance(person, Person):
                age = person._age # can be used within class
            self._age = float(age)

def get(fn):
    HOME_DIR=Path.Path.home()
    f = HOME_DIR / 'classroom' / 'data'
    pattern = '{}.*'.format(fn)
    ret = list(f.rglob(pattern))
    cnt = len(ret)
    if cnt == 0:
        print('the file name [{}] not found'.format(fn))
        return
    elif cnt > 1:
        print('mutiple entry found [{}]'.format(ret))
        return
    return ret[0]


def load_dataset(fn): 
    return pd.read_csv(get(fn))
