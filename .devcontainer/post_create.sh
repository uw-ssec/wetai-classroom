# Install braingeneers
${NB_PYTHON_PREFIX}/bin/pip install --no-cache git+https://github.com/uw-ssec/braingeneerspy.git#egg=braingeneers[data,iot,analysis,ml,hengenlab]

# Install Jupyter
python -m pip install jupyter # Install Jupyter package
jupyter notebook notebook --generate-config # Create config file
jupyter notebook password # Set password