from setuptools import setup, find_packages

setup(
    name='ReceiptAnalyzer',
    version='1.0.0',
    url='https://github.com/pranjal7842/ReceiptAnalyzer',
    author='Pranjal',
    description='Extract receipt data using the Form Recognizer REST API with Python',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='rest restful api flask swagger openapi flask-restplus form-recognizer',
    packages=find_packages(),
    install_requires=['flask-swagger-ui==3.36.0']
)
