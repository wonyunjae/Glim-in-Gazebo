from setuptools import find_packages, setup

package_name = 'map_converter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/nav2_map_convert.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wynz',
    maintainer_email='wyj5578@koreatech.ac.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'map_converter = map_converter.map_converter:main',
        ],
    },
)
