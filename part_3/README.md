## Running instructions

This guide assumes you are running OS X or Linux

# Pre requisites
Make sure your system has:
- Python 3 (Preferably 3.7 and up)
- PIP

Then, install `virtualenv` by running
```shell
sudo pip install virtualenv
```

## Project execution instructions
1. Clone the project's repository
2. Navigate to the folder called `part_3`
3. Create a new virtual environment by running
```shell
virtualenv --python python3 venv
```
4. Activate the virtual environment using
```shell
source venv/bin/activate
```
5. Install dependencies by running
```shell
pip install -r requirements.txt
```
**Note: Dependencies won't be installed globally but in the virtual env**

6. Execute the code! use
```shell
python main.py
```

7. To run all tests, use pytest
```shell
python -m pytest tests
```

Or limit the test file
```shell
python -m pytest tests/test_helpers.py
```
