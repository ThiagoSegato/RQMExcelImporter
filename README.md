## RQMExcelImporter
Extracts items from the test plan. 

This project was based on:
[IBM Engineering Test Management (ETM) Excel/Word Importer Utility](https://jazz.net/wiki/bin/view/Main/RQMExcelWordImporter)

### How to use
    
    $ pip install RQMExcelImporter
    >>> import RQMExcelImporter  
    >>> RQMExcelImporter.convert('your_rqms_file')

### Sample of a conversion
![Screenshot_20220522_210424](https://user-images.githubusercontent.com/26276218/169722065-1247132e-0866-4721-9653-628b563d0d45.png)

### Steps to test source code locally with two example files

1. Create environment using virtualenv

`virtualenv venv`

2. Install all the packages necessary

`pip install -r requirements.txt`

3. Run tests

`python -m unittest tests.test_RQMExcelImporter`

### Steps to create that package and distribute to PyPI

1. Install package to globally way if not installed already

`pip install twine`

2. Create the source distribution of the package

`python setup.py sdist`

3. Upload the source distribution on PyPI

`twine upload dist/*`
