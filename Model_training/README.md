This folder contains training code for the Cloud Attenuation model. There are three groups in total: Regression, Tree-based, and CNNs models.  
1. **Regression model** : The <code>Regression_model.ipynb</code> file contains training code for linear and polynomial regression models.  
   - An input file is <code>separated_DATASET_cloudmask.csv</code>
   - An Output file is <code>Ihat_cmRegress.csv</code>  
   
2. **Tree-based model** : The <code>Tree_based_model.ipynb</code> file contains training code for Random forest and XGBoost models.  
   - Input files are <code>separated_DATASET_cloudmask.csv</code> and <code>separated_DATASET_chred_overview.csv</code>
   - Output files are <code>Ihat_cmTree.csv</code>, <code>Ihat_ovTree.csv</code>, <code>RF_5-fold_crossvalidation_result.csv</code> and <code>XGB_5-fold_crossvalidation_result.csv</code>
