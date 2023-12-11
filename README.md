# sqlalchemy-challenge

This challenge involved doing a climate analysis for the Honolulu, HI area, utilizing Python and SQLAlchemy, in order to plan a vacation. The data was obtained from the _Journal of Atmospheric and Oceanic Technology_'s article entitled "An Overview of the Global Historical Climatology Network-Daily Database." Data on temperature and precipitation were explored over a 1-yr. time period. After completing the analysis, a Flask API was designed, which returned JSON's of the temperature and precipiation data using the jsonify function.

After connecting to the SQLite database and linking Python to the database using SQLAlchemy, various queries were run in order to conduct the analysis. Pandas was used to plot the data. The query results were then used to create a Flask API which allow the user to get temperature and precipitation data for different times of the year aiding the user in planning a vacation.

In addition to using the resources and documentation from the class that we were provided, I attended office hours and contacted AskBCS Learning Assistant to resolve issues with my Flask API that were causing errors. I checked Stack Overflow to also resolve errors and suggestions for modifying my code. This website was also helpful in getting more information on Flask documentation: [
](https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify)https://flask.palletsprojects.com/en/1.1.x/api/#flask.json.jsonify

