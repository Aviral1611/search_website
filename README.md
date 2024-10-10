# EXA Search App

This is a Flask-based web application that allows users to search for keywords across multiple domains (like Reddit and StackOverflow) using the EXA API. The application includes features like dynamic search, customizable domain selection, and search results with urls.

## Features
- Search across domains (Reddit, StackOverflow, etc.).
- Display search results with titles, URLs.
- Custom domain selection for users.
- Responsive design with a dark theme.

## Technologies Used
- Flask (Backend framework)
- EXA API (Search functionality)
- Python-Dotenv (For environment variable management)
- HTML/CSS (Frontend)
- Bootstrap (Styling)
- Jinja2 (Template rendering)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3.x installed.
- You have a valid EXA API key.

## Installation

Follow these steps to install and run the project locally:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/exa-search-app.git
    cd exa-search-app
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of your project and add your EXA API key:

    ```
    EXA_API_KEY=your_exa_api_key
    ```

5. Run the application:

    ```bash
    python app.py
    ```

6. Open your browser and navigate to `http://localhost:5000`.

## Usage

1. Enter a search query in the search bar.
2. Select a domain to search (e.g., Reddit, StackOverflow).
3. Click the "Search" button to retrieve results.
4. The search results will display with clickable titles and URLs.


## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
