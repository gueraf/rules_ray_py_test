FROM rayproject/ray:2.46.0-py312-cpu

RUN sudo apt update && \
    sudo apt install -y \
    zstd \
    git \
    npm && \
    sudo apt clean && \
    sudo rm -rf /var/lib/apt/lists/*

RUN sudo npm install -g @bazel/bazelisk

RUN conda config --add channels conda-forge && \
    conda install -n base "conda-package-handling>=2.4.0" conda-build

RUN git clone --recurse-submodules https://github.com/gueraf/rules_ray_py_test.git
