🔒 Encrypted Text Decryption Project

🌟 Overview

    This Python project demonstrates a simple encryption-decryption mechanism. It analyzes an encrypted text file, identifies patterns, and decrypts it using a predefined mapping. The results are saved in a new file and additional statistics, such as the longest word and line count, are computed.

🛠 Features


    - Character Frequency Analysis: Identifies the four most frequent characters in the encrypted text.
    - Custom Decryption Mapping: Maps frequent characters to specified replacements.
    - File Operations: Reads from and writes to files for encrypted and decrypted content.
    - Text Statistics:
        - Finds the longest alphabetic word.
        - Counts the number of lines in the result file.
    - Pattern Generation: Appends patterns and processed content to the original file.
📂 Project Structure

    .
    ├── file.txt               # Input file with encrypted text
    ├── results.txt            # File containing the decrypted text
    ├── P1.py                # Main application logic
    └── README.md              # Project documentation
🔧 Setup Guide

Prerequisites

    Python 3.x installed on your system.
Installation 

Clone the repository:

        git clone https://github.com/matanohana433/python_core.git
        cd python_core
🚀 Usage

1. Run the main script:


    python main.py
2. What it does:

        - Reads the encrypted content from file.txt.
        - Analyzes the text and decrypts it based on a custom mapping.
        - Writes the decrypted content into results.txt.
        - Prints additional statistics:
            - The longest word in the results.
            - The total number of lines in the results.
📊 Example Output

Decrypted Text:

        'Practice, Eventually Makes Perfect. All You Need Is Python.'
        J.R.R.R Tolkin. 
        Oops Its Not Him; ---> Etor

    Your longest word is Eventually

    The number of lines is 3
🔍 Key Learnings

    - File Handling: Demonstrates reading and writing to text files.
    - String Manipulation: Performs character replacements and word filtering using regex.
    - Basic Cryptography: Implements simple character-based encryption and decryption.
    - Pattern Generation: Adds visual patterns to the file for enhanced presentation.

📬 Contact

    For questions or collaboration opportunities, feel free to reach out:

Email: matanohana433@gmail.com
GitHub: matanohana433