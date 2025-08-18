[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16893134.svg)](https://doi.org/10.5281/zenodo.16893134)

# Rt-to-RI
*Rt-to-RI* is a Python tool that converts the retention time (Rt) into the corresponding retention index (RI). This can be done for the entire data of a gas chromatography (GC) chromatogram (value pairs of Rt and intensity). The input is the raw data file of the sample chromatogram in .txt or .csv format and a second .csv file containing the retention times of an n-alkane standard mix on the same chromatographic system. The output is a single data set in .csv or .xlsx format and an interactive preview image. The new data file can then be imported into a visualisation programme used to display the GC chromatogram with the RI on the abscissa and for further processing.

# Web-Application
*Rt-to-RI* is available online via the following link: 
https://cclh50.chm.tu-dresden.de/app

Alternatively, you can install the tool on your computer and use it locally by following the installation instructions.

If you use *Rt-to-RI* tool, please cite this work!
L. Müller, J. M. Zimmermann, T. J. Simat (2025): Rt-to-RI Python tool [Computer software], Zenodo, [DOI 10.5281/zenodo.16893056.](https://doi.org/10.5281/zenodo.16893134) 

# Installation
1) If necessary, install Python (programming language) or Anaconda (contains Python and other useful packages).
    - https://www.python.org/downloads/
    - https://www.anaconda.com/download
2) Clone or download the repository into a suitable directory.
3) If necessary, install the packages by running the command ```pip install -r requirements.txt``` in your terminal.
4) Open the ```app.py``` and run the the file to start the application locally. 
5) Copy the presented link ('Dash is running on http://127.X.X.X:XXXX/') in your Browser.
6) Follow the instructions that you will now find in the web application. This way you can convert your raw data.

# Testing the web application
To try out the test case, please follow these steps:
1) Perform all steps in the web application. To do this, use the file ```Testfile_GC-MS_raw-data.CSV```, which you can find in the repository, and the unchanged alkane mix template (file ```Alkanmix.csv```).
2) If you have followed the instructions in the web application, you should see a preview image. You should also be able to download a converted file with the same content as the file ```Testfile_transformed_data_file.csv``` (you can find the file in the repository for comparison).

# Background
The retention index (RI) is used in gas chromatography (GC) to standardise the retention time of an analyte independently of the measuring device, the temperature gradient, the column dimension and the gas flow. The RI is a relative value that is characteristic for a substance on a certain stationary phase in a separation column [1]. The RIs of many substances on different stationary phases - mostly DB-1, DB-5, WAX and FFAP - are listed in databases such as the NIST database [2]. Therefore, the RI of a substance can be used as a criterion to identify the substance in addition to the mass spectrum. The aim of this work was to calculate the RI not only for individual peaks, but for the entire GC chromatogram. 

A programme was written in Python which transforms the raw data of a chromatogram (pairs of values from retention time (Rt) and the measured intensity) in txt or csv format into a new txt or csv file. For this calculation, a txt file is used, which contains the retention times of an n-alkane standard on the same chromatographic system. The programme calculates the corresponding RI for each data point using the calculation formula according to Kováts [1] and van Den Dool & Kratz [3].
The result is a data set in txt or csv format. The GC chromatogram can then be displayed with the retention index on the abscissa after import into programmes of your choice such as Excel or Origin.

References: <br>
[1] Kováts E. (1958), Gaschromatographische Charakterisierung organischer Verbindungen. Teil 1: Retentionsindices aliphatischer Halogenide, Alkohole, Aldehyde und Ketone. Helvetica Chimica Acta 41 (7), 1915 – 1932; https://doi.org/10.1002/hlca.19580410703 <br>
[2] National Institute of Standards and Technology, NIST Chemistry WebBook, Standard Reference Database; https://doi.org/10.18434/T4D303 <br>
[3] van Den Dool, H. & Kratz, P. Dec. (1963), A generalization of the retention index system including linear temperature programmed gas-liquid partition chromatography. Journal of Chromatography 11, 463 - 471; https://doi.org/10.1016/S0021-9673(01)80947-X

# Contributing
You are welcome to contribute to the web application, whether with simple comments or with ideas for the code and implementation. <br>
Also feel free to ask questions if you need support! 

To do this, please use the 'Issues' tab of this repository.

# Contact information
The authors can be contacted by email:
lina.mueller@tu-dresden.de
thomas.simat@tu-dresden.de

Please also visit the website of our working group on the Dresden University of Technology website:
https://tu-dresden.de/mn/chemie/lc/lc2
