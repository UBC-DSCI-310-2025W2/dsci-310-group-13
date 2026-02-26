FROM jupyter/scipy-notebook:python-3.11

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
    seaborn==0.13.2

# Default command
CMD ["start-notebook.sh"]