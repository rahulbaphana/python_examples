# Python examples using TDD

## **Windows 7 Installation**

### Download **Python 3** [latest](https://www.python.org/downloads/) and run the executable

### Add it to the **PATH**

### Verify **Python 3** installation from power shell or git bash or command line tool installed
```
> python3 -V
```

### Install [pip](https://pip.pypa.io/en/stable/installing/) and add it to **PATH**

### Install **py.test** 
```
> pip install -U pytest
```

### Run all tests
```
> python3 setup.py test
```

### Output after running the tests
```
➜  python_examples git:(master) python3 setup.py test
running pytest
Searching for pytest
Best match: pytest 3.1.2
Processing pytest-3.1.2-py3.6.egg

Using ~/python_prac/python_examples/.eggs/pytest-3.1.2-py3.6.egg
Searching for py>=1.4.33
Best match: py 1.4.34
Processing py-1.4.34-py3.6.egg

Using ~/python_prac/python_examples/.eggs/py-1.4.34-py3.6.egg
running egg_info
writing UNKNOWN.egg-info/PKG-INFO
writing dependency_links to UNKNOWN.egg-info/dependency_links.txt
writing top-level names to UNKNOWN.egg-info/top_level.txt
reading manifest file 'UNKNOWN.egg-info/SOURCES.txt'
writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
running build_ext
=============================================== test session starts ===============================================
platform darwin -- Python 3.6.1, pytest-3.1.2, py-1.4.34, pluggy-0.4.0 -- /usr/local/opt/python3/bin/python3.6
cachedir: .cache
rootdir: ~/python_prac/python_examples, inifile: setup.cfg
collected 4 items

tests/test_number_equality.py::TestCheckNumbers::test_add_two_parameters PASSED
tests/test_shopping_cart.py::TestShoppingCart::test_empty_shopping_cart PASSED
tests/test_shopping_cart.py::TestShoppingCart::test_product_added_to_cart PASSED
tests/test_shopping_cart.py::TestShoppingCart::test_product_added_to_cart_with_quantity PASSED

============================================ 4 passed in 0.02 seconds =============================================
```

## **Mac Installation**

### Install **Python 3** latest
```
$ brew install python3
```

### Verify **Python 3** installation
```
$ python3 -V
```

### Install **[nose](https://nose.readthedocs.io/en/latest/)**
```
$ easy_install nose==1.3.7
```

### Running tests on this repo in verbose mode
```
$ nosetests -v
```
### Below command will **not** create the **.pyc** files and also capture any console output
```
$ nosetests --no-byte-compile  -s -v
```

### if using **py.test** for running tests
```
$ python3 setup.py test
```

## **Ubuntu 16.04 Installation**

### Installing **Python 3** on [Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)

### Installing **py.test** on [Ubuntu 16.0.04](https://docs.pytest.org/en/latest/getting-started.html)

### Install **nose** on [Ubuntu](https://nose.readthedocs.io/en/latest/)