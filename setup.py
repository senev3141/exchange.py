from setuptools import setup
import re

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ""
with open("exchange/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    try:
        import subprocess

        p = subprocess.Popen(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()

        p = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass

readme = ""
with open("README.rst") as f:
    readme = f.read()

extra_require = {
    "docs": [
        "sphinx",
        "sphinxcontrib_trio",
        "sphinx_rtd_theme",
    ],
}

packages = [
    "exchange",
]

setup(
    name="exchange.py",
    author="Senev",
    url="https://github.com/senev3141/exchange.py",
    project_urls={
        "Documentation": "https://exchangepy.readthedocs.io/en/latest/",
        "Issue Tracker": "https://github.com/senev3141/exchange.py/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="An async API wrapper for the Stack Exchange API.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    extras_require=extra_require,
    python_requires=">=3.9.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
    ],
)
