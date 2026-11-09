import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'fossbot_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@todo.todo',
    description='Projekt interfejsu FossBot',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'click_controller = fossbot_interface.click_controller:main',
            'dashboard_node = fossbot_interface.dashboard_node:main'
        ],
    },
)
