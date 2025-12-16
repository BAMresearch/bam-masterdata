#!/usr/bin/env python

import os

import pkg_resources


def calculate_package_size():
    total_size = 0
    for dist in pkg_resources.working_set:
        package_location = dist.location
        if os.path.exists(package_location):
            package_size = sum(
                os.path.getsize(os.path.join(root, file))
                for root, _, files in os.walk(package_location)
                for file in files
            )
            total_size += package_size

    print(f'Total size of installed packages: {total_size / (1024 * 1024):.2f} MB')


# * In the root folder, run `python scripts/pkg_size.py` to calculate the total size of installed packages
if __name__ == '__main__':
    calculate_package_size()
