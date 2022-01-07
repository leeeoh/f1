# Project to perform adhoc analysis using Python

# dim_constructor
season_year, constructor_id, constructor_name, chassis, power_unit

# dim_driver
driver_id, driver_name, driver_number, birthday_date, age, country, start_date, f1_experience_days

# dim_roster
team_id, driver_id, start_date, end_date

# dim_track
track_id, track_name, country, continent, elevation_m, turn_count, test_lap_time_ms, distance_m, humidity

# race_calendar
season_year, race_id, track_id, race_date, lap_count, night_flag

# results_qualifying
season_year, race_id, driver_id, position_number, fastest_lap_time_ms

# results_race
season_year, track_id, driver_id, position_number, fastest_lap_flag, nts_earned

# results_championship_driver
season_year, driver_id, points_total, wins_count, podiums_count

# results_championship_constructor
season_year, constructor_id, points_total, wins_count, podiums_count