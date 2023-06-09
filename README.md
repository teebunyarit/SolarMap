# Improving cloud attenuation model for ground irradiance estimation across Thailand using cloud images from Himawari satellite

This repository is created for version control of our senior project in `2102499: Electrical Engineering Project` during of August 2022 - May 2023. The project detail elaborately describes in [report](http://jitkomut.eng.chula.ac.th/group/nuttamon_boonyarit_solarmap.pdf) (Thai version).

<p align="center">
  <img src="https://github.com/teebunyarit/SolarMap/assets/113121308/4905ccc3-4fe8-499f-abf2-02a670b40149" width="550" height="300" />
</p>

 Nuttamon and I had worked on this project with guidance from Associate Professor Jitkomut Songsiri in my senior year. This project is an extension of the [Thailand Solar Map by CUEE project](http://jitkomut.eng.chula.ac.th/pdf/eesolarmap.pdf) and aims to improve the efficiency of the cloud attenuation model. The proposed model uses cloud images from the [Himawari-8 satellite](https://himawari.optemis.space/)  and physical data for each area. This project develops three types of models: regression models, tree-based models, and deep learning models. The overall process of our project are shown below.

<p align="center">
  <img src="https://github.com/teebunyarit/SolarMap/assets/113121308/f176a0d8-b9c9-4dea-8349-d222a21f4560" width="720" height="350" />
</p>

The best-proposed model is a convolutional neural network (CNN) model in which the least mean absolute error. There are 2 types of the structure of CNN models which are 'Cloud2K' model and 'Cloud2I' model. 'Cloud2K' model is the model mapping to clear-sky index which have 4 sub-structures and Cloud2I' model is the model mapping to estimated irradiance which have 3 sub-structures. The sturcture of CNN models are shown below.
<p align="center">
  <img src="https://github.com/teebunyarit/SolarMap/assets/113121308/74981871-5d7a-4d72-b8f2-62a6deea9a32" width="650" height="400" />
</p>

This repository is composed of the following folders
- **Data_preparetion** are utilized for downloading data, cleaning it, and generating datasets.
- **Model_training** contains training code for the Cloud Attenuation model. There are three groups in total: Regression, Tree-based, and CNNs models.
- **Data_visualization** is used for data and results visualization.
- **DataAndResult** store the CSV files used in this project.


