from setuptools import setup, find_packages

setup(
    name='django-tex',
    description='A simple Django app to render Latex templates and compile them into Pdf files.',
    url='https://github.com/weinbusch/django-tex',
    author='Martin Bierbaum',
    license='MIT',
    keywords='django latex jinja2',
    packages=find_packages(exclude=['tests']),
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
        ],
    install_requires=[
        'django>=1.11.4',
        'jinja2>=2.9.6',
    ],
    python_requires='>=3.6.2',
    package_data={
        '': ['*.tex'],
    },
)