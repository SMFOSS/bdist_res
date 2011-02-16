from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='bdist_res',
      version=version,
      description="Distutils command for driving the creation packaging of non-python resources (like js, css, etc)",
      long_description=open('README.rst').read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='whit',
      author_email='whit at surveymonkey.com',
      url='http://code.surveymonkey.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['path.py'],
      entry_points="""
      [distutils.commands]
      bdist_res=bdist_res.command:build_resources
      """
      )
