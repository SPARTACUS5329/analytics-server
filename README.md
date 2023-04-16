# analytics-server


## Installation instructions

``` 
git clone https://github.com/SPARTACUS5329/analytics-server.git
pip install -r requirements.txt 
uvicorn app:app --reload
```

Download the FMP folder from the datasets given

## Implemented Algorithms:

1. Sentient analysis to go through the transcripts of each company
    - We have used pre-trained nlp libraries to extract the keywords from the transcripts.
    - These key words are then fed to a hugging face model which gives output in the form of a positive or negative label and a corresponding rating
    - Since we cant feed a large set to hugging face, we have broken down the paragraphs into smaller phrases.
    - We get a net negative and positive rating for each year of each companies transcripts
    - A common trend we noticed was, the result of all the transcripts was quite positive. So we came up with an algorithm to give a final negative positive rating to each company.
        - We Normalised these final rating values so that the mean = 0 and variance of these values = 0 
        -  Final Rating = A * positive<sub>i</sub> + B * negative<sub>i</sub>
        - Upon using external computation units we used all the datasets to get ratings and then using these obtained values we got values:<br/>
                <b>A: 0.0026223464946062386<br/>
                B: -0.017333561945556908</b>
        - These values ensure a normal distribution for the <b> Final Rating</b>

2. Stock Analysis  
	- We used the following metrics to asses stocks
		- RSI value
		- P/B value
		- P/E value
		- Forware P/E value
		
3. Prediction reccomendation based on past data using LSTM networks, trained on past data
