import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorindigo", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-nish-theme",
    version=ABOUT["__version__"],
    url="https://github.com/NISH-COURSES/tutor-nish-theme",
    project_urls={
        "Code": "https://github.com/NISH-COURSES/tutor-nish-theme",
        "Issue tracker": "https://github.com/NISH-COURSES/tutor-nish-theme/issues",
        "Community": "https://discuss.openedx.org",
    },
    license="AGPLv3",
    author="ZSVN Devs",
    author_email="zameelhassan2024@cs.ajce.in",
    maintainer="ZSVN Devs",
    maintainer_email="zameelhassan2024@cs.ajce.in",
    description="NISH theme plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor>=15.0.0,<16.0.0"],
    entry_points={"tutor.plugin.v1": ["indigo-nish = tutorindigo.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
