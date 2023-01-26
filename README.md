

<h1 align="center">
  <br>
  <img src="https://becode.org/app/uploads/2020/03/cropped-becode-logo-seal.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center">IMMOWEB Data Analyses & Visualization <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
  <br>
  By Anıl EMBEL
  <br>
</h1>


<p align="center">
  <a href="##Scrapping"> Scrapping </a> •
  <a href="#how-to-use">Analyses & Visualization </a> •
  <a href="#download"> ML  Models</a> •
  <a href="#credits">Deployment</a> •
  <a href="#related">Contact</a> •
  <a href="#license">License</a>
</p>

<div align="center" >
  <img  src="https://i.hizliresim.com/13o286h.png" width="400" height="700" > 
</div>


## Scrapping

The Scraper Mechanism consists of four different Python documents.

* 1- get_links.py uses Selenium and Beautiful Soup libraries to scrape a website for links and writes them to a file.
* 2- threads.py uses the get_links() function from the first document to scrape a website for links using multiple webdrivers in parallel, and writes the links to a file.
* 3- cleaning.py uses the Beautiful Soup library to parse HTML pages, extract information, and store it in a CSV file.
* 4- main.py is the main code for running the program, which includes the pool function from the second document.

## Analyses & Visualization 

This section consists of 7 separate steps.

 <p> 
<b>Step 1: </b>Small Look and understanding data - In this step, you are quickly examining the data and gaining an understanding of what it contains, such as the number of rows and columns, data types, and overall structure.  

<b>Step 2: </b> Researches about All Columns - In this step, you are researching and understanding the meaning and significance of each column in the dataset. 

<b>Step 3: </b> Data Frame Check - In this step, you are checking the dataframe for any errors or inconsistencies, such as missing values or outliers

<b>Step 4: </b> Small Look Cleaned Data Set If there is more needed - In this step, you are taking a quick look at the cleaned dataset to ensure that it is ready for further analysis. If any further cleaning is needed, it is done in this step. 

<b>Step 5: </b> Data Analysis - In this step, you are using various statistical techniques to analyze the data and draw insights from it. 

<b>Step 6: </b>Data Interpretation - In this step, you are interpreting the results of the data analysis and making conclusions about the insights that have been gained.

<b>Step 7: </b> Data Visualization - In this step, you are creating visual representations of the data, such as charts and graphs, to better communicate the insights and make them more easily understandable for others. This can be done using various libraries like matplotlib, seaborn etc.

</p>


## Ml MODELS 

There are two notebooks in this section.

- ML_ALL.ipynb

- ML-SALE&RENT.ipynb

In my 1st file, I saw that a better result can be obtained when the data is separated as rented and for sale, so you can directly examine the 2nd file.

<p>For ML-SALE&RENT.ipynb document 

In this project, we proposed a machine-learning model for Price Prediction on Real Estate Listings. We preprocessed the data and evaluated multiple algorithms including <b>Linear Regression Method</b> and <b>the Lasso Regression method</b>. Our results showed that Linear Regression Method achieved the highest R-squared error rate with a score of <b>0.875</b> </p>

  

<p>In conclusion, the proposed model has the potential for Linear Regression Method. The model could predict the prices of Estates easily. The prediction is based on The Estates Features. The Features are; </p>


<ul>

<li>Number of rooms</li>

<li>Living Area (m2)</li>

<li>If the Kitchen Fully Equipped</li>

<li>If Estate Furnished</li>

<li>If Estate has a Garden</li>

<li>If Estate has a Swimming Pool </li>

<li>What are the conditions of the statement (6 options)</li>

<li>Type of the house (17 different types)</li>

<li>Their Region (9 different provinces from Belgium)</li>

</ul>

<p>Here is the some graphs for Actual prices and Predicted Prices </p>

<p><b>For Sale</b> </p>

<div align="center" >
  <img  src="https://i.hizliresim.com/l5aeuaw.png"  width="700" height="500" alt="ML MODEL For Sale">
</div>

<p><b>For Rent</b> </p>

<div align="center" >
  <img  src="https://i.hizliresim.com/ovowmeu.png"  width="700" height="500" alt="ML MODEL For Sale">
</div>

## Conclusion

<p><b> What's Learned</b> </p>
<p>After the first 3 stages of the project, I learned how to write data, analyze data, set up the ml model and make the data ready for the model.</p>

<p><b> Results About the Project</b> </p> 
<p>In the model I built on the price estimation, I saw that the most influential factors are obviously the area of ​​the house in square meters, the number of rooms, the presence of a garden and its location.</p>

## Deployment

<p>This area will be filled in previous weeks </p>



## Contact

Please, contact with me via GitHub.

[Anil](https://github.com/anilembel)

## License

MIT

---


