# BFVM23PROG2

Data processing Programming course for DSLS 
Times series study cases will be provided soon

see also <a href ="https://fennaf.gitbook.io/bfvm22prog1/">gitbook link</a>

- `assessment` folder: In this folder you find all the assignments
- `scripts` folder: Demo scripts such as unit testing scripts and creating sql database
- `study cases` folder: Examples of study cases for analysis of both continous and categorical data
- `tutorials` folder: Tutorials for specific topics


## Create a virtual environment to install your packages
Login the linux grid. Open the terminal. Choose a path and a name for your virtual environment, for instance `.venv/dsls`


```
#create a new environment
python3 -m venv {path/to/new/virtual/environment} {name}

#activate the virtualenv
source {path/to/new/virtual/environment}{name}/bin/activate 

#create jupyter notebook kernel for venv
pip install ipykernel
python -m ipykernel install --user --name={name}
pip install jupyter

#install required packages
pip install numpy
pip install pandas
pip install seaborn
pip install bokeh
```

make sure that you use the created kernel in your jupyter notebook or visual studio code

contact information: f.feenstra@pl.hanze.nl
