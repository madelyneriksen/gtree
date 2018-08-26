"""Setup File"""


from setuptools import setup


setup(
    name = 'gtree',
    version = '0.1.0',
    packages = ['gtree'],
    entry_points = {
        'console_scripts': [
            'gtree = gtree.__main__:main'
        ]
    }
)


