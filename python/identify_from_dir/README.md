# Script for identifying images from a directory

## Requirements
python version 3.6 or higher with the following packages installed:
* `exif`

```bash
pip install exif
```


## Usage

1. copy [identify.py](identify.py) to your computer
2. set API_KEY in [identify.py](identify.py) to your [plant.id](https://web.plant.id) api key
3. set DIRECTORY in [identify.py](identify.py) to the directory containing the images you want to identify
4. run the script `python identify.py`
5. script generates a CSV file `plant_id_identification.csv` in directory containing the images (see [example](images/plant_id_identification.csv))
