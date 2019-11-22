from setuptools import find_packages, setup

setup(
    name='flask-restful-boilerplate',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'flask',
        'flask-restful',
    ],
    python_requires='>=3.6',
)
