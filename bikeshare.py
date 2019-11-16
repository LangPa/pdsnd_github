import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Please specify')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('City: ').lower()
        
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('City must be either Chicago, New York city or Washington')

    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Month: ').lower()
        
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('Month must be from January to June. For all months enter "all".')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Day: ').lower()
        
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print('Please enter a day of the week. For all days enter "all"')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month_index = df['month'].mode()[0]
    popular_month = ['january', 'february', 'march', 'april', 'may', 'june'][popular_month_index - 1]
    print(f'The most popular month was {popular_month}')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f'The most popular day was {popular_day}')


    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'The most common hour of travel was {popular_hour}')


        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is {popular_start_station}.')
    

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end stations is {popular_end_station}.')

    # TO DO: display most frequent combination of start station and end station trip
    df['Journey'] = df['Start Station'] + ' to ' + df['End Station']
    popular_journey = df['Journey'].mode()[0]
    print(f'The most common journey is {popular_journey}.')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(f'The total travel time was {total_time} seconds')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f'The mean travel time was {mean_time} seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types, '\n')


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count, '\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])

        print(f'The oldest traveller was born in {earliest}, the youngest in {most_recent} and the majority of traveller were born in {most_common}.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
          """Displays chunks of the raw data"""
          i = 0
          
          while True:
            
            if input('\n Enter "y" to display 5 lines of raw data, otherwise press enter key to continue: ') == 'y':
                print('\n', df.iloc[i: i+5])
                i += 5
                
            else:
                break
          
          
          
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
