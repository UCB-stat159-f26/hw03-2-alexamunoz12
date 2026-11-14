# HW3

## Assignment

This assignment builds on HW1 and HW2 where I worked with Serena Williams's career match data. For this homework, I created a Python package that can download and clean career match data for different tennis players from Tennis Abstract. The package also creates a scatter plot similar to the one from HW2. The x-axis shows the player's age and the y-axis shows the age difference between the player and their opponent. 

## How to install

To install the package from GitHub, run:

```bash
pip install git+https://github.com/alexamunoz12/hw03-2-alexamunoz12.git
```

## How to Use

The package has two main functions:

- `get_player_data()` downloads and cleans a player's career match data.
- `plot_player_career()` creates a scatter plot using the cleaned data.


## Testing

I used `pytest` to test the data cleaning functions with sample JavaScript data instead of downloading data from the website during testing.

To run the tests:

```bash
python -m pytest tests/ -v
```

## Reflections

In this assignment, I learned how to turn my HW2 code into a Python package that other people can install and use. Something that was pretty challenging was making the code work for different players instead of just Serena Williams. I ran into many errors when downloading and processing the data but working through them helped me understand how to debug my functions. Also i had done test cases before but i feel like this was a better learning experience for learning how to do test cases.
