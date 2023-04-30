# DataPrepCV

# Mosquito Dataset Preparation

This repository contains the necessary tools for creating and organizing the mosquito dataset used in the VectorCam research project. It includes two Jupyter notebooks and associated utility files to handle the dataset.

## Requirements

- Python 3.6+
- Jupyter Notebook
- pandas
- NumPy
- dotenv

## Installation

1. Clone this repository to your local machine.

```sh
git clone https://github.com/your_username/Mosquito-Dataset-Preparation.git
```

2. Change the directory to the project folder.

```sh
cd Mosquito-Dataset-Preparation
```

3.   Create a virtual environment and activate it.

```sh
python -m venv venv
source venv/bin/activate
```

4.   Install the required packages.

```sh
pip install -r requirements.txt
```

5.    Create a .env file in the root directory of the repository to store your database access credentials. Replace your_username, your_password, and your_url with the actual values.

```makefile
dp_export_username=your_username
dp_export_password=your_password
dp_export_url=your_url
```

## Usage

This repository contains two Jupyter notebooks:

1. `download_data.ipynb`: Downloads data from the database, stores it into a CSV file and creates an associated image folder. It also cleans up the CSV to get rid of unnecessary test images.
2. `train_test_preparation.ipynb`: Selects columns of interest used to train mosquito classifiers, organizes images into folders based on data_source, and creates train-test splits for all data. It also creates train-test folders (and class folders inside them) according to the ImageNet data organization style. This notebook serves as a demo script to show users how to perform these tasks, rather than being a complete script to run all at once.

To run the notebooks, start the Jupyter Notebook server:

```sh
jupyter notebook
```

Then, navigate to the desired notebook in your web browser and follow the instructions within the notebook.

## Acknowledgements

This project is part of the VectorCam research project under the supervision of Dr. Soumyadipta Acharya from the JHU CBID initiative. The dataset prepared using these tools is used to train a lightweight CNN-based algorithm for malaria vector surveillance in Uganda.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

