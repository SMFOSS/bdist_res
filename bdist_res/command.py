from setuptools import Command
from contextlib import contextmanager
import os
import tarfile


class build_resources(Command):
    """
    Command for introspecting a package and building the resources within
    """
    description = "Build any css and js resources"
    user_options = [('zip', 'z', 'use zip to compress'),
                    ('path', 'p', 'path to build'),
                    ('qualifier', 'q', 'what it is. Differentiate from the archive for the python package')]

    def initialize_options(self):
        self.zip = False
        self.path = None
        self.qualifier = 'resources'

    def finalize_options(self):
        pass

    def run(self):
        self.build_assets()

    def build_assets(self):
        from path import path
        folder = path('.').abspath() / self.path
        dist = path('.').abspath() / 'dist'
        if not dist.exists():
            dist.mkdir()
        version = self.distribution.get_version()
        name = self.distribution.get_name()
        outdir = path(dist / "%s-%s-%s" %(name, version, self.qualifier))
        if outdir.exists():
            outdir.rmtree()
        archive = path(outdir + '.tar.gz')
        if archive.exists():
            archive.remove()
        with pushd(folder):
            with tarfile.open(archive, "w:gz") as gz:
                for sdir in path('.').dirs():
                    gz.add(sdir, arcname="%s/%s" %(version, sdir.name))
        print archive.abspath()


@contextmanager
def pushd(dir):
    '''
    Borrowed from Paver
    
    A context manager for stepping into a 
    directory and automatically coming back to the previous one. 
    The original directory is returned. Usage is like this::
    
        from __future__ import with_statement
        # the above line is only needed for Python 2.5
        
        from paver.easy import *
        
        @task
        def my_task():
            with pushd('new/directory') as old_dir:
                ...do stuff...

    '''
    old_dir = os.getcwd()
    os.chdir(dir)
    try:
        yield old_dir
    finally:
        os.chdir(old_dir)
