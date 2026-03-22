FROM jupyter/scipy-notebook@sha256:fca4bcc9cbd49d9a15e0e4df6c666adf17776c950da9fa94a4f0a045d5c4ad33

# Set working directory
WORKDIR /home/jovyan/work

# Copy project files into container
COPY . .

# Install additional dependencies
RUN pip install \
    pandas==2.2.2 \
    numpy==1.26.4 \
    scikit-learn==1.4.2 \
    matplotlib==3.8.4 \
    seaborn==0.13.2\
    jinja2==3.1.2 \
    requests==2.31.0 \
    tabulate==0.9.0

# Default command
CMD ["start-notebook.sh"]