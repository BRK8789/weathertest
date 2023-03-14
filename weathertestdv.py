import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
logo = Image.open('swrnlogo.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="Weather Dataset  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
st.title("Weather Dataset EDA")
# File upload
uploaded_file = st.file_uploader("Choose a Weather Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
# Define the list of names
names = ["K.NEERAJA", "K.AMRUTHA", "K.VAMSI","B.SAI RAM","T.MUKESH","A.HEMANTH","CH.KALYAN"]

# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
st.title("Weather Data Analysis")
# Define the analysis questions to be answered
analysis_questions = {
    "1. Find all the unique 'Wind Speed' values in the data.": "wind_speed_unique",
    "2. Find the number of times when the 'Weather is exactly Clear'.": "weather_clear_count",
    "3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.": "wind_speed_4_count",
    "4. Find out all the Null Values in the data.": "null_values",
    "5. Rename the column name 'Weather' of the dataframe to 'Weather Condition'.": "rename_column",
    "6. What is the mean 'Visibility'?": "mean_visibility",
    "7. What is the Standard Deviation of 'Pressure' in this data?": "std_pressure",
    "8. What is the Variance of 'Relative Humidity' in this data?": "var_relative_humidity",
    "9. Find all instances when 'Snow' was recorded.": "snow_recorded",
    "10. Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.": "wind_speed_24_visibility_25",
    "11. What is the Mean value of each column against each 'Weather Condition'?": "mean_by_weather_condition",
    "12. What is the Minimum & Maximum value of each column against each 'Weather Condition'?": "min_max_by_weather_condition",
    "13. Show all the Records where Weather Condition is Fog.": "weather_condition_fog",
    "14. Find all instances when 'Weather is Clear' or 'Visibility is above 40'.": "weather_clear_visibility_40",
    "15. Find all instances when 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'.": "weather_clear_rh50_visibility_40"
}

# Define a function to answer each analysis question
def answer_analysis_question(question_key):
    if analysis_questions[question_key] == "wind_speed_unique":
        unique_wind_speeds = data["Wind Speed_km/h"].unique()
        st.write(f"All the unique 'Wind Speed' values in the data are: {unique_wind_speeds}")
        st.dataframe(unique_wind_speeds)
    elif analysis_questions[question_key] == "weather_clear_count":
        clear_weather_count = (data["Weather"] == "Clear").sum()
        st.write(f"The number of times when the 'Weather is exactly Clear' is {clear_weather_count}")
    elif analysis_questions[question_key] == "wind_speed_4_count":
        wind_speed_4_count = (data["Wind Speed_km/h"] == 4).sum()
        st.write(f"The number of times when the 'Wind Speed was exactly 4 km/h' is {wind_speed_4_count}")
    elif analysis_questions[question_key] == "null_values":
        null_values = data.isnull().sum().sum()
        st.write(f"The number of Null Values in the data is {null_values}")
    elif analysis_questions[question_key] == "rename_column":
        data.rename(columns={"Weather": "Weather Condition"}, inplace=True)
        st.write(f"The column name 'Weather' of the dataframe has been renamed to 'Weather Condition'.")
    elif analysis_questions[question_key] == "mean_visibility":
        mean_visibility =data["Visibility_km"].mean()
        st.write(f"The mean 'Visibility' is {mean_visibility}")
    elif analysis_questions[question_key] == "std_pressure":
        std_pressure = data["Press_kPa"].std()
        st.write(f"The Standard Deviation of 'Pressure' in this data is {std_pressure}")
    elif analysis_questions[question_key] == "var_relative_humidity":
        var_relative_humidity = data["Rel Hum_%"].var()
        st.write(f"The Variance of 'Relative Humidity' in this data is {var_relative_humidity}")
    elif analysis_questions[question_key] == "snow_recorded":
        snow_recorded = data[data["Weather"].str.contains("Snow")]
        st.write(f"All instances when 'Snow' was recorded are:\n ")
        st.dataframe(snow_recorded)
    elif analysis_questions[question_key] == "wind_speed_24_visibility_25":
        wind_speed_24_visibility_25 = data[(data["Wind Speed_km/h"] > 24) & (data["Visibility_km"] == 25)]
        st.write(f"All instances when 'Wind Speed is above 24' and 'Visibility is 25' are:\n")
        st.dataframe(wind_speed_24_visibility_25)
    elif analysis_questions[question_key] == "mean_by_weather_condition":
        mean_by_weather_condition = data.groupby("Weather").mean()
        st.write(f"The Mean value of each column against each 'Weather' is:\n")
        st.dataframe(mean_by_weather_condition)
    elif analysis_questions[question_key] == "min_max_by_weather_condition":
        min_max_by_weather_condition = data.groupby("Weather").agg(["min", "max"])
        st.write(f"The Minimum & Maximum value of each column against each 'Weather' is:\n")
        st.dataframe(min_max_by_weather_condition)
    elif analysis_questions[question_key] == "weather_condition_fog":
        weather_condition_fog = data[data["Weather"] == "Fog"]
        st.write(f"All the Records where Weather Condition is Fog are:\n")
        st.dataframe(weather_condition_fog)
    elif analysis_questions[question_key] == "weather_clear_visibility_40":
        weather_clear_visibility_40 = data[(data["Weather"] == "Clear") | (data["Visibility_km"] > 40)]
        st.write(f"All instances when 'Weather is Clear' or 'Visibility is above 40' are:\n")
        st.dataframe(weather_clear_visibility_40)
    elif analysis_questions[question_key] == "weather_clear_rh50_visibility_40":
        weather_clear_rh50_visibility_40 = data[(data["Weather"] == "Clear") & (data["Rel Hum_%"] > 50) | (data["Visibility_km"] > 40)]
        st.write(f"All instances when 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40' are:\n")
        st.dataframe(weather_clear_rh50_visibility_40)
def main():
    st.title("Weather Data Analysis App")
    st.sidebar.title("Project Team Members:")
    st.sidebar.title("Under the Guidance Of:")
    st.sidebar.title("Dr.Bomma.Ramakrishna")
    st.sidebar.title("Select Analysis Question")
# Display the analysis question options in the sidebar
analysis_question_options = list(analysis_questions.keys())
selected_analysis_question = st.sidebar.selectbox("Select Analysis Question", analysis_question_options)

# Call the answer_analysis_question function for the selected analysis question
answer_analysis_question(selected_analysis_question)
#What is the distribution of temperatures in the dataset?
# Data visualization question
st.write("## Distribution of Temperatures")
# Create histogram of temperatures
fig, ax = plt.subplots()
sns.histplot(data=data, x="Temp_C", ax=ax)
ax.set_xlabel("Temperature (Celsius)")
ax.set_ylabel("Count")
# Display histogram
st.pyplot(fig)
#Is there a relationship between temperature and visibility?
# Data visualization question
st.write("## Relationship between Temperature and Visibility")
# Create scatterplot of temperature and visibility
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="Temp_C", y="Visibility_km", ax=ax)
ax.set_xlabel("Temperature (Celsius)")
ax.set_ylabel("Visibility (km)")
# Display scatterplot
st.pyplot(fig)
#What is the average temperature by month?
# Data visualization question
st.write("## Average Temperature by Month")
# Convert date column to datetime
data["Date/Time"] = pd.to_datetime(data["Date/Time"])
# Create new column for month
data["Month"] = data["Date/Time"].dt.month
# Calculate mean temperature by month
mean_temp_by_month = data.groupby("Month")["Temp_C"].mean()
# Create bar chart of mean temperature by month
fig, ax = plt.subplots()
mean_temp_by_month.plot(kind="bar", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Mean Temperature (Celsius)")
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=0)
# Display bar chart
st.pyplot(fig)
#What is the average pressure by weather condition?
# Data visualization question
st.write("## Average Pressure by Weather Condition")
# Calculate mean pressure by weather condition
mean_pressure_by_condition = data.groupby("Weather").agg({"Press_kPa": "mean"})
# Rename columns
mean_pressure_by_condition.columns = ["Mean Pressure (kPa)"]
# Sort by mean pressure
mean_pressure_by_condition = mean_pressure_by_condition.sort_values(by="Mean Pressure (kPa)", ascending=False)
# Create bar chart of mean pressure by weather condition
fig, ax = plt.subplots()
mean_pressure_by_condition.plot(kind="bar", ax=ax)
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Mean Pressure (kPa)")
ax.set_xticklabels(mean_pressure_by_condition.index, rotation=90)
# Display bar chart
st.pyplot(fig)

