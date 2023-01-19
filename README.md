
<h1 align="center">
  <br>
  <img src="https://becode.org/app/uploads/2020/03/cropped-becode-logo-seal.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center">IMMOWEB Data Analyses & Visualization <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
  <br>
  By Anıl EMBEL
  <br>
</h1>


<p align="center">
  <a href="#Scrapping"> Scrapping </a> •
  <a href="#how-to-use">Analyses & Visualization </a> •
  <a href="#download"> ML MODELS </a> •
  <a href="#credits">Required Libraries</a> •
  <a href="#related">Contact</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://media.giphy.com/media/GRmrkmIt9GXncuAz14/giphy.gif)

<img src="https://media.giphy.com/media/GRmrkmIt9GXncuAz14/giphy.gif" width="400" height="300">


## Scrapping

The Scraper Mechanism consists of four different Python documents.

* 1- get_links.py uses Selenium and Beautiful Soup libraries to scrape a website for links and writes them to a file.
* 2- threads.py uses the get_links() function from the first document to scrape a website for links using multiple webdrivers in parallel, and writes the links to a file.
* 3- cleaning.py uses the Beautiful Soup library to parse HTML pages, extract information, and store it in a CSV file.
* 4- main.py is the main code for running the program, which includes the pool function from the second document.

## Analyses & Visualization 

This section consists of 7 separate steps.

## <p style="background-color:#16A085; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:5px 5px;"> Step 1: Small Look and understanding data - In this step, you are quickly examining the data and gaining an understanding of what it contains, such as the number of rows and columns, data types, and overall structure. </p>

## <p style="background-color:#16A085; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 2: Researches about All Columns - In this step, you are researching and understanding the meaning and significance of each column in the dataset. </p>

## <p style="background-color:#16A085; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 3: Data Frame Check - In this step, you are checking the dataframe for any errors or inconsistencies, such as missing values or outliers</p>

## <p style="background-color:#2C3E50; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 4: Small Look Cleaned Data Set If there is more needed - In this step, you are taking a quick look at the cleaned dataset to ensure that it is ready for further analysis. If any further cleaning is needed, it is done in this step. </p>

## <p style="background-color:#2C3E50; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 5: Data Analysis - In this step, you are using various statistical techniques to analyze the data and draw insights from it. </p>

## <p style="background-color:#8B8B00; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 6: Data Interpretation - In this step, you are interpreting the results of the data analysis and making conclusions about the insights that have been gained.</p>

## <p style="background-color:#9B59B6; font-family:newtimeroman; color:#FFF9ED; font-size:125%; text-align:center; border-radius:10px 10px;">Step 7: Data Visualization - In this step, you are creating visual representations of the data, such as charts and graphs, to better communicate the insights and make them more easily understandable for others. This can be done using various libraries like matplotlib, seaborn etc.</p>

## Ml MODELS 

This will be filled out in the future 

## Required Libraries


<div class="container">
<p>import numpy as np</p>
<p>import pandas as pd</p>
<p>import seaborn as sns </p>
<p>import matplotlib.pyplot as plt</p>
<p>from skimpy import clean_columns</p>
</div>


## Contact

Please, contact any of the authors via GitHub.

[Anil](https://github.com/anilembel)

## License

MIT

---


