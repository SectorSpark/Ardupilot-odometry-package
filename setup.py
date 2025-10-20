from setuptools import setup

package_name = 'external_odometry'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Me',
    maintainer_email='me@example.com',
    description='External odometry publisher for MAVROS SITL',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'odom_pub = external_odometry.odometry_pub:main',
        ],
    },
)
