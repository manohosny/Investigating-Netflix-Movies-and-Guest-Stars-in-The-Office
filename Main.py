# Import the Pandas library
import pandas as pd
# Import the Matplotlib library for plotting
import matplotlib.pyplot as plt

# Create lists for years and durations of movies
years = [i for i in range(2011,2021)]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary using the years and durations lists
movie_dict = {"years":years ,"durations":durations}

# Print the dictionary to the console
print(movie_dict)

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame to the console
print(durations_df)

# Create a new figure for plotting
fig = plt.figure()

# Plot the years against the durations
plt.plot(years, durations)

# Add a title to the plot
plt.title("Netflix Movie Durations 2011-2020")

# Display the plot
plt.show()

# Read a CSV file into a DataFrame
netflix_df = pd.read_csv("datasets/netflix_data.csv")

# Print the first five rows of the DataFrame
print(netflix_df[0:5])

# Filter the DataFrame to only include movies
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']

# Select specific columns from the DataFrame
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset[0:5])

# Create a new figure with a larger size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of movie durations against their release years
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])

# Add a title to the plot
plt.title("Movie Duration by Year of Release")

# Display the plot
plt.show()

# Filter movies that have a duration shorter than or equal to 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] <= 60]

# Print the first 20 rows of short movies
print(short_movies[0:20])

# Initialize an empty list to store colors
colors = []

# Loop through the DataFrame to assign colors based on the genre
for lab, row in netflix_movies_col_subset.iterrows() :
    if row['genre'] == 'Children' :
        colors.append('red')
    elif row['genre'] == 'Documentaries' :
        colors.append('blue')
    elif row['genre'] == 'Stand-Up' :
        colors.append('green')
    else:
        colors.append('black')

# Print the first 10 items of the colors list
print(colors[0:10])

# Set the plotting style and create a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot with color-coded points based on genre
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'], c = colors)

# Add axis labels and a title
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie duration by year of release')

# Display the plot
plt.show()
