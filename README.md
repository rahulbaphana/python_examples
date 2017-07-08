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

### Install **nose** on [Ubuntu](https://nose.readthedocs.io/en/latest/)