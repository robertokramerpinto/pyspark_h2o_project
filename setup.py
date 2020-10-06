from setuptools import setup, find_packages

setup(
    name='pyspark_h2o_project',
    version='0.1',
    description='pyspark_h2o_project',
    long_description='pyspark_h2o_project',

    # The project's main homepage.
    # url='https://github.com/pypa/sampleproject',

    # Author details
    author='roberto kramer',
    author_email='robertokramerpinto@gmail.com',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs'])
)