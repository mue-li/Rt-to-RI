# Rt-to-RI
Rt-to-RI is a Python tool that converts the retention time (Rt) into the corresponding retention index (RI). This can be done for the entire data of a gas chromatography (GC) chromatogram (value pairs of Rt and intensity) in .txt or .csv format. This calculation uses a .csv file containing the retention times of an n-alkane standard mix as reference compounds on the same chromatographic system. The result is a data set in .csv format and an interactive preview image. The resulting data set can be imported into a visualisation programme and used to display GC chromatograms with the RI instead of the Rt on the abscissa.

# Installation
1) If necessary, install Python (programming language) and Anaconda (contains Python and other useful packages) as well as a text editor, for example Visula Studio Code.
    - https://www.python.org/downloads/
    - https://www.anaconda.com/download
    - https://code.visualstudio.com/download
2) Clone or download the repository into a suitable directory (via green button 'Code').
3) If necessary, install the packages by running the command ```pip install -r requirements.txt``` in your terminal.
4) Open the ```app.py``` and run the the file to start the application locally. 
5) Go in your terminal and copy the presented link ('Dash is running on http://127.X.X.X:XXXX/') in your Browser.
6) Follow the instructions that you will now find in the web application. This way you can convert your raw data.

# Testing the web application
To try out the test case, please follow these steps:
1) Perform all steps in the web application. To do this, use the file ```Testfile_GC-MS_raw-data.CSV```, which you can find in the repository, and the unchanged alkane mix template (file ```Alkanmix.csv```).
2) If you have followed the instructions in the web application, you should see a preview image. You should also be able to download a converted file with the same content as the file ```Testfile_transformed_data_file.csv``` (you can find the file in the repository for comparison).

# Background
The retention index (RI) is used in gas chromatography (GC) to standardise the retention time of an analyte independently of the measuring device, the temperature gradient, the column dimension and the gas flow. The RI is a relative value that is characteristic for a substance on a certain stationary phase in a separation column [1]. The RIs of many substances on different stationary phases - mostly DB-1, DB-5, WAX and FFAP - are listed in databases such as the NIST database [2]. Therefore, the RI of a substance can be used as a criterion to identify the substance in addition to the mass spectrum. The aim of this work was to calculate the RI not only for individual peaks, but for the entire GC chromatogram. 

A simple programme was written in Python which transforms the raw data of a chromatogram (pairs of values from retention time (Rt) and the measured intensity) in txt or csv format into a new txt or csv file. For this calculation, a txt file is used, which contains the retention times of an n-alkane standard on the same chromatographic system. The programme calculates the corresponding RI for each data point using the calculation formula according to Kováts [1] and van Den Dool & Kratz [3].
The result is a data set in txt or csv format. The GC chromatogram can then be displayed with the retention index on the abscissa after import into programmes of your choice such as Excel or Origin.

References: <br>
[1] Kováts E. (1958), Gaschromatographische Charakterisierung organischer Verbindungen. Teil 1: Retentionsindices aliphatischer Halogenide, Alkohole, Aldehyde und Ketone. Helvetica Chimica Acta 41 (7), 1915 – 1932; https://doi.org/10.1002/hlca.19580410703 <br>
[2] National Institute of Standards and Technology, NIST Chemistry WebBook, Standard Reference Database; https://doi.org/10.18434/T4D303 <br>
[3] van Den Dool, H. & Kratz, P. Dec. (1963), A generalization of the retention index system including linear temperature programmed gas-liquid partition chromatography. Journal of Chromatography 11, 463 - 471; https://doi.org/10.1016/S0021-9673(01)80947-X

