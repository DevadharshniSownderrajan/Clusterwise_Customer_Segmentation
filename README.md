# Customer Segmentation using K-Means Clustering

## Project Overview

This project uses K-Means Clustering, an unsupervised machine learning algorithm, to group mall customers based on their annual income and spending score. A Streamlit web application allows users to enter customer details and predict their cluster.

## Objectives

* Understand customer spending behaviour.
* Group customers into different segments.
* Visualize customer clusters.
* Predict the cluster for a new customer using a web app.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Streamlit
* Joblib

## Workflow

1. Load and explore the dataset.
2. Perform exploratory data analysis (EDA).
3. Select annual income and spending score features.
4. Scale the features using StandardScaler.
5. Use the Elbow Method to select the number of clusters.
6. Train the K-Means clustering model.
7. Visualize clusters and analyze customer segments.
8. Build a Streamlit app to predict the cluster for new customers.

## Customer Segments

The model identifies five customer clusters, which can be interpreted using their income and spending patterns:

* Average income and average spending
* High income and high spending
* Low income and high spending
* High income and low spending
* Low income and low spending

These descriptions are interpretations of the cluster averages; the model itself assigns cluster labels.

## Streamlit Application

Users can enter a customer's annual income and spending score to predict the corresponding cluster.

## Business Benefits

Customer segmentation can help businesses understand different customer groups, plan targeted marketing campaigns, and make better data-driven decisions.

## How to Run the Project

1. Clone this repository.

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure `kmeans_model.pkl` and `scaler.pkl` are in the project folder.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Dataset

The project uses a Mall Customers dataset containing customer details such as gender, age, annual income, and spending score.

## Future Improvements

* Add more customer features.
* Improve the app's visualizations.
* Deploy the application online.
