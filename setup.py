from setuptools import setup
from setuptools import find_packages

setup(
    name="logagg-collector",
    version="0.0.1",
    description="logs aggregation framework",
    keywords="logagg",
    author="Deep Compute, LLC",
    author_email="contact@deepcompute.com",
    url="https://github.com/deep-compute/logagg/logagg_collector",
    license="MIT",
    dependency_links=[
        "https://github.com/deep-compute/pygtail/tarball/master/#egg=pygtail-0.6.1",
        "https://github.com/deep-compute/logagg/logagg_collector",
    ],
    install_requires=[
        "kwikapi==0.4.6",
        "kwikapi-tornado==0.3.3",
        "basescript==0.2.9",
        "diskdict==0.2.4",
        "ujson==1.35",
        "logagg-utils==0.5.0",
        "fuse-python==0.3.1",
    ],
    package_dir={"logagg_collector": "logagg_collector"},
    packages=find_packages("."),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    # test_suite='test.suite_maker',
    entry_points={
        "console_scripts": [
            "logagg-collector = logagg_collector:main",
            "logagg-fs = logagg_fs:main",
        ]
    },
)
