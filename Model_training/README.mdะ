This folder contains training code for the Cloud Attenuation model. There are three groups in total: Regression, Tree-based, and CNNs models.  
1. **Regression model** : The <code>Regression_model.ipynb</code> file contains training code for linear and polynomial regression models.  
   - An input file is <code>separated_DATASET_cloudmask.csv</code>
   - An output file is <code>Ihat_cmRegress.csv</code>  
   
2. **Tree-based model** : The <code>Tree_based_model.ipynb</code> file contains training code for Random forest and XGBoost models.  
   - Input files are <code>separated_DATASET_cloudmask.csv</code> and <code>separated_DATASET_chred_overview.csv</code>
   - Output files are <code>Ihat_cmTree.csv</code>, <code>Ihat_ovTree.csv</code>, <code>RF_5-fold_crossvalidation_result.csv</code> and <code>XGB_5-fold_crossvalidation_result.csv</code>

3. **Deep learning model** : The `CNNsModel_cloudmask.ipynb` and `CNNsModel_cloudmask_overview.ipynb` are contain training code for CNNs model by using only cloud mask layer and using both of cloud mask and red channel layers.
   - Input files of `CNNsModel_cloudmask.ipynb` are `Image_dataset_1layer.csv` and `Attribute_dataset_1layer.csv`
   - Output files of `CNNsModel_cloudmask.ipynb` are the trained models which name are `Cloud2K_1.h5`, `Cloud2K_2.h5`, . .. `Cloud2I_3.h5`
   - Input files of `CNNsModel_cloudmask_overview.ipynb` are `Image_dataset_2layers.csv` and `Attribute_dataset_2layers.csv`
   - Output files of `CNNsModel_cloudmask_overview.ipynb` are the trained models which name are `Cloud2Kv1.h5`, `Cloud2Kv2.h5`, . .. `Cloud2Iv3.h5`
