# # BingPointsBot

A simple automation script using Selenium to perform random searches on Bing and accumulate points.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- A GitHub account

## Getting Started

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone git@github.com:rickscode/BingPointsBot.git
```

### 2. Navigate to the Project Directory

```bash
cd BingPointsBot
```

### 3. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage your dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` File

Create a file named `.env` in the project directory to store your environment variables:

```plaintext
BING_EMAIL=your_email@example.com
BING_PASSWORD=your_password
BING_LOGIN_URL=your unique bing search login url 
```

Replace `your_email@example.com` and `your_password` with your actual Bing account credentials.

### 6. Run the Program

You can now run the script:

```bash
python bingpoints.py
```

### 7. Monitor Output

The program will log in to your Bing account and perform random searches, printing messages to indicate its progress.

## Important Notes

- Ensure that you have a stable internet connection.
- If you encounter issues with the script, make sure your credentials are correct and that there are no security prompts preventing the login.

## License

This project is licensed under a private license. For more information, please contact the project owner.
