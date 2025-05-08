FROM cimg/python:3.12.10-node

RUN sudo npm install -g @bazel/bazelisk

RUN sudo apt update && \
    sudo apt install -y \
    pipx zstd && \
    sudo apt clean && \
    sudo rm -rf /var/lib/apt/lists/*

RUN wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" -O /tmp/miniconda.sh && \
    chmod +x /tmp/miniconda.sh && \
    /tmp/miniconda.sh -b && \
    rm /tmp/miniconda.sh && \
    ~/miniconda3/bin/conda config --add channels conda-forge && \
    ~/miniconda3/bin/conda install -n base "conda-package-handling>=2.4.0" conda-build

RUN pipx install ray[default]==2.45.0

# export RAY_CONDA_HOME=$(realpath ~/miniconda3/) && yes | ray start --head &
# git clone --recurse-submodules https://github.com/gueraf/rules_ray_py_test.git && cd rules_ray_py_test/rules_ray_py && git pull origin main && cd .. && bazelisk run examples/py_ray_hello_world:hello_world_ray_job -- --wait=true