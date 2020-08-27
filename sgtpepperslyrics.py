from wordcloud import WordCloud, STOPWORDS # creates wordcloud
import matplotlib.pyplot as plt # displays wordcloud
import pandas as pd # reads csv
import numpy as np # to get the color of our image
from PIL import Image # loads image

# reads the comma seperated data
def read_csv():
    return pd.read_csv(r"sgtpeppers.csv")

def main():
    df = read_csv()

    # initialize the text
    lyric_words = ""

    # eliminates certain words
    stopwords = set(STOPWORDS)

    for val in df.songContent:
        # converts each val to a string
        val = str(val) 
  
        # split the value
        tokens = val.split() 
      
        # converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
      
        lyric_words += " ".join(tokens)+" "

    # gets color of the image
    custom_image = np.array(Image.open("cloud.png"))

    # creates wordcloud
    wordcloud = WordCloud(background_color ='white', 
                stopwords = stopwords, 
                mask = custom_image).generate(lyric_words)


    # displays the wordcloud
    plt.imshow(wordcloud, interpolation = 'bilinear') 
    plt.axis("off") 
    plt.tight_layout(pad = 0)   
    plt.show()

if __name__ == "__main__":
    main()