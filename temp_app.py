# temp_app.py
#chatgpt ah code
import os

def read_credentials(filepath):
    credentials = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    key, value = line.split('=', 1)
                    credentials[key.strip()] = value.strip()
    except Exception as e:
        print(f"Error reading credentials from {filepath}: {e}")
    return credentials

def main():
    # Path where Vault Agent is expected to render the secret file.
    secret_file_path = "/etc/my-app-secret/my-app-secret.conf"
    
    print("Starting temporary app to display credentials...")
    print(f"Attempting to read credentials from: {secret_file_path}")
    
    credentials = read_credentials(secret_file_path)
    
    if credentials:
        print("Credentials retrieved:")
        for key, value in credentials.items():
            print(f"{key} = {value}")
    else:
        print("No credentials found or an error occurred.")
        
if __name__ == '__main__':
    main()