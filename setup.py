from setuptools import setup, find_packages

setup(
    name='django-tex',
    version='0.1',
    description='A simple Django app to render Latex templates and compile them into Pdf files.',
    url='https://github.com/weinbusch/django-tex',
    author='Martin Bierbaum',
    license='MIT',
    keywords='django latex jinja2',
    packages=find_packages(),
    install_requires=[
        'django>=1.11.4',
        'jinja2>=2.9.6',
    ],
    python_requires='>=3.6.2',
    package_data={
        '': ['*.tex'],
    },
)