"""Setup for crane_x7_description."""

import os
from glob import glob

from setuptools import find_packages
from setuptools import setup

package_name = 'crane_x7_description'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    # packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes', 'visual'), glob('meshes/visual/*')),
        (os.path.join('share', package_name, 'meshes', 'collision'), glob('meshes/collision/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Floris Erich',
    maintainer_email='floris.erich@aist.go.jp',
    description='Description of the RT Corporation CRANE X7 robot',
    license='BSD'
)
