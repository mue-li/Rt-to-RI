---
title: 'Rt-to-RI – A simple Python programme to transform the retention time (Rt) into the retention index (RI) for gas chromatography chromatograms'
tags:
  - Python
  - retention time
  - retention index
  - gas chromatography
  - chromatograms
  - analytical chemistry
authors:
  - name: Lina Müller
    affiliation: 1
  - name: Jonas M. Zimmermann
    affiliation: 2
  - name: Thomas J. Simat
    affiliation: 1
affiliations:
 - name: Technische Universität Dresden, Germany
   index: 1
   ror: 042aqky30
 - name: Technical advisor (unaffiliated), Germany
   index: 2
date: 08 July 2025
bibliography: paper.bib

---

# Summary
*RT-to-RI* is a simple programme written in the Python programming language that converts the retention time (Rt) into the corresponding retention index (RI) for the data of a gas chromatography (GC) chromatogram (value pairs of Rt and the measured intensity) (see \autoref{fig:abs}). The programme calculates the corresponding RI for each data point using the calculation formula according to Kováts [@kovats] and van Den Dool & Kratz [@vanDen]. The input in the presented programme is the raw data file of the sample chromatogram in .txt or .csv format and a second .csv file containing the retention times of an n-alkane standard mix on the same chromatographic system. The output is a single data set in .csv format and an interactive preview image. The new data file can then be imported into programmes such as Excel [@excel], Origin [@origin] or others. Here, the data can be visualized as a GC chromatogram with the RI on the abscissa and be used for further processing.

# Statement of need
The retention index is used in gas chromatography to normalise the retention time of an analyte independently of the measuring device, the temperature gradient, the column dimension and the gas flow. The RI is a relative value that is characteristic of a substance on a specific stationary phase in a separation column [@kovats]. The RIs of many substances on different stationary phases - mostly DB-1, DB-5, WAX and FFAP - are listed in databases such as the NIST database [@nist]. Therefore, the RI of a substance can be used as a criterion to identify the substance in addition to the mass spectrum. This is particularly important for homologous series of substances whose mass spectra are highly similar but can be differentiated by their RI.

The aim of the work was to calculate the RI not only for individual peaks, but also for the entire GC chromatogram. The transformed chromatogram with a normalised RI abscissa makes it easier and clearer to compare chromatograms from independent measurements. 

The target group for this programme includes all analysts who work with GC, for example chemists, food chemists, toxicologists, biologists, environmental scientists and lots more.

# State of the field
As far as the authors are aware, people convert the retention time into the RI chromatogram in a non-automated way themselves. While some integrated software tools in measuring devices can calculate the RI of integrated peaks, to the best of our knowledge they do not convert the entire chromatogram.

For processing, raw data (e.g. in .txt or .csv format) of chromatograms are imported into programmes such as Excel [@excel] or Origin [@origin] in order to process them for scientific papers, posters and presentations. The authors are currently not aware of any easily available, customisable tools for converting the retention time to RI for an entire raw data files in .txt or .csv format. 
*Rt-to-RI* was developed to offer an easily accessible and easy-to-use solution. *Rt-to-RI* closes the gap in the workflow between receiving the raw data from the measuring device and further processing the chromatograms in a programme of choice. The *Rt-to-RI* converter can be easily integrated into the workflow and reduces the workload when processing chromatogram data.

# Authors’ Contribution
L. Müller wrote the manuscript and developed the scientific core element of the programme. J.M. Zimmermann contributed technical advice and support on general programming. T.J. Simat provided the conceptualisation and contributed to the manuscript. 


# References