# Install braingeneers
${NB_PYTHON_PREFIX}/bin/pip install --no-cache git+https://github.com/uw-ssec/braingeneerspy.git#egg=braingeneers[data,iot,analysis,ml]

# Install Jupyter
${NB_PYTHON_PREFIX}/bin/pip install jupyter
jupyter notebook --generate-config # Create config file
