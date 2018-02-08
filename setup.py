from setuptools import setup

setup(
    name='pruebaapp',
    packages=['pruebaapp'],
    version='0.1.0',
    author='Juan David Rodríguez García',
    description='Basic Flask project (package)',
    license='MIT',
    author_email='juanda@juandarodriguez.es',
    include_package_data=True,
    install_requires=[
        'Flask',
        'Redis'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    scripts=['bin/run.py']
)
