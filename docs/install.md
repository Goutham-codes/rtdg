# Install

## Using exe file
Clone or download this repo and run the [gui.py](https://github.com/Goutham-codes/rtdg/blob/master/source/gui.py) file.

Or download the [exe file](https://github.com/Goutham-codes/rtdg/blob/master/gui.exe) and run it.

![](https://github.com/Goutham-codes/rtdg/blob/master/docs/img/interface.PNG)

## Running [gui.py](https://github.com/Goutham-codes/rtdg/blob/master/source/gui.py)  file

Create a virtual environment and install the modules in requirements.txt

sh
python -m venv venv

Activate the virtual environment to install the modules in it.
sh
venv\Scripts\activate.bat

Now install the modules.
sh
pip install -r requirements.txt

Running the gui file
sh
python source/gui.py


## Creating exe file

Install the pyinstaller module using pip
sh
pip install pyinstaller

Type the following command to create exe file
sh
pyinstaller source/gui.py --onefile -w

-w for no console.
