from setuptools import setup, find_packages

desc = """Mustache library for Python"""
summ = """Mustache library for Python"""

PACKAGE_NAME = "pystache"
PACKAGE_VERSION = "0.1"

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=desc,
      summary=summ,
      author='Mikeal Rogers',
      author_email='defunkt@github.com',
      url='http://defunkt.github.com/pystache',
      license='GPL 3.0',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      package_data = {'': ['*.js', '*.css', '*.html', '*.txt', '*.xpi', '*.rdf', '*.xul', '*.jsm', '*.xml' ],},
      platforms =['Any'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development :: Libraries :: Python Modules',
