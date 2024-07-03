import shutil
import subprocess
import os
import sys

from coconut import tools

#cfd_solver = 'openfoam.v8'
cfd_solver = 'openfoam.v10'
#csm_solver = 'abaqus.v2022'
csm_solver = 'abaqus.v2023'
cfd_dir = './CFD'
csm_dir = './CSM'

#print("Current PYTHONPATH:", os.environ.get('PYTHONPATH', ''))

# Add the project root to the PYTHONPATH if not already included
#project_root = "/project/home/p200396/philip/coconut"
#if project_root not in sys.path:
#    sys.path.insert(0, project_root)

# Debugging: Print the current sys.path
#print("Current sys.path:", sys.path)

# copy run_simulation.py script to main directory
shutil.copy('../../run_simulation.py', './')

# clean working directories
shutil.rmtree(cfd_dir, ignore_errors=True)
shutil.rmtree(csm_dir, ignore_errors=True)

# create new CFD folder
#shutil.copytree('../setup_files/openfoam3d', cfd_dir)
shutil.copytree('../setup_files/openfoam3d_v10', cfd_dir)
cfd_env = tools.get_solver_env(cfd_solver, cfd_dir)
subprocess.check_call('./setup_openfoam3d.sh', shell=True, cwd=cfd_dir, env=cfd_env)

# create new CSM folder
shutil.copytree('../setup_files/abaqus3d', csm_dir)
csm_env = tools.get_solver_env(csm_solver, csm_dir)
subprocess.check_call('./setup_abaqus3d.sh', shell=True, cwd=csm_dir, env=csm_env)
