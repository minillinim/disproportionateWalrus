from distutils.core import setup

setup(
    name='disproportionateWalrus',
    version='0.0.1',
    author='Michael Imelfort',
    author_email='mike@mikeimelfort.com',
    packages=['disproportionatewalrus', 'disproportionatewalrus.test'],
    scripts=['bin/disproportionateWalrus'],
    url='http://pypi.python.org/pypi/disproportionateWalrus/',
    license='GPLv3',
    description='disproportionateWalrus',
    long_description=open('README.md').read(),
    install_requires=[],
)

