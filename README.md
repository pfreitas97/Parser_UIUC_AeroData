# UIUC-Aerodynamic-Data-Parser

The Applied Aerodynamics Group at UIUC has created one of the largest databases of empirical test results for propellers, particularly small propellers that are typically used in drones. In addition, the Group also hosts one of the largests databases of airfoil geometric files (1,550 distinct airfoils). All of these make the use of UIUC's dataset very attractive to Aerospace Engineers looking to to test the accuracy of their models, conuduct preliminary sizing estimates, among other uses. Unfortunately the entire database does not follow consistent conventions, making the simultaneous use of the entire database somewhat tedious at times. Since I could not find a public repo automating the data wrangling process I decided to publish mine. Hopefully this can help you in your projects as it has helped me in mine.



## Propeller Database

The propeller database is divided into 2 separate volumes, the primary difference between the two is the presence of both imperial and metric data, and 3D printed propellers in the second volume. In general parsing data in the first volume is much easier, since the data was entered in a more consistent format. 

The majority of the code for wrangling propller data is included in the propeller_data_util file. It handles scrapping important information that is included only in the filename, such as the radius and pitch of the propeller. As well as determining the appropriate units for every file, and selecting only a specific subset of the data at a time. Currently I am ignoring several propellers by design (namely the ones that were 3D printed and/or do not include pitch information) since I did not personally need them for my purposes, but it should be a fairly easy fix if you're interested in those as well.

In the near future I intend to make the propeller data utility return a propeller object / list of lists / list of pandas dataframes with all of the relevant information for every propeller or a subset thereof. This is primarily intended for cases where some procedured must be performed on all propellers in dataset (e.g. making a regression model, training a neural net, etc..).


## Airfoil Database

The airfoil geometric files are not by themselves particularly useful, however they can be incredibly helpful when paired with an xfoil api (e.g. xfoil-python: https://github.com/DARcorporation/xfoil-python). Xfoil is a 2D flow solver that predicts actual performance (such as lift and drag) remarkably well (See for instance https://doi.org/10.2514/6.2008-7345). The primary functionality added here is a script to rename the files to be more consistent for easier lookup (e.g. most naca files included  NACA in the file name, however not the naca0012 which was named n0012). 
