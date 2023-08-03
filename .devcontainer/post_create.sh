# Activate Conda env
conda activate international-deploy
conda init
source ~/.bashrc

# Install braingeneers
python -m pip install --force-reinstall --no-cache-dir git+https://github.com/uw-ssec/braingeneerspy.git@update_repo#egg=braingeneers[data,iot,analysis,ml,hengenlab]
