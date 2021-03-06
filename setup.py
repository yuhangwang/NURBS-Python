from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='NURBS-Python',
	version='1.0',
	description='NURBS curve and surface calculation algorithms in native Python',
	author='Rauf Bingol',
	license='MIT',
	url='https://github.com/orbingol/NURBS-Python',
	packages=['nurbs'],
	long_description=read('README.md'),
	classifiers=[
	'License :: OSI Approved :: MIT License',
	'Topic :: Scientific/Engineering :: Mathematics'
	]
	)