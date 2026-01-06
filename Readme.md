Movie Recommender System
A content-based movie recommender system built with Python, Pandas, and Scikit-learn. The application is served as an interactive web app using Streamlit.

🎬 Features
Content-Based Filtering: Recommends movies based on similarity of genres, keywords, cast, and crew.
Interactive UI: A simple and clean web interface built with Streamlit to select a movie and get recommendations.
Fetches Movie Posters: Dynamically fetches and displays movie posters using the TMDB API.
Data Preprocessing: Includes a script for processing and cleaning the raw TMDB 5000 movie dataset.
⚙️ How It Works
The recommendation engine is built using the following steps:

Data Loading & Merging: The TMDB 5000 Movies and Credits datasets are loaded and merged into a single dataframe.
Feature Selection: Key features like genres, keywords, overview, cast, and crew (specifically the director) are selected.
Data Cleaning & Preprocessing: Missing data is handled, and the text-based JSON columns are parsed to extract relevant information (e.g., genre names, actor names).
Feature Engineering: A unified tags column is created by combining all the selected features into a single text block for each movie.
Text Vectorization: The tags are converted into a numerical vector space using the CountVectorizer (Bag of Words model). This process ignores common English stop words.
Similarity Calculation: The cosine similarity is calculated between all movie vectors to determine how similar they are to each other.
Recommendation: When a user selects a movie, the system finds the most similar movies based on the pre-calculated cosine similarity scores and returns the top 5 matches.
🛠️ Technologies Used
Python: Core programming language.
Pandas: For data manipulation and analysis.
NumPy: For numerical operations.
Scikit-learn: For CountVectorizer and cosine_similarity.
NLTK: For stemming text to normalize words.
Streamlit: To create the interactive web application.
Pickle: For saving and loading the trained model (dataframes and similarity matrix).
Requests: For making API calls to TMDB.
🚀 Setup and Usage
To run this project locally, follow these steps:

1. Prerequisites
Python 3.8 or higher
pip
2. Clone the Repository
git clone https://github.com/your-username/Movie-Recommender-System-main.git
cd Movie-Recommender-System-main
3. Install Dependencies
It is recommended to use a virtual environment.

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
4. Get the Data
The project uses the TMDB 5000 Movie Dataset. Download the following files and place them in the root directory of the project:

tmdb_5000_movies.csv
tmdb_5000_credits.csv
5. Preprocess the Data
Run the Jupyter Notebook or the Python script to process the data and generate the necessary pickle files. This will create movies.pkl and similarity.pkl.

python movie_recommender_system.py
Note: The app.py file is configured to download pre-compiled pickle files, so this step is only necessary if you want to regenerate them from scratch.

6. Run the Streamlit App
Once the dependencies are installed and the pickle files are present, run the Streamlit application:

streamlit run app.py
Your web browser will open with the application running at http://localhost:8501.

7. How to Use the App
Open the web application in your browser.
Select a movie from the dropdown menu.
Click the "Recommend" button.
The app will display the top 5 recommended movies along with their posters.
📁 File Structure
.
├── app.py                      # The Streamlit web application script
├── movie_recommender_system.py   # Python script for data processing and model building
├── Movie_Recommender_System.ipynb # Jupyter Notebook with the detailed analysis
├── movies.pkl                  # Pickled dataframe of movies
├── similarity.pkl                # Pickled cosine similarity matrix
├── tmdb_5000_credits.csv         # Raw data file
├── tmdb_5000_movies.csv          # Raw data file
├── requirements.txt              # List of Python dependencies
└── README.md                     # This file
