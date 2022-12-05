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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=['chicago','new york city','washington']
        city=input('\n Please enter the name of the city you want to analyse (Chicago,New York City,Washington)\n').lower()
        if city in cities:
            break
        else:
            print("City data not found! Please enter a valid city name.")


    # get user input for month (all, january, february, ... , june)
    while True:
        months=['January','February','March','April','May','June','All']
        month=input("\n Please enter the month for which you want to see the data (January,February,March,April,May,June).\n Type 'All' if you don't want to put a month filter \n").title()
        if month in months:
            break
        else:
            print('Data for the month not found! Please enter a valid month')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
        day=input("Please enter the day of the week for which you want to see the data.\n Type 'All' if you don't want to put a day filter.\n").title()
        if day in days:
            break
        else:
            print('Please enter a valid day of the week.')


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
    #load data file into the dataframe
    df=pd.read_csv(CITY_DATA[city])
    #convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #extracting the month and the day of the week from start time and creating a new column
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    #filtering by month if applicable
    if month!='All':
        months=['January','February','March','April','May','June']
    #using the index of the month to get the corresponding input
        month=months.index(month)+1
        #filtering by month to create a new DataFrame
        df=df[df['month']==month]
    #filtering by day of the week if applicable
    if day!='All':
        #filtering by day of the week to create a new dataframe
        df=df[df['day_of_week']==day]
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month
    if month=='All':
        popular_month=df['month'].mode()[0]
        months=['January','February','March','April','May','June']
        popular_month=months[popular_month-1]
        print('{} is the most popular month.'.format(popular_month))



    # displaying the most common day of week
    if day=='All':
        popular_day=df['day_of_week'].mode()[0]
        print('{} is the most popular day of the week.'.format(popular_day))


    # displaying the most common start hour
    df['Start Hour']=df['Start Time'].dt.hour
    popular_hour=df['Start Hour'].mode()[0]
    print('{}:00 hrs is the popular hour.'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('{} is the most popular start station'.format(popular_start_station))


    # displaying most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('{} is the most popular end station'.format(popular_end_station))

    # displaying most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    popular_combination=df['combination'].mode()[0]
    print('{} is the most popular combination of start and end station'.format(popular_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print('{} hour(s) {} minute(s) {} second(s) is the total trip duration.'.format(hour,minute,second))



    # display mean travel time
    avg_duration=round(df['Trip Duration'].mean())
    min,sec=divmod(avg_duration,60)
    hr,min=divmod(min,60)
    if min>60:
        print('{} hour(s) {} minute(s) {} second(s) is the mean travel time.'.format(hr,min,sec))
    else:
        print('{} minute(s) {} second(s) is the mean travel time.'.format(min,sec))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count=df['User Type'].value_counts()
    print('The user types are:\n',user_count)


    # Display counts of gender
    if city.title()=='Chicago' or city.title()=='New York City':
        gender_count=df['Gender'].value_counts()
        print("\n The count for the gender found are:\n",gender_count)


    # Display earliest, most recent, and most common year of birth
        oldest_user=int(df['Birth Year'].min())
        print("\n The oldest user is born in the year of ",oldest_user)
        youngest_user=int(df['Birth Year'].max())
        print('\n The youngest user is born in the year of ',youngest_user)
        common_year=int(df['Birth Year'].mode()[0])
        print('\n Most of the users are born in the year of ',common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    response=['yes', 'no']
    while True:
        choice=input("Would you like to view some individual trip data(5 entries) ?\n Please type 'yes'or 'no'\n").lower()
        if choice in response:
            if choice=='yes':
                start=0
                end=5
                data=df.iloc[start:end,:9]
                print(data)
                while True:
                    choice_new=input("Would you like to view more trip data?\n Please type 'yes'or 'no'\n").lower()
                    if choice_new in response:
                        if choice_new=='yes':
                            start+=5
                            end+=5
                            data=df.iloc[start:end,:9]
                            print(data)
                        else:
                            break
                break
            else:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
