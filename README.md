# Simple room classifier using ai-compare REST API

![AI-Compare API](https://ai-compare.com/static/images/Ai-compare_new.png)

## How it works ?

Simply add your api that you can retrieve in your  [ai-compare account](https://ai-compare.com/my_apis/my_account)

`client = AutoMLVisionClient(api_key='<your_api_key>')`

## The dataset

The dataset is present [here](https://github.com/Arowne/automl_vision_aicompare/tree/master/floor_plan_dataset) and is based on [ROBIN](https://github.com/gesstalt/ROBIN/blob/master/ROBIN.zip) floor plan dataset


| Folder name   | Label name         | Number of samples  |
| ------------- |:------------------:| ------------------:|
| 0             | 3 rooms            | 170                |
| 1             | 4 rooms            | 170                |
| 2             | 5  rooms           | 170                |
