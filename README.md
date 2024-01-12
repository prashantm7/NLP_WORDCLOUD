Movie and Product Reviews Analysis
1. Amazon Product Reviews Analysis
Data Extraction
To extract reviews for a Google Pixel product on Amazon, the script utilizes web scraping techniques. It retrieves reviews from multiple pages, and the extracted data is stored in a text file named "Googlepixel.txt."

Preprocessing
The reviews are processed to remove unwanted symbols, numbers, and common stopwords. The resulting text is used to generate a WordCloud, providing a visual representation of frequently occurring words.


2. IMDB Movie Reviews Analysis
Data Extraction
For the IMDB movie reviews, the script collects reviews for a specific movie and stores them in a text file named "movie_review.txt."

Preprocessing
Similar to the product reviews analysis, the movie reviews undergo preprocessing to remove unwanted symbols, numbers, and stopwords. The processed text is then used to create a WordCloud.


Sentiment Analysis
Both analyses involve sentiment analysis, where the overall sentiment of the reviews is determined. The sentiment analysis is based on the content of the reviews, providing insights into the opinions and feedback from users.

Unigram and Bigram Word Cloud
In addition to the overall sentiment analysis, the script generates unigram and bigram WordClouds for better visualization of frequently occurring words and phrases in the reviews.

Unigram WordCloud

Bigram WordCloud

Note: Please replace "insert_path_to_image" with the actual paths to the generated WordCloud images.

This script provides a comprehensive analysis of reviews, helping to understand user sentiments and identify key themes in the feedback for both products and movies.
