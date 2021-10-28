from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()


print('''Message from Author:
I hope this package makes your life easier while working with maxymiser.

Thanks,
Shubham
''')

setup(
    name='maxify',
    version='1.1.2',
    description='A utility to interact with maxymiser with command line',
    author='Shubham Gupta',
    author_email='shubhamg2404@gmail.com',
    packages=find_packages(),
    install_requires=['openpyxl', 'requests'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'maxify=maxify.manage:main'
        ]
    },
    include_package_data=True
)
