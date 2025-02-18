import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

matchResult = pd.read_csv('../kaggle-data/MNCAATourneyDetailedResults.csv')