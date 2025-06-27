# Rt-to-RI
Rt-to-RI is a Python tool that converts the retention time (Rt) into the corresponding retention index (RI). The resulting data set can be imported into a visualisation program and used to display GC chromatograms with the RI instead of the Rt on the abscissa.

# Installation
1) If necessary, install Python (programming language) and Anaconda (contains Python and other useful packages) as well as a text editor, for example Visula Studio Code.
    - https://www.python.org/downloads/
    - https://www.anaconda.com/download
    - https://code.visualstudio.com/download
2) Clone the repository into a suitable directory (git clone).
3) Open the app.py file.
4) If necessary, install the extentions (see requirements.txt). To install execute pip install -r requirements.txt in the terminal.
5) Run the the file app.py
6) Go in you terminal and copy the presented link ('Dash is running on http://127.X.X.X:XXXX/') in your Browser.
7) Follow the instructions that you will now find in the web application. This way you can convert your raw data.

# Testing the web application
1) Perform all steps in the web application. To do this, use the file ‘Testfile_GC-MS_raw-data.CSV’, which you can find in the repository, and the unchanged alkane mix template (file 'Alkanmix.csv').
2) You should see a preview image. You should also be able to download a converted file with the same content as the file 'Testfile_transformed_data_file.csv' (file in the repository for comparison).

# Background
The retention index (RI) is used in gas chromatography (GC) to standardise the retention time of an analyte independently of the measuring device, the temperature gradient, the column dimension and the gas flow. The RI is a relative value that is characteristic for a substance on a certain stationary phase in a separation column [1]. The RIs of many substances on different stationary phases - mostly DB-1, DB-5, WAX and FFAP - are listed in databases such as the NIST database [2]. Therefore, the RI of a substance can be used as a criterion to identify the substance in addition to the mass spectrum. The aim of this work was to calculate the RI not only for individual peaks, but for the entire GC chromatogram. 

A simple programme was written in Python which transforms the raw data of a chromatogram (pairs of values from retention time (Rt) and the measured intensity) in txt or csv format into a new txt or csv file. For this calculation, a txt file is used, which contains the retention times of an n-alkane standard on the same chromatographic system. The programme calculates the corresponding RI for each data point using the calculation formula according to Kováts [1] and van Den Dool & Kratz [3].
The result is a data set in txt or csv format. The GC chromatogram can then be displayed with the retention index on the abscissa after import into programs such as Excel or Origin.

References:

[1] Kováts E. (1958), Gaschromatographische Charakterisierung organischer Verbindungen. Teil 1: Retentionsindices aliphatischer Halogenide, Alkohole, Aldehyde und Ketone. Helvetica Chimica Acta 41 (7), 1915 – 1932; https://doi.org/10.1002/hlca.19580410703

[2] National Institute of Standards and Technology, NIST Chemistry WebBook, Standard Reference Database; https://doi.org/10.18434/T4D303

[3] van Den Dool, H. & Kratz, P. Dec. (1963), A generalization of the retention index system including linear temperature programmed gas-liquid partition chromatography. Journal of Chromatography 11, 463 - 471; https://doi.org/10.1016/S0021-9673(01)80947-X

# Acknowledgement
A big thank you for the technical support in developing and debugging the web application goes to Jonas.
