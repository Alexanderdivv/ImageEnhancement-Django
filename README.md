# Image-Enhancement
Kode Program untuk Pengolahan Citra Digital

## Gunakan requrement.txt untuk download dependancy

## Installation and Setup Guide for Unix/Linux

### For Model

1. Clone the Github Repository

```
$ git clone https://github.com/Alexanderdivv/ImageEnhancement-Django.git && cd ImageEnhancement-Django/
```

2. Create a new Environment for the Project using virtualenv

**Note** - Install pip package manager from [here](https://pip.pypa.io/en/stable/installing/)

```
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```


3. Install all the necessary Packages in requirements.txt using pip package manager

```
$ pip install -r requirements.txt
```

4. Change Directory to that of test_model.py

```
$ cd Image-Enhancement/
```

5. Run the model
* If you have a gpu then put use_gpu to true else to false

For ex -

```
$ python3 PCD.ipynb use_gpu=false
```

### For WebSite

1. Clone the Github Repository

```
$ git clone https://github.com/Alexanderdivv/ImageEnhancement-Django.git && cd ImageEnhancement-Django/
```

2. Create a new Environment for the Project using virtualenv

**Note** - Install pip package manager from [here](https://pip.pypa.io/en/stable/installing/)

```
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```


3. Install all the necessary Packages in requirements.txt using pip package manager

```
$ pip install -r requirements.txt
```

4. Change Directory to run the Django Server

```
$ cd src/
```

5. Run server on your machine

```
$ python3 manage.py runserver
```

