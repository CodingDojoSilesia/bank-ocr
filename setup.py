from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'pytest',
    ],
    author='imatw4r',
    author_email='bartek.krzys@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
)
