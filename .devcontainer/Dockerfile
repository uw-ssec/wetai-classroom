FROM mcr.microsoft.com/devcontainers/anaconda:0-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends \
#     Glances \
#     wget \
#     curl \
#     ncdu \
#     ffmpeg \
#     rclone \
#     awscli \
#     hdf5-tools \
#     time

# Install additional Python packages
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir \
    jupyterlab-git

# The ADD command below downloads the latest commit information. If it has changed since the last build
# the following layers will not be cached, if it hasn't changed the following layers will rebuild.
# ADD "https://api.github.com/repos/braingeneers/braingeneerspy/commits?per_page=1" /tmp/latest_braingeneers_commit
# RUN python -m pip install --force-reinstall --no-cache-dir git+https://github.com/braingeneers/braingeneerspy.git#egg=braingeneerspy[all]
RUN python -m pip install --no-cache-dir git+https://github.com/uw-ssec/braingeneerspy.git@update_repo#egg=braingeneerspy[data,iot,analysis,ml,hengenlab]
