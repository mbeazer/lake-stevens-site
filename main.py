from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    # max_temp_list = []
    # min_temp_list = []
    # avg_temp_list = []
    #
    # weather = open("ls-weather.json")
    # weather_json = weather.read()
    # weather_data = json.loads(weather_json)
    #
    # this_month = datetime.now().strftime('%m')
    # this_day = datetime.now().strftime('%d')
    #
    # for data in weather_data:
    #     date = data['dt_iso'].split("+")[0].strip()
    #     month = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%m')
    #     day = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d')
    #
    #     if month == this_month and day == this_day:
    #         max_temp_list.append(data['main']['temp_max'])
    #         min_temp_list.append(data['main']['temp_min'])
    #         avg_temp_list.append(data['main']['temp'])
    #
    # high_temp = max(max_temp_list)
    # low_temp = min(min_temp_list)
    # avg_temp = "{:.1f}".format(sum(avg_temp_list) / len(avg_temp_list))
    #
    # for data in weather_data:
    #     date = data['dt_iso'].split("+")[0].strip()
    #     month = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%m')
    #     day = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d')
    #
    #     if month == this_month and day == this_day and data['main']['temp_max'] == high_temp:
    #         high_year = data['dt_iso'].split("+")[0].strip()
    #         high_year = datetime.strptime(high_year, '%Y-%m-%d %H:%M:%S').strftime('%y')
    #
    #     if month == this_month and day == this_day and data['main']['temp_min'] == low_temp:
    #         low_year = data['dt_iso'].split("+")[0].strip()
    #         low_year = datetime.strptime(low_year, '%Y-%m-%d %H:%M:%S').strftime('%y')
    #
    # # print(f"High temp: {high_temp} F in '{high_year}")
    # # print(f"Low temp: {low_temp} F in '{low_year}")
    # # print(f"Avg temp: {avg_temp} F")
    #
    # weather.close()

    # TESTING
    high_temp = "90"
    low_temp = "34"
    avg_temp = "67"
    high_year = "94"
    low_year = "20"

    return render_template("index.html", high_temp=high_temp, low_temp=low_temp, avg_temp=avg_temp, high_year=high_year, low_year=low_year)


if __name__ == "__main__":
    app.run(debug=True)
