# Further Computer Programming Coursework.

Simulating Covid 19 Throughout Bristol University First Year Students.

## Description:

The purpose of the code is to simulate the covid-19 virus throughout the first year accomodations, considering the origin of the student, how social they are, their halls and their course. These conditions can be tweaked within the InitialConditions.csv file. 

## Installing and running:

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

The code is simple for the user, and only requires running the Main.py file, though all files in the repository must be downloaded into the same directory.

In order for the code to work, the user must input their chosen plots and dates for which they want to see information for. This can all be found and edited within the GraphSelection.csv file. For the 'Main' plot, the user can chose between 3 variables, S, I and R, which must be seperated with a comma for multiple variable demonstration on the plot E.G 'S,R'. For the other plots, only one varaible can be demonstrated at a time, though the dates for these plots can be different. 

Once the Main.py file is ran, the plots will pop up one by one, and can either be saved or closed. Closing the plot will prduce the next plot. 

The outcome of the code would look something like this: ![Image](https://github.com/louis-swanepoel/FCP/blob/main/Example%20Screenshot.png)

## Results of the code: 

The code produces several plots with the users chosen inputs to represent the susceptible, infected and recovered populations within the greater student population. These plots can be moused over to show the exact figures on the x y axis. Each time they pop up they can be saved.
## Credits:

- Louis Swanepoel: [Github User](https://github.com/louis-swanepoel)
- Ludo Oliver: [Github User](https://github.com/xd21736)
- Ted Mellow: [Github User](https://github.com/Ted-Mellow)
- Alex De Oliveira: [Github User](https://github.com/AlexDE6)
