import os
from settings import BuildSettings

setpath = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# settings = BuildSettings('tests_output.ini', setpath + '/tests.ini', def_pth=setpath)  # works
settings = BuildSettings(setpath + '/tests_output.ini', setpath + '/tests.ini', def_pth='')

settings.add('test_setting_not_default', 'True')
settings.save()