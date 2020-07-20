# UIUC Aerodynamic Data Parsing

The Applied Aerodynamics Group at UIUC has created one of the largest databases of empirical test results for propellers, especially small propellers that are typically used in drones. In addition, the Group also hosts one of the largests databases of airfoil geometric files (1,550 distinct airfoils). All of these features make the use of UIUC's dataset very attractive to Aerospace Engineers looking to to test the accuracy of their models, conduct preliminary sizing estimates, among other uses. Unfortunately the entire database does not follow consistent conventions, making the simultaneous use of the entire database somewhat tedious at times. Since I could not find a public repo automating the data wrangling process I decided to publish mine. Hopefully this can help you in your projects as it has helped me in mine.



## Propeller Database

The propeller database is divided into 2 separate volumes, the primary difference between the two is the presence of both imperial and metric data, and 3D printed propellers in the second volume.

The majority of the code for wrangling propller data is included in the propeller_data_util file. It handles scrapping important information that is included only in the filename, such as the radius and pitch of the propeller. As well as determining the appropriate units for every file, and selecting only a specific subset of the data at a time. Currently I am ignoring several propellers by design (namely the ones that were 3D printed and/or do not include pitch information) since I did not personally need them for my purposes, but it should be a fairly easy fix if you're interested in those as well.

To use the `prop_File_Filter` simply provide a path to the directory containing the propeller datafiles, by default the function will parse all files in the target directory and return the results in **inches** however you can choose the metric option if you'd prefer **meters** or you can use the `contains` option if you'd like to only parse files that contain a specific substring, this can be useful when working exclusively with static test results or only propellers from APC, for instance.  The `verbose` option, when set to true, will printout the names of all the propeller files that were excluded because they were 3D printed or did not contain pitch information. A sample code usage is given below:

```python
filenames,diameters,pitches,AbsolutePaths = prop_File_Filter(path, contains="static", metric=True, verbose=True)
```

The line above would parse through every text file in `path` and output 4 lists, with the values in the diameter and pitch lists in meters, it would only return the static test files and would also print to console the name of every file that was not included due to the lack of pitch information.

To use the `merge_propeller_files`  function provide a path to a directory containing all of the txt files you wish to parse, as well as the two substrings used to identify the type of files being merged. The function will return a pandas dataframe, with the following data: `[Propeller name,Diameter,Pitch,FilePath_1,FilePath_2]` where the first and second filepath point to the propeller files that contain the first and second substrings provided. A sample code usage below:


```python
Propeller_DataFrame = merge_propeller_files(path,"geom","static",metric=False,dropDuplicates=False,sort=True)
```

Here the geometric and static datafiles would be linked in the same dataframe, with each row corresponding to a propeller's specific data. Note that in this example duplicates would not be dropped so propellers with more than one configuration would be kept in the DataFrame, but on the flip side it would not be possible to use the names to uniquely identify each propeller.



## Airfoil Database

The airfoil geometric files are not by themselves particularly useful, however they can be incredibly helpful when paired with an xfoil api (e.g. [xfoil-python](https://github.com/DARcorporation/xfoil-python) ). Xfoil is a 2D flow solver that predicts airfoil performance (such as coefficeint of lift and drag) remarkably well (See for instance https://doi.org/10.2514/6.2008-7345). The primary functionality added here is a script to rename the files to be more consistent for easier lookup (e.g. most naca files included  NACA in the file name, however not the naca0012 which was named n0012). 



## Download util

If you'd prefer to download the entire database from source, you can import the functions  `downloadPropellerData`  and/or `downloadAirfoilData` then simply call them from the appropriate working directory to download the files directly.  The propeller database available at UIUC includes additional data which I did not include, such as pictures, plots of the text files and html files. Currently there is no difference between the airfoil database in the source and the one included here.
