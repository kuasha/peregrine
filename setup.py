from distutils.core import setup

setup(
    name='cosmos',
    version='0.01.00.009',
    packages=['cosmos', 'cosmos.admin', 'cosmos.admin.samples', 'cosmos.datamonitor', 'cosmos.dataservice', 'cosmos.rbac', 'cosmos.schema',
              'cosmos.service'],
    url='http://cosmosframework.com',
    license='MIT License',
    author='Maruf Maniruzzaman',
    author_email='marufm@cosmosframework.com',
    description='Thin server application framework',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7'
    ],

    install_requires=['tornado', 'motor', 'mongolog'],

    entry_points = {
        'console_scripts': [
            'cosmosadmin = cosmos.admin.commands:admin_main'
        ]
    }
)