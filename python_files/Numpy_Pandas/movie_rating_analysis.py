import pandas as pd
import numpy as np

# ensure reproducibility

np.random.seed(42)

# ---users table
users=pd.DataFrame({
    'UserID':range(1,8),
    'Name':['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Age':[25, 30, 22, 35, 28, 40, 19],
    'City':['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Delhi', 'Mumbai']
})

# --- Movies table
movies = pd.DataFrame({
    'MovieID': range(101, 107),
    'Title': ['Inception', 'Titanic', 'Avengers', 'Joker', 'Interstellar', 'Coco'],
    'Genre': ['Sci-Fi', 'Romance', 'Action', 'Drama', 'Sci-Fi', 'Animation'],
    'Price': [250, 200, 300, 150, 250, 100]
})

ratings=pd.DataFrame({
    'RatingID':range(1001,1016),
    'UserID':np.random.choice(users['UserID'],15),
    'MovieID':np.random.choice(movies['MovieID'],15),
    'Rating':np.random.randint(1,6,15),
    'WatchDate':pd.date_range(start='2025-01-01',periods=15,freq='10D')
})

# Display generated tables
print("Users Table:\n", users)
print("\nMovies Table:\n", movies)
print("\nRatings Table:\n", ratings)


# merge ratings + users

rating_users=pd.merge(ratings,users,on='UserID',how='left')
print(rating_users)

ratings_full=pd.merge(rating_users,movies,on='MovieID',how='left')
print(ratings_full)

ratings_full['Revenue']=ratings_full['Price']

# Preview full dataset
print("\nFull Ratings Dataset:\n", ratings_full)


# Top movies by average rating

top_movies=ratings_full.groupby('Title')['Rating'].mean().sort_values(ascending=False)
print(f'TOP MOVIES:\n{top_movies}')

# Top users by revenue

top_users=ratings_full.groupby('Name')['Revenue'].sum().sort_values(ascending=False)
print(f'TOP USERS BY REVENUE:\n{top_users}')

# Avg rating genre x city

pivot_genre_city=pd.pivot_table(
    ratings_full,
    values='Rating',
    index='Genre',
    columns='City',
    aggfunc='mean',
    fill_value=0
)

print(pivot_genre_city)

# monthly watch and revenue trends

# ensure watch date in datetime

ratings_full['WatchDate']=pd.to_datetime(ratings_full['WatchDate'])

ratings_ts=ratings_full.set_index('WatchDate')

monthly_revenue=ratings_ts['Revenue'].resample('M').sum()

print(monthly_revenue)

monthly_watches=ratings_ts['Rating'].resample('M').count()
print(monthly_watches)


# super fan

user_watch_count=ratings_full.groupby('Name')['Rating'].count()

ratings_full['SuperFan']=ratings_full['Name'].map(lambda x:'Yes' if user_watch_count[x]>=3 else 'No')

print("\nRatings with Superfan Flag:\n", ratings_full[['Name','Title','Rating','SuperFan']])