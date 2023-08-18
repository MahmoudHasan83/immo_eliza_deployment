# immo_eliza_deployment

# Project Description
After gathering over 20,000 dataset, This dataset has been used for training/testing to create a prediction model. the prediction model then saved and implemented using FAST API 
and then Dockerized to be used to predict the new houses in Belgium

# Program description (workflow)
Overall:  This is a FAST API implementation of the linear regression model to predict the prices of the houses in belgium based on training sets from the immoweb website.

1. The program has three main folders model, predict and preprocessing
2. At first the data will be sent to the API inside the main.py ,  which then sent to the preprocessing to be formulated in the right format. the ML model will be loaded and then
3. The ML model will be loaded and then the preprocessed vector will be fetched inside the model to produce the prediction which will eventually will be send back to the user.

# Installation
Create a phython virtual environement
Install libraries ( Requests, BeautifulSoup, Chain, Pandas,Fastapi,numpy,pydantic,Literal,predict )
Install Docker desktop

After installing Docker open terminal and inside the directory of the main folder that contains the docker file ' Dockerfile " Run this command:

```bash
docker build -t <choose-image-name> .
```

# Usage
Make price predictions on real estate sales in Belgium.

Creation of the docker container for the ML prediction model to be used later to predict the prices of the houses in belgium.

# Visuals


# Contributors
Mahmoud Hasan<br>


# Timeline
- Duration: `4 days`




