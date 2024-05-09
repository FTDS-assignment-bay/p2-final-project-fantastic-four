import pickle
import streamlit as st
import requests


def recommend(city):
    index = cities[cities['city'] == city].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_accommodations = []
    for i in distances[1:6]:
        # fetch the accommodation details
        accommodation_details = fetch_accommodation_details(i[0])
        recommended_accommodations.append(accommodation_details)

    return recommended_accommodations


st.header('Airbnb Accommodation Recommender System Using Machine Learning')
cities = pickle.load(open('/listings_clustered.csv','rb'))
similarity = pickle.load(open('/rec_sys.pkl','rb'))

city_list = cities['city'].values
selected_city = st.selectbox(
    "Type or select a city from the dropdown",
    city_list
)

if st.button('Show Recommendation'):
    recommended_accommodations = recommend(selected_city)
    for accommodation in recommended_accommodations:
        st.text("Accommodation Description: " + accommodation['description'])
        st.text("Accommodation City: " + accommodation['city'])
        st.text("Accommodates: " + str(accommodation['accommodates']))
        st.text("Number of Reviews: " + str(accommodation['number_of_reviews']))
        st.text("Bedrooms: " + str(accommodation['bedrooms']))
        st.text("Beds: " + str(accommodation['beds']))
        st.text("Price: " + str(accommodation['price']))
        st.text("Review Scores Rating: " + str(accommodation['review_scores_rating']))
        st.text("Bathrooms: " + str(accommodation['bathrooms']))
