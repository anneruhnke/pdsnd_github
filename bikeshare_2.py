import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('You can explore data for Chicago, New York City or Washington. Please choose one city: ').lower()

    while city not in CITY_DATA:
        print('\nThis input is not valid.')
        print('Please enter your data again.\n')
        city = input('You can explore data for Chicago, New York City or Washington. Please choose one city: ').lower()

    # get user input for month (all, january, february, ... , june)
    month_example = [1,2,3,4,5,6,7]
    try:
        month = int(input('Which month do you want to choose? Type 1 for January, 2 for February, 3 for March, 4 for April, 5 for May, 6 for June and 7 for all months:'))
        month in month_example
        if month == 1:
            print('You chose January.')
        elif month == 2:
            print('You chose February.')
        elif month == 3:
            print('You chose March.')
        elif month == 4:
            print('You chose April.')
        elif month == 5:
            print('You chose May.')
        elif month == 6:
            print('You chose June.')
        elif month == 7:
            print('You chose all months.')
        else:
            print('\nYou entered unvalid data.')
            print('The program automatically chooses no filter for months.\n')
            month = 7
    except:
        print('\nThis input is not valid.')
        print('The program automatically chooses no filter for months.\n')
        month = 7

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_example = [0,1,2,3,4,5,6,7]
    try:
        day = int(input('Which day do you want to choose? Type 0 for Sunday, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday and 7 for all days:'))
        day in day_example
        if day == 0:
            print('You chose Sunday.')
        elif day == 1:
            print('You chose Monday.')
        elif day == 2:
            print('You chose Tuesday.')
        elif day == 3:
            print('You chose Wednesday.')
        elif day == 4:
            print('You chose Thursday.')
        elif day == 5:
            print('You chose Friday.')
        elif day == 6:
            print('You chose Saturday.')
        elif day == 7:
            print('You chose all days.')
        else:
            print('\nYou entered unvalid data.')
            print('The program automatically chooses no filter for days.\n')
            day = 7
    except:
        print('\nThis input is not valid.')
        print('The program automatically chooses no filter for days.\n')
        day = 7

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    dd = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    if month != 7:
        df = df[df['month'] == month]

    if day != 7:
        df = df[df['day'] == day]

    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month:', popular_month)

    # display the most common day of week
    popular_dow = df['day'].mode()[0]
    print('Most popular day of week:', popular_dow)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour: ', popular_hour)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    '''Displays statistics on the most popular stations and trip.'''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Popular Route'] = df['Start Station'] + ' - ' + df['End Station']
    popular_route = df['Popular Route'].mode()[0]
    print('Most popular route:', popular_route)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    '''Displays statistics on the total and average trip duration.'''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total trip duration:', total_trip_duration)

    # display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('Average trip duration:', average_trip_duration)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    '''Displays statistics on bikeshare users.'''

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User types:', '\n', user_type)
    print('\n')

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender:', '\n', gender)
        print('\n')

        # Display earliest, most recent, and most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year:', most_common_birth_year)

        birth_year_min = df['Birth Year'].min()
        print('The earliest birth year:', birth_year_min)

        birth_year_max = df['Birth Year'].max()
        print('The most recent birth year:', birth_year_max)
    except:
        print('Gender data is not available for this city.')

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        index=0
        while True:
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            if raw_data.lower() != 'no':
                print(df.iloc[(index):(index+5), 0:8])
                index+=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
	main()
