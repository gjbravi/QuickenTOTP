import rumps, pyotp, pyperclip

# Set the seed here
seed = "token_seed_here"

# Create a TOTP object using the seed
totp = pyotp.TOTP(seed)

# Generate the current token
token = totp.now()

# Copy the token to the clipboard
pyperclip.copy(token)

# Create a system application
app = rumps.App("Quick TOTP")

# Define an action for the "Generate token" button
@rumps.clicked("Copy token")
def generate_token(sender):
    # Generate the current token
    token = totp.now()
    # Show the pop-up
    rumps.notification("Quick TOTP", "Copied token: ", token)
    # Copy the token to the clipboard
    pyperclip.copy(token)

# Add the "Generate token" button to the system application
app.menu = ["Generate token"]

# Start the application
app.run()
