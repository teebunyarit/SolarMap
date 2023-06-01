The <code>Data_preparation</code> folders are utilized for downloading data, cleaning it, and generating datasets.  

- The <code>Load_cloud_image.ipynb</code> file is used to download cloud images.
  - Output files are <code>check_avaiable_cloudmask.csv</code> and <code>check_avaiable_overview_chred.csv</code>
 
- The <code>Irradiance_file_creation.ipynb</code> file is used to download estimation irradiance data and aggregrate measurement irradiance files into a single file.
  - Input files are **measurement irradiance** files, <code>plant_metadata.csv</code> and <code>plant_metadata_tiff_index.csv</code>
  - Output files are <code>ihat_only_modelv1.csv</code>, <code>ihat_only_modelv2.csv</code> and <code>ims.csv</code>
  
- The <code>cloudindex_file_creation.ipynb</code> file is used to clean cloud images and extract the cloud index from them.
  - Input files are cloud images and <code>plant_metadata.csv</code>
  - Output files are <code>ci_cloudmask.csv</code> and <code>ci_overview_chred.csv</code>

- The <code>generate_clearsky_variable.ipynb</code> file is used to generate clear sky data: clear-sky irradiance, airmass and zenith angle
  - A input file is <code>plant_metadata.csv</code>
  - A output file is <code>clear_sky.csv</code>

- The <code>Dataset_Cleaning_and_Creation.ipynb</code> file is used to clean and create dataset for training process.
  - Input files are <code>clearsky_data.csv</code>, <code>ims.csv</code>, <code>ims_cleaned.csv</code>, <code>ci_cloudmask.csv</code> (or <code>ci_overview_chred.csv</code>), <code>ihat_only_modelv2.csv</code> and <code>ihat_only_modelv1.csv</code>
  - Output files are <code>DATASET_cloudmask.csv</code>, <code>ims_cleaned.csv</code>, <code>ihat_modelv1.csv</code> and <code>ihat_modelv2.csv</code>

- The <code>split_dataset.ipynb</code> file is used to separate dataset into three paths base on clear sky index


The <code>clearskycal.py</code> file in the <code>CUEESolar</code> folder is module which calculating clear sky data.

