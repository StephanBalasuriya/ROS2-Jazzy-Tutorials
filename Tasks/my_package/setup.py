from setuptools import find_packages, setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stephan',
    maintainer_email='kanishkabalasuriya2002@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'my_node = my_package.my_node:main'
            'pose_re_pub = my_package.pose_re_pub:main',
            'params_setter = my_package.params_setter:main',
            'twist_from_database = my_package.twist_from_database:main',
            'zero_twist = my_package.zero_twist:main', 
            'param_reader = my_package.param_reader:main',

        ],
    },
)
