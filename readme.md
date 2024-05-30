# Voice-Based Email System for the Visually Impaired

This project is a voice-based email system designed to assist visually impaired users in composing and reading emails through voice commands. The system uses speech recognition, text-to-speech, and email handling libraries to provide a seamless experience.

## Features

- Compose and send emails using voice commands.
- Check the inbox and read unread emails using voice commands.
- Text-to-speech feedback for all actions and prompts.

## Requirements

The following packages are required to run this project:

- `speechrecognition`
- `pyaudio`
- `beautifulsoup4`
- `gtts`
- `pyglet`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/voice-based-email.git
    cd voice-based-email
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**

    ```bash
    python voice_email.py
    ```

2. **Follow the voice prompts:**

    - To compose an email, say "Compose a mail" or any recognized phrase for option 1.
    - To check your inbox, say "Check your inbox" or any recognized phrase for option 2.

3. **For composing an email:**
    - You will be prompted to speak the subject of the email.
    - Then you will be prompted to speak the body of the email.

4. **For checking your inbox:**
    - The system will announce the total number of emails and the number of unseen emails.
    - The latest unseen email's sender, subject, and body will be read aloud.

## Configuration

Ensure you have the correct email credentials in the script:

- Replace `"miniyamini2525@outlook.com"` with your sender email address.
- Replace `"taneniyamini@gmail.com"` with your receiver email address.
- Replace `"Qwerty@123456"` with your email password.

**Note:** For security reasons, do not hardcode your password in production code. Use environment variables or secure vaults to store sensitive information.

## Example Interaction

Here is an example interaction:

You are logging from: tanen

Compose a mail.
Check your inbox
Your choice: Check your inbox
Number of emails in your inbox: 5
Your unseen emails are: 2
From: example@example.com
Subject: Test Email
Body: This is a test email.



## Troubleshooting

- Ensure your microphone is working and accessible by the script.
- Verify that you have an active internet connection for the speech recognition service.
- Make sure IMAP and SMTP access is enabled in your email account settings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [Google Text-to-Speech](https://pypi.org/project/gTTS/)
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [Pyglet](https://pypi.org/project/pyglet/)
