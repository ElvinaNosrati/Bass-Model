## Bass Model Analysis for Lucid Air

### Overview

This project analyzes the diffusion of the **Lucid Air**, a luxury electric vehicle from **TIME's Best Inventions of 2022**, using the **Bass Diffusion Model**. The analysis compares Lucid Air with a past innovation, the **BMW i series**, to estimate the parameters for the Bass Model, predict the diffusion path, and calculate the number of worldwide adopters over time.

The project involves:
- Estimating Bass Model parameters using historical sales data of the BMW i series.
- Predicting the future adoption of the Lucid Air based on these parameters.
- Estimating the number of new and cumulative adopters over the next 20 years.
  
### Project Structure
```
Bass-Model/
├── data/
│   ├── bmw_electric_sales.xlsx          
│   ├── lucid_air_adoption_prediction.csv  
├── img/
│   ├── bmw_sales_plot.png               
│   ├── lucid_air_adopters.png           
│   ├── lucid_air_sales.png              
├── report/
│   ├── report_source.md                 
│   ├── report.pdf                       
├── readme.md                           
├── script1.py                           
├── script2.py                           

```
### Explanation:

- **data/**:
  - `bmw_electric_sales.xlsx`: The Excel file containing historical sales data for the **BMW i series** from 2014 to 2022.
  - `lucid_air_adoption_prediction.csv`: A CSV file containing the predicted adoption for **Lucid Air** over the next 20 years.

- **img/**:
  - `bmw_sales_plot.png`: The bar plot showing **BMW i series sales** over the years.
  - `lucid_air_adopters.png`: The plot showing cumulative and new adopters of **Lucid Air** over time.
  - `lucid_air_sales.png`: The predicted sales curve for **Lucid Air** using the Bass Model.

- **report/**:
  - `report_source.md`: The Markdown source file used to generate the final report.
  - `report.pdf`: The final report in **PDF format**, containing all the analysis, plots, and conclusions.

- **readme.md**:
  - The documentation file, which provides an overview of the project and instructions for usage.

- **script1.py**:
  - This Python script generates the **BMW sales plot** from the historical sales data.

- **script2.py**:
  - This Python script estimates the Bass Model parameters and predicts the future adoption of **Lucid Air** based on the model.
