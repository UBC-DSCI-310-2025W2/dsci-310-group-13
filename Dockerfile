FROM jupyter/scipy-notebook@sha256:fca4bcc9cbd49d9a15e0e4df6c666adf17776c950da9fa94a4f0a045d5c4ad33

# Set working directory
WORKDIR /home/jovyan/work

# Switch to root to install system-level packages (Quarto)
USER root

# Install Quarto
RUN ARCH=$(dpkg --print-architecture) && \
    curl -L -o quarto.tar.gz "https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-${ARCH}.tar.gz" && \
    mkdir -p /opt/quarto && \
    tar -xzf quarto.tar.gz -C /opt/quarto --strip-components=1 && \
    ln -s /opt/quarto/bin/quarto /usr/local/bin/quarto && \
    rm quarto.tar.gz

# Switch back to the regular notebook user for security
USER ${NB_USER}

# Copy project files into container
COPY . .

# Install additional dependencies
RUN pip install \
    click==8.1.7 \
    pandas==2.2.2 \
    numpy==1.26.4 \
    scikit-learn==1.4.2 \
    matplotlib==3.8.4 \
    seaborn==0.13.2\
    jinja2==3.1.2 \
    requests==2.31.0 \
    tabulate==0.9.0 \ 
    pytest==8.3.4 \
    pandera==0.30.1

# Default command
CMD ["start-notebook.sh"]