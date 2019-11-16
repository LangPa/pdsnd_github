import analysis_tools as a

          
          
def main():
    while True:
        city, month, day = a.get_filters()
        df = a.load_data(city, month, day)

        a.time_stats(df)
        a.station_stats(df)
        a.trip_duration_stats(df)
        a.user_stats(df)
        a.raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
