# ML-Wikipedia-Runner
Machine Learning model that predicts which page best to choose to reach the goal page.

This is a final project for "Introduction to Machine Learning by Università di Macerata" course. Created by Dmytro Zakharov, Daniil Korenkov, Kvaratskheliia David.

## Project presentation
You can download it [here](https://drive.google.com/file/d/1JzHXeJ98Lp0u9z3MlC1IXrBS8sa7xDpq/view?usp=sharing) or from the `presentation` folder.

## What is included in the project?

- `internal/dataset_generator` — logic responsible for generating
the dataset. Main function here is `web_clicker.py` which launches the browser
from the web driver, open the **Six Degrees of Wikipedia** website and
mines the data. In the `inputs` file we included the list of words that is used for the model and
forming the input. `output` is a place where the generated table is stored.
- `internal/model` — place where we trained and saved our model.
- `interface` — scripts that launches the colorful CLI for interacting with a model.

## How to launch and which functions are included?

From the project root folder type in:

- `python3 main.py -m generate` to launch dataset miner
- `python3 main.py -m six-degrees-chart` to show distances distribution from the **Six Degrees of Wikipedia** website
- `python3 main.py -m generator-chart` to show distances distribution for our dataset
- `python3 main.py -m generate-features` to convert generated dataset to one needed for the model (with features)
