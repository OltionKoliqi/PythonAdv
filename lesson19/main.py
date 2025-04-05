import pandas as pd

from lesson18.lesson18 import total_books, unique_titles

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_Genre
    }
    books_df = pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success("New Book Added Successfully!")

st.sidebar.header('Filter Options')
selected_author = st.sidebar.selectbox("Select Author", ['All'] +list(books_df['Author'].unique()))
selected_Year = st.sidebar.selectbox("Select Year", ['All'] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ['All'] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider("Maximum Price", 0, books_df['Price'].max(), books_df['Price'].max())

filtered_Book_df = books_df.copy()

if selected_author != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Author'] == selected_author]
if selected_Year != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Year'] == selected_Year]
if selected_genre != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Genre'] == selected_genre]

filtered_Book_df = filtered_Book_df[( filtered_Book_df['User Rating'] >= min_rating) & filtered_Book_df['Price'] <= max_price]

st.subheader("Summary Statustics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

























