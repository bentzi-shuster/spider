# IS 392 Job Spider

## URL Dataset

`https://www.kaggle.com/datasets/peopledatalabssf/free-7-million-company-dataset`

- The above dataset is a collection of 7 million companies and their details.
- This dataset was chosen because it is a large URL dataset without any dangerous or mature content.
- The dataset is also free to use and download.

## Data Collection Plans

### 1. Retrieve job postings URLs from the dataset

Step 1. Open a URL from the dataset.
Step 2. Pull the HTML content from the URL and parse it (using BeautifulSoup or similar).
Step 3. Extract the job postings urls from the HTML content.

- This will be done by looking for specific keywords in the HTML content (e.g., "job", "career", "employment").

Step 4. Store the job postings URLs in a database or file for further processing.

### 2. Extract job postings data from the URLs

Step 1. Open a job posting URL.
Step 2. Pull the HTML content from the URL and parse it with Gemini or other LLM apis.
Step 3. Extract the X-Path of the job posting data from the HTML content.

- This is done so that the data can be extracted from the HTML content in a structured way in the future without having to use an LLM every time.

Step 4. Extract the job posting data from the HTML content using the X-Path.
Step 5. Store the job posting data in a database or file for further processing.

### 3. Analyze the job postings data

S