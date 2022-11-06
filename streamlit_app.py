from turtle import left
import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
import time
from datetime import date
from datetime import timedelta


API_KEY ="b3da6f17b06b43efffa122805fa60148"

st.set_page_config(page_title = "My webpage", layout = "wide")


st.title("First Project")


def convert_to_celcius(temp):
    return temp - 273.15

def find_current_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(convert_to_celcius( weather_data['main']['temp']))
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City not found")
        st.stop()
    return general, temperature, icon

col_1,col_2 = st.columns(2)
with col_1:
    st.header("Find the weather of the City you want")
    city = st.text_input("Enter city name:").lower()
    if st.button("Go!"):
        general , temperature, icon = find_current_weather(city)
        with st.container():
            st.metric(label = "Temperature",value = f"{temperature} {chr(176)}C")
            st.write(general)
            st.image(icon)
with col_2:
    st.header("Limassol Weather")
    general , temperature, icon = find_current_weather("Limassol")
    st.metric(label = "Temperature",value = f"{temperature} {chr(176)}C")
    st.write(general)
    st.image(icon)

def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts,60)
            time_now = '{:02d}:{:02d}'.format(mins,secs)
            st.header(time_now)
            time.sleep(1)
            ts -= 1
        st.write("Time up!")
col__1,col__2 = st.columns(2)
with col__1:
    st.header("Pomodoro Timer")
    time_in_minutes = st.number_input("Enter time in minutes:",min_value = 1, value = 25)
    time_in_seconds = time_in_minutes * 60
    if st.button("Start"):
        count_down(time_in_seconds)
with col__2:
    st.header("Colour to Hex Selector")

    colour = st.color_picker('Pick A Colour', '#8569a8')

    st.write('The colour you picked is', colour)

    
col___1,col___2 = st.columns(2)
with col___1:
    st.header('BMI Calculator')

    st.text("""
    BMI is a person’s weight in kilograms divided by the square of height in meters. 
    A high BMI can indicate high body fatness.
    If your BMI is less than 18.5, it falls within the underweight range.
    If your BMI is 18.5 to <25, it falls within the healthy weight range.
    If your BMI is 25.0 to <30, it falls within the overweight range.
    If your BMI is 30.0 or higher, it falls within the obesity range.
    Obesity is frequently subdivided into categories:
    Class 1: BMI of 30 to < 35
    Class 2: BMI of 35 to < 40
    Class 3: BMI of 40 or higher. 
    Class 3 obesity is sometimes categorized as “severe” obesity.
    Credits: https://www.cdc.gov/obesity/adult/defining.html
	    """)


    weight = st.number_input("Enter your Weight in KG", step = 0.1, value = 50.00)
    height = st.number_input("Enter your Height in Meters",value = 1.50)
    bmi = weight/(height)**2
    st.success(f"Your BMI is {bmi}")

with col___2:
    st.header("Αναφορά")
    st.text("""
    Για την υλοποίηση της σελίδας ξεκίνησα με το widget του καιρού.
    Ακολουθώντας το εξής βίντεο στο youtube:
    https://www.youtube.com/watch?v=CP3t5gVIm5o&ab_channel=MalayaliCode
    Χρησιμοποιώντας ένα API key παίρνουμε τα δεδομένα καιρού από την
    σελίδα openweathermap, με τις κατάλληλες τροποποιήσεις από τα δεδομένα
    που λαμβάνουμε εμφανίζουμε μόνο την θερμοκρασία, μια γενική περιγραφή 
    και το αντίστοιχο εικονίδιο που αντιπροσωπεύει τον καιρό.
    Το δεύτερο widget αντί να δέχεται πόλη παίρνει κατευθείαν τα δεδομένα 
    για την Λεμεσό.
    Το τρίτο widget είναι μια αντίστροφη μέτρηση, ο χρήστης δίνει τον χρόνο 
    σε λεπτά, εμείς τον μετατρέπουμε σε δευτερόλεπτα και με την συνάρτηση
    count_down ο χρόνος μειώνεται ανά δευτερόλεπτο μέχρι να μηδενιστεί και
    να εμφανίσει το κατάλληλο μήνυμα. Το βίντεο που ακολούθησα είναι το εξής: 
    https://www.youtube.com/watch?v=vjDtlfS10ic&t=1s&ab_channel=MalayaliCode
    Το τέταρτο widget δέχεται το βάρος και το ύψος ενός ατόμου και εμφανίζει 
    αν τον δείκτη BMI του συγκεκριμένου ατόμου για να δεί αν ειναι λιποβαρής,
    κανονικό ή υπέρβαρο, και αν είναι υπέρβαρο σε ποιά τάξη παχυσαρκίας ανήκει.
    https://github.com/ASR373/YT-BMI-APP/blob/main/app.py
    Το πέμπτο widget είναι ένα απλό color_picker που εμφανίζει το αντίστοιχο
    χρώμα σε δεκαεξαδικό αριθμό απλά τυπώνοντας την μεταβλητή colour μέσα στην 
    οποία αποθηκεύται το χρώμα που επιλέγουμε.
    Το έκτο widget το χρησιμοποίησα από την σελίδα 
    https://github.com/nikkisharma536/streamlit_app
    το οποίο χρησιμοποιεί τα δεδομένα του  covid.csv αρχείου και εμφανίζει 
    διάφορα στατιστικά στοιχεία σχετικά με τον covid19 για συγκεκριμένες 
    ημερομηνιές. Το πρώτο διάγραμμα εμφανίζει τα περιστατικά θανάτου για την
    Ελλάδα για τον μήνα Απρίλιο του 2020. Η δεύτερη γραφική δείχνει τα
    επιβεβαιωμένα κρούσματα για μία ή και περισσότερες χώρες που θα επιλέξει
    ο χρήστης. Και το τρίτο κομμάτι είναι ο παγκόσμιος χάρτης που εμφανίζει την
    εμβέλια σε κάθε χώρα διαφόρων μετρικών που σχετίζονται με τον covid19.

	    """)

DATA_URL = ('covid.csv')
@st.cache(allow_output_mutation=True)

def load_data():
    data = pd.read_csv(DATA_URL)
    data['date'] = pd.to_datetime(data['date'],format='%d/%m/%Y' ).dt.strftime('%Y-%m-%d')
    return data

# Load rows of data into the dataframe.
df = load_data()


# bar chart 
filter_data = df[(df['date'] >='2020-04-01') & (df['Country']== 'Greece')].set_index("date")

st.markdown( "Greece daily Death cases from 1st April 2020")

st.bar_chart(filter_data[['total_deaths']])

#   WIDGETS
subset_data = df

### MULTISELECT
country_name_input = st.multiselect(
'Country name',
df.groupby('Country').count().reset_index()['Country'].tolist())

# by country name
if len(country_name_input) > 0:
    subset_data = df[df['Country'].isin(country_name_input)]

st.subheader('Comparision of infection growth')

total_cases_graph  =alt.Chart(subset_data).transform_filter(
    alt.datum.total_cases > 0  
).mark_line().encode(
    x=alt.X('date', type='nominal', title='Date'),
    y=alt.Y('sum(total_cases):Q',  title='Confirmed cases'),
    color='Country',
    tooltip = 'sum(total_cases)',
).properties(
    width=1500,
    height=600
).configure_axis(
    labelFontSize=17,
    titleFontSize=20
)

st.altair_chart(total_cases_graph)


metrics =['total_cases','new_cases','total_deaths','new_deaths','total_cases_per_million','new_cases_per_million','total_deaths_per_million','new_deaths_per_million','total_tests','new_tests','total_tests_per_thousand','new_tests_per_thousand']

cols = st.selectbox('Covid metric to view', metrics)

# let's ask the user which column should be used as Index
if cols in metrics:   
    metric_to_show_in_covid_Layer = cols  

# Variable for date picker, default to Jan 1st 2020
date = date(2020,1,1)

# Set viewport for the deckgl map
view = pdk.ViewState(latitude=0, longitude=0, zoom=0.2,)

# Create the scatter plot layer
covidLayer = pdk.Layer(
        "ScatterplotLayer",
        data=df,
        pickable=False,
        opacity=0.3,
        stroked=True,
        filled=True,
        radius_scale=10,
        radius_min_pixels=5,
        radius_max_pixels=60,
        line_width_min_pixels=1,
        get_position=["Longitude", "Latitude"],
        get_radius=metric_to_show_in_covid_Layer,
        get_fill_color=[252, 136, 3],
        get_line_color=[255,0,0],
        tooltip="test test",
    )



# Create the deck.gl map
r = pdk.Deck(
    layers=[covidLayer],
    initial_view_state=view,
    map_style="mapbox://styles/mapbox/light-v10",
)


# Create a subheading to display current date
subheading = st.subheader("")

# Render the deck.gl map in the Streamlit app as a Pydeck chart 
map = st.pydeck_chart(r)

# Update the maps and the subheading each day for 90 days
for i in range(0, 120, 1):
    # Increment day by 1
    date += timedelta(days=1)

    # Update data in map layers
    covidLayer.data = df[df['date'] == date.isoformat()]

    # Update the deck.gl map
    r.update()

    # Render the map
    map.pydeck_chart(r)

    # Update the heading with current date
    subheading.subheader("%s on : %s" % (metric_to_show_in_covid_Layer, date.strftime("%B %d, %Y")))
    
    # wait 0.1 second before go onto next day
    time.sleep(0.05)









