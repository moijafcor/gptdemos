conda create -n [PROJECT_NAME] python=3.8
conda activate [PROJECT_NAME]

conda install -c conda-forge python-dotenv
# CPU-only version
conda install -c pytorch faiss-cpu=1.7.4 mkl=2021 blas=1.0=mkl

# GPU(+CPU) version
conda install -c pytorch -c nvidia faiss-gpu=1.7.4 mkl=2021 blas=1.0=mkl

pip install faiss-gpu # For CUDA 7.5+ Supported GPU's.
# OR
pip install faiss-cpu # For CPU Installation
