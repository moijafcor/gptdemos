# Environment Setup

`conda create -n [PROJECT_NAME] python=3.8`
`conda activate [PROJECT_NAME]`

`conda install -c conda-forge python-dotenv`

## CPU-only Systems

`conda install -c pytorch faiss-cpu=1.7.4 mkl=2021 blas=1.0=mkl`
`pip install faiss-cpu # For CPU Installation`

## GPU(+CPU) Systems

`conda install -c pytorch -c nvidia faiss-gpu=1.7.4 mkl=2021 blas=1.0=mkl`
`pip install faiss-gpu # For CUDA 7.5+ Supported GPU's.`


## PDF Oracle

In order to run pdforacle.py you need to use streamlit:

`streamlit run pdforacle.py`
