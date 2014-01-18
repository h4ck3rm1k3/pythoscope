import sys

try:
    from setuptools import setup
    # ctypes library is part of standard library since Python 2.5.
    if sys.version_info < (2, 5):
        install_requires = ['ctypes']
    else:
        install_requires = []


    args = dict(
        entry_points = {'console_scripts': ['pythoscope = pythoscope:main']},
        install_requires = install_requires,
        test_suite = 'nose.collector',
        tests_require = ['nose', 'mock', 'docutils', 'setuptools-lint'])
except ImportError:
    from distutils.core import setup
    args = dict(scripts = ['scripts/pythoscope'])

# The C module doesn't need to be built for Python 2.5 and higher.
if sys.version_info < (2, 5):
    from distutils.core import Extension
    ext_modules = [Extension('pythoscope._util', sources=['pythoscope/_util.c'])]
else:
    ext_modules = []


from pythoscope import __version__ as VERSION

args['install_requires'].append( 'setuptools-lint')


setup(
    name='pythoscope',
    version=VERSION,

    author = 'Michal Kwiatkowski',
    author_email = 'constant.beta@gmail.com',
    description = 'unit test generator for Python',
    long_description = open("README").read() + "\n" + open("Changelog").read(),
    license = 'MIT',
#    url = 'http://pythoscope.org',
    url='https://github.com/h4ck3rm1k3/pythoscope',

    ext_modules = ext_modules,

    packages = ['pythoscope', 'pythoscope.inspector', 'pythoscope.generator',
                'bytecode_tracer',
                #'lib2to3', 'lib2to3.pgen2'
            ],
    package_data = {'pythoscope': [],
                    'bytecode_tracer': [],
                    #'lib2to3': ['*.txt']
                },

    keywords='testing test case generator',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Testing',
    ],

    **args
)
