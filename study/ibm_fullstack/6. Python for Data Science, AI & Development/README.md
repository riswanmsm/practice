Installing Jupyter on pipenv

1. activate pipenv environment by runnig
   pipenv shell
2. install ipykernel in environment
   pipenv install ipykernel
3. create virtual kernel
   pipenv run python -m ipykernel install --user --name=my-virtualenv-kernel
4. install jupyter
   pipenv install jupyter
5. open the terminal and goto the project folder then activate pipenv environment by running
   pipenv shell
6. open the project in vs code from terminal by running below while inside the project direcoty
   code .
7. click on the python in the vscode top right side and select the above created virtual kernel
