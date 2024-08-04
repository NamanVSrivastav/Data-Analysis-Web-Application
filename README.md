# Django CSV Data Analysis Web Application

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis, and display the results and visualizations on a web interface. The project demonstrates basic functionalities like file upload, data processing, and data visualization using Python libraries such as pandas, numpy, matplotlib, and seaborn.

## Technical Information Summary

1. **Handling Missing Data**:
-   Missing data is managed by either removing incomplete rows or imputing missing values using the mean or median. This ensures accurate and reliable analysis by preventing biases in the data.

2. **Data Analysis**:
-   Key statistics, such as mean, median, and standard deviation, are calculated to provide insights into the dataset's central tendencies and variability. The mean gives the average, the median represents the middle value, and the standard deviation measures data dispersion.

3. **Data Visualization**:
-   Visualizations, such as histograms with KDE plots, are generated using seaborn and matplotlib. These plots help users easily understand data distributions and identify patterns.

4. **Purpose and Benefits**:
-   The project offers a robust approach to data analysis, providing users with tools to clean data, calculate essential statistics, and visualize distributions. It ensures data integrity and flexibility, allowing users to analyze any numerical column in their uploaded CSV files.

## Features

1. **File Upload**:
   - Users can upload CSV files for analysis through a simple web form.
   - The uploaded files are temporarily stored for processing.

2. **Data Processing**:
   - The application uses pandas to read the uploaded CSV file.
   - It displays the first few rows of the data.
   - It calculates summary statistics (mean, median, standard deviation) for specified numerical columns.
   - Missing values are identified and handled appropriately.

3. **Data Visualization**:
   - Basic plots such as histograms are generated for numerical columns.
   - Visualizations are integrated with pandas using matplotlib and seaborn.
   - The generated plots are displayed on the web page.

4. **User Interface**:
   - A simple and user-friendly interface is provided using Django templates.
   - The interface displays data analysis results and visualizations in an organized manner.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or higher
- pandas
- matplotlib
- seaborn

### Installation

1. **Clone the Repository**:
   - git clone https://github.com/NamanVSrivastav/Django-Project-VE3.git
   - cd django-csv-analysis
    
2. **Create and Activate a Virtual Environment**:
   - python -m venv env
   - source env/bin/activate  
    
3.**Install Dependencies**:
   - pip install -r requirements.txt
    
4.**Database Migration**:
   - python manage.py migrate
    
5.**Run the Server**:
   - python manage.py runserver

6.**Access the Application**:
   - Open a web browser and navigate to http://127.0.0.1:8000/.



## Code Highlights

1. **views.py**:

Handles file uploads and data analysis.
Uses pandas for data manipulation and seaborn/matplotlib for visualization.
Provides the logic for rendering templates with analysis results.

2. **Templates**:

- upload.html: Allows users to upload a CSV file.
- result.html: Displays analysis results, including summary statistics and visualizations.

3. **Sample CSV File**

- For testing purposes, include a sample CSV file named sample_data.csv in the root directory of the project. This file can contain data similar to the following structure:

- Name,Age,Height,Weight,Sleep Duration
- John Doe,25,175,70,7
- Jane Smith,30,160,60,6.5
...

### Handling Missing Data

- Missing data in the specified column for analysis. If missing data is present, it is either removed or filled with appropriate values before performing any statistical analysis.

### Future Enhancements

- Extend the data visualization options with more plot types.
- Implement more advanced data analysis techniques.
- Allow users to select multiple columns for analysis.
- Enhance the user interface with additional styling and interactivity.
- Currently, the application analyzes only the "Sleep Duration" column. In future enhancements, we plan to support analysis of other numerical columns as well.



For any questions or issues, please contact [vsnaman2002@gmail.com].
