"""Setup for crane_x7_moveit_config."""

import os
from glob import glob

from setuptools import find_packages
from setuptools import setup

package_name = 'crane_x7_moveit_config'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    # packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('launch', package_name), glob('launch/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Floris Erich',
    maintainer_email='floris.erich@aist.go.jp',
    description='Description of the RT Corporation CRANE X7 robot',
    license='BSD'
)
