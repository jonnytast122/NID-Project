project_name/
│
├── notebooks/                    # Jupyter notebooks for exploration and model training
│   ├── trained_model.ipynb
│   ├── training_with_outlier.ipynb
│   └── training_without_outlier.ipynb
│
├── data/                         # Data directory for storing datasets
│   ├── Cleaned_data.csv
│   ├── Data.csv
│   ├── Test_data.csv
│   └── Train_data.csv
│
├── models/                       # Serialized models and other related files
│   ├── label_encoder.pkl
│   └── random_forest_model.pkl
│
├── graphs/                       # Directory for graph representations and visualizations
│   ├── Digraph.gv
│   └── Digraph.gv.pdf
│
├── src/                          # Source code for the project
│   ├── api.py                    # API module for serving predictions
│   └── app.py                    # Main application module
│
├── README.md                     # Project description and instructions
├── requirements.txt              # Required packages for the project to run
└── .gitignore                    # Specifies intentionally untracked files to ignore


| Training with Outliers            | Pros                                                        | Cons                                               |
|-----------------------------------|-------------------------------------------------------------|----------------------------------------------------|
| More data                         | Provides more data points for the model to learn from.       | May lead to overfitting to the outliers.           |
| More representative of real-world | Outliers can be part of real-world scenarios.                | Adds noise to the data, making learning harder.    |

| Training without Outliers         | Pros                                                        | Cons                                               |
|-----------------------------------|-------------------------------------------------------------|----------------------------------------------------|
| Less noisy data                   | Reduces noise in the data, making it easier to learn.        | Less data available for training the model.        |
| Less likely to overfit            | Reduces the chance of the model overfitting to outliers.     | Data may be less representative of the real world. |


- training_score > testing_score: overfitting
- training_score < testing_score: underfitting
- training_score ~= testing_score: good fit


### Selected Features
```
flag_S0
flag_SF
src_bytes
dst_bytes
logged_in
count
serror_rate
srv_serror_rate
dst_host_srv_count
dst_host_same_srv_rate
dst_host_diff_srv_rate
dst_host_same_src_port_rate
dst_host_serror_rate
dst_host_srv_serror_rate
```


## Normal Attack Detection Endpoints
```json
{
    "flag_S0": 1,
    "flag_SF": 0,
    "src_bytes": 0,
    "dst_bytes": 0,
    "logged_in": 0,
    "count": 100,
    "serror_rate": 1.0,
    "srv_serror_rate": 1.0,
    "dst_host_srv_count": 10,
    "dst_host_same_srv_rate": 0.1,
    "dst_host_diff_srv_rate": 0.7,
    "dst_host_same_src_port_rate": 0.0,
    "dst_host_serror_rate": 1.0,
    "dst_host_srv_serror_rate": 1.0
}
```

## Neptune Attack Detection Endpoint
```json
{
    "flag_S0": 1,
    "flag_SF": 0,
    "src_bytes": 0,
    "dst_bytes": 0,
    "logged_in": 0,
    "count": 100,
    "serror_rate": 1.0,
    "srv_serror_rate": 1.0,
    "dst_host_srv_count": 10,
    "dst_host_same_srv_rate": 0.1,
    "dst_host_diff_srv_rate": 0.7,
    "dst_host_same_src_port_rate": 0.0,
    "dst_host_serror_rate": 1.0,
    "dst_host_srv_serror_rate": 1.0
}
```


## Satan Attack Detection Endpoint
```json
{
    "flag_S0": 0,
    "flag_SF": 1,
    "src_bytes": 0,
    "dst_bytes": 0,
    "logged_in": 0,
    "count": 50,
    "serror_rate": 0.0,
    "srv_serror_rate": 0.0,
    "dst_host_srv_count": 10,
    "dst_host_same_srv_rate": 0.1,
    "dst_host_diff_srv_rate": 0.6,
    "dst_host_same_src_port_rate": 0.5,
    "dst_host_serror_rate": 0.0,
    "dst_host_srv_serror_rate": 0.0
}
```

## Portsweep Attack Detection Endpoint

```json
{
    "flag_S0": 0,
    "flag_SF": 0,
    "src_bytes": 0,
    "dst_bytes": 0,
    "logged_in": 0,
    "count": 5,
    "serror_rate": 0.0,
    "srv_serror_rate": 0.0,
    "dst_host_srv_count": 5,
    "dst_host_same_srv_rate": 1.0,
    "dst_host_diff_srv_rate": 0.0,
    "dst_host_same_src_port_rate": 1.0,
    "dst_host_serror_rate": 0.0,
    "dst_host_srv_serror_rate": 0.0
}
```


## Smurf Attack Detection Endpoint

```json
{
    "flag_S0": 0,
    "flag_SF": 0,
    "src_bytes": 1000,
    "dst_bytes": 0,
    "logged_in": 0,
    "count": 1000,
    "serror_rate": 0.0,
    "srv_serror_rate": 0.0,
    "dst_host_srv_count": 255,
    "dst_host_same_srv_rate": 1.0,
    "dst_host_diff_srv_rate": 0.0,
    "dst_host_same_src_port_rate": 1.0,
    "dst_host_serror_rate": 0.0,
    "dst_host_srv_serror_rate": 0.0
}
```