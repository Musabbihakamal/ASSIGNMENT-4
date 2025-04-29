import hashlib

# Simulated hash_password function
def hash_password(password):
    """Simulate a hashing function (using SHA256 for this example)."""
    return hashlib.sha256(password.encode()).hexdigest()

# Stored logins: dictionary with email as key and hashed password as value
stored_logins = {
    'user@example.com': hash_password('mysecretpassword'),
    'admin@example.com': hash_password('adminpassword123'),
    'test@example.com': hash_password('testpassword'),
}

def login(email, password_to_check):
    """Check if the provided password matches the stored password hash for the given email."""
    # Check if the email exists in the stored logins
    if email in stored_logins:
        # Get the hashed password stored for this email
        stored_password_hash = stored_logins[email]
        
        # Hash the password the user entered
        hashed_input_password = hash_password(password_to_check)
        
        # Compare the hashed input password with the stored hash
        if stored_password_hash == hashed_input_password:
            return True
        else:
            return False
    else:
        # Email not found
        return False

# Example usage:
email = input("Enter email: ")
password_to_check = input("Enter password: ")

if login(email, password_to_check):
    print("Login successful!")
else:
    print("Login failed!")
