A python environment is created using the following code in `run.pbs`:
```
# Create python environment: only needed once!
#python3 -m venv my_python-env
#source my_python-env/bin/activate
#pip install --upgrade pip
#pip install --upgrade pip
#python3 -m pip install "numpy>=1.19.5" "scipy>=1.3.0" "matplotlib==3.1.3"
```
You can uncomment this the first time you submit `run.pbs`. For all subsequent runs, you can comment it.

Note that the following line should also be updated to point to  the directory containing the `coconut` repository
```
export PYTHONPATH=/project/home/p200396/philip:$PYTHONPATH
```