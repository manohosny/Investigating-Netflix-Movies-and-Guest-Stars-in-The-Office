# Netflix Movie Duration Analysis

## Project Overview

This project aims to analyze and visualize the durations of movies available on Netflix from the year 2011 to 2020. The analysis is performed using Python, leveraging the Pandas library for data manipulation and the Matplotlib library for data visualization.

## Features

- Line plot of movie durations from 2011 to 2020
- Scatter plot of movie durations by their release years
- Filtering and subsetting data for specific types of movies
- Color-coded scatter plot based on movie genres

## Requirements

- Python 3.x
- Pandas
- Matplotlib

To install the required packages, run:

```bash
pip install pandas matplotlib
```

## How to Run

1. Clone this repository.
2. Navigate to the project directory.
3. Run the Python script `your_script_name.py`.

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the name of the Python script containing the code.

## Files

- `your_script_name.py`: The main Python script where the analysis and plotting are performed.
- `datasets/netflix_data.csv`: The dataset containing information about movies and shows on Netflix.

## Code Structure

1. **Data Preparation**: The code starts by creating a dictionary of years and durations, which is then converted into a Pandas DataFrame.
2. **Initial Plotting**: A line plot is generated to visualize the trend of movie durations from 2011 to 2020.
3. **Data Loading**: A CSV file containing Netflix data is loaded into a DataFrame.
4. **Data Filtering**: The DataFrame is filtered to only include movies and specific columns like title, country, genre, release year, and duration.
5. **Advanced Plotting**: A scatter plot is created to visualize movie durations by their release years.
6. **Data Subsetting**: Movies with durations less than or equal to 60 minutes are filtered.
7. **Color Coding**: A color-coded scatter plot is generated based on the genre of the movies.

## Author

Abdulrahman Hosny

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Netflix for providing the dataset
- Pandas and Matplotlib communities for the libraries

Feel free to contribute to this project by submitting pull requests or issues.
