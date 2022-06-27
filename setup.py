from importlib.metadata import entry_points
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description_text = readme_file.read()

setup (
    name="bosch_career",
    version="1.0.1",
    description="Educational package about package security and the question what 'being a software company' means.",
    long_description=long_description_text,
    author="Frederik S. Held",
    author_email="kontakt@frederikheld.de",
    license="GNU GPLv3",
    packages=["bosch_career"],
    package_dir={ "bosch_career": "bosch_career/" },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Security",
        "Topic :: Software Development"
    ],
    entry_points={
        "console_scripts": ["bosch_career=bosch_career.__main__:main"]
    },
    keywords="education security recruiting fail",
    python_requires=">=2.7"
)