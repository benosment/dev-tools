#! /usr/bin/env python
#
# Ben Osment
# Sat Nov 16 10:53:10 2013

"""setup Python projects"""

import argparse
import os
import shutil

# source, dest tuples for filenames to copy
files = [('gitignore', '.gitignore'),
         ('LICENSE', 'LICENSE'),
         ('pre-commit', '.git/hooks/pre-commit'),
        ]


def parse_args():
    # build the command line parser
    parser = argparse.ArgumentParser(description='setup Python projects')
    parser.add_argument('directory',
                        action='store',
                        help='directory of project to initializes')
    parser.add_argument('--force',
                        help='overwrite files',
                        action='store_true')
    args = parser.parse_args()
    return args


def get_src_dir():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    resources_dir = os.path.join(base_dir, 'resources')
    return resources_dir
    

def copy_files(src_dir, dst_dir, force):
    for target in files:
        src_file, dst_file = target
        src_path = os.path.join(src_dir, src_file)
        dst_path = os.path.join(dst_dir, dst_file)
        # don't overwrite the file if exists, unless --force is specified
        if not force:
            if os.path.isfile(dst_path):
                pass
        shutil.copyfile(src_path, dst_path)


def create_dirs(base_dir):
    # create missing directories
    os.mkdir(os.path.join(base_dir, 'tests'))
    # create another directory with the same name as the project
    os.mkdir(os.path.basename(os.path.abspath(base_dir)))


def main():
    # parse the args
    args = parse_args()
    # determine source directory
    src = get_src_dir()
    # copy files
    copy_files(src, args.directory, args.force)
    # create dirs
    create_dirs(args.directory)

if __name__ == '__main__':
    main()
