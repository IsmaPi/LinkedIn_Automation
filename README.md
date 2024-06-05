# 📰 Tech News Scraper & LinkedIn Post Generator

Welcome to the **Tech News Scraper & LinkedIn Post Generator** repository! This project is designed to scrape the web for the latest tech news, convert the extracted text into LinkedIn post format, and provide informative summaries for social media engagement.

![GitHub last commit](https://img.shields.io/github/last-commit/IsmaPi/LinkedIn_Automation)
![GitHub issues](https://img.shields.io/github/issues/IsmaPi/LinkedIn_Automation)
![GitHub pull requests](https://img.shields.io/github/issues-pr/IsmaPi/LinkedIn_Automation)
![GitHub license](https://img.shields.io/github/license/IsmaPi/LinkedIn_Automation)

## 🌟 Key Features

- **Web Scraping**: Utilizes Selenium and BeautifulSoup to scrape tech news articles from various sources.
- **Text Processing**: Cleans and processes the scraped text to remove unwanted characters and format it for readability.
- **LinkedIn Post Generation**: Uses OpenAI API to generate LinkedIn posts from the processed text, ensuring high engagement and relevance.

## 🚀 How to Get Started

### Prerequisites

- Python 3.x
- Chrome WebDriver
- Flask
- BeautifulSoup
- Selenium
- OpenAI API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/tech-news-scraper.git](https://github.com/IsmaPi/LinkedIn_Automation/)
   cd LinkedIn_Automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

### Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Send a POST request to `/run_main` with a JSON payload containing the link:**
   ```json
   {
     "link": "https://example.com/tech-news-article"
   }
   ```

## 📚 Example Use-Case

Here's an example of how you can use this project to scrape a tech news article and generate a LinkedIn post:

1. **Send a POST request to the Flask server:**
   ```bash
   curl -X POST http://127.0.0.1:5000/run_main -H "Content-Type: application/json" -d '{"link": "https://example.com/tech-news-article"}'
   ```

2. **Receive the generated LinkedIn post in the response:**
   ```json
   {
     "post": "..."
   }
   ```

## 📖 Documentation

For more detailed information on how to use this project, please refer to the [documentation](docs/documentation.md) _coming soon_.

## 🤝 Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for checking out our project! If you have any questions or feedback, feel free to open an issue or contact us directly. Happy coding! 🚀
