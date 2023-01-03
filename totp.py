import rumps, pyotp, pyperclip

# Set the seed here
seed = "TOKEN_SEED_HERE"

# Create a TOTP object using the seed
totp = pyotp.TOTP(seed)

# Generate the current token
token = totp.now()

# Copy the token to the clipboard
pyperclip.copy(token)

# Create a system application
app = rumps.App("Quicken TOTP")

# Define an action for the "Generate token" button
@rumps.clicked("Copy token")
def generate_token(sender):
    # Generate the current token
    token = totp.now()
    # Show the pop-up
    rumps.notification("Quicken TOTP", "Copied token: ", token)
    # Copy the token to the clipboard
    pyperclip.copy(token)

# Add the "Generate token" button to the system application
app.menu = ["Copy token"]

# Start the application
app.run()
