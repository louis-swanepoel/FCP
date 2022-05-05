# Further Computer Programming Coursework.

Simulating Covid 19 Throughout Bristol University First Year Students.

## Description:

The purpose of the code is to simulate the covid-19 virus throughout the first year accomodations, considering the origin of the student, how social they are, their halls and their course. These conditions can be tweaked within the InitialConditions.csv file. 

## Installing and Running:

This code requires a few pre-installed packages: 

* Matplotlib [Guide](https://matplotlib.org/stable/users/installing/index.html)

* Numpy [Guide](https://numpy.org/install/)

* Plotly [Guide](https://plotly.com/python/getting-started/)

* Pandas [Guide](https://pandas.pydata.org/docs/getting_started/install.html)

* DateTime [Guide](https://pypi.org/project/DateTime/)

If the code is being ran on the linux lab machines, the conda environment can be activated with:
'source /opt/anaconda/2020.07/bin/activate'

Then add the command 'python Main.py' for the code to begin and initial prompts to be asked.
## How to use the code:

The code is simple for the user, and only requires running the main.py file, though all files in the repository must be downloaded into the same directory.

Once ran, the user will be asked when they want the simulation to end, which extends up to the current day, today.

The user will then be asked whether they want to collect any other data, which will lead to the courses, nationality and halls plots being presented. Otherwise, only the SIR model will be presented.

The date of this data collection is asked, and then further prompts specifying the type of data to be represented are asked, the choice between S, I and R. 

Finally, the user will be asked whether they want to see the representation of 1, 2 or 3 variables on the SIR graph. 

The outcome of the code would look something like this: ![Image](https://github.com/louis-swanepoel/FCP/blob/main/Example%20Screenshot.png)

## Credits:

- Louis Swanepoel: [Github User](https://github.com/louis-swanepoel)
- Ludo Oliver: [Github User](https://github.com/xd21736)
- Ted Mellow: [Github User](https://github.com/Ted-Mellow)
- Alex De Oliveira: [Github User](https://github.com/AlexDE6)
