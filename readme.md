# TOTP Token Generator for macOS

This is a one-time password (TOTP) generator that allows users to generate tokens and copy them to the clipboard. It is useful for two-factor authentication on secure online accounts.

## Installation

To install the dependencies for this project, run the following command:

```pip install rumps pyotp pyperclip```

OR

```pip install -r requirements.txt```

## Usage

To run the TOTP generator, use the following command:

```python3 totp.py```

OR

In case you would like to run a background process, you can use nohup:

```nohup python3 totp.py &```

A menu bar icon will appear with a "Generate token" button. Click the button to generate a new token and copy it to the clipboard.

## Dependencies

This project requires the following libraries:

- rumps
- pyotp
- pyperclip

## Plans for improvements

- Containerize and ship a pre-built lightweight image
- Add vault to encrypt token seed
- and more

## Maintainers

- gbravi