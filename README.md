# News Research Tool 📈

This tool allows you to research news articles by providing URLs, processing the content, and answering your questions based on the article's information. The tool leverages **Ollama** (a local large language model) and **FAISS** (a similarity search engine) to efficiently index, retrieve, and answer queries related to stock market and financial news.

![New research tool](https://github.com/user-attachments/assets/3770d861-02f5-442b-8987-33beb1057bf1)


## Key Features:
- **Load News Articles**: Input up to 3 article URLs and process their content.
- **Text Processing & Chunking**: Splits article text into smaller chunks to handle larger documents.
- **Local Model Integration**: Uses **Ollama** to process and generate insights based on the content.
- **Embedding & Indexing**: Generates embeddings for article text and stores them in a **FAISS** vectorstore for fast retrieval.
- **Answer Queries**: Ask questions about the content, and get accurate answers along with the source URLs.

## How It Works:

### 1. Input URLs:
Users can enter up to three news article URLs in the sidebar of the app.

### 2. Process Data:
Once the "Process URLs" button is clicked:
- **UnstructuredURLLoader** loads the article content.
- The text is split into smaller chunks using **RecursiveCharacterTextSplitter**.
- Embeddings are generated using **HuggingFaceEmbeddings** and stored in a **FAISS** vectorstore.

### 3. Save & Load Embeddings:
The generated embeddings and vectorstore are saved to a local file (`faiss_store_ollama.pkl`). This allows the tool to efficiently search the content without reprocessing the articles each time.

### 4. Ask Questions:
- Users can enter a question related to the news articles in the "Question" input field.
- The tool will retrieve the most relevant answers using the **RetrievalQA** chain, based on the indexed articles.
- The results will be displayed along with the sources from where the information was retrieved.

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/anamipatel81/News-Research_Tool.git
   cd News-Research-Tool
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run main.py
2.The web app will open in your browser.

- On the sidebar, you can input URLs directly.
- Initiate the data loading and processing by clicking "Process URLs."
- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.
- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.
- The FAISS index will be saved in a local file path in pickle format for future use.
- One can now ask a question and get the answer based on those news articles
- In video tutorial, we used following news articles
   
