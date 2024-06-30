from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['antropomorphic_project'],
    package_dir={'': 'src'},
    package_data={'antropomorphic_project': ['launch/*.launch']}
)
setup(**d)