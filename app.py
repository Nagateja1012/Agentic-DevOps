import os

def add(a, b):
    return a + b


def load_config():
    api_key = os.getenv("APP_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing required environment variable: APP_API_KEY")
    return api_key

def main():
    config = load_config()
    print(f"App is running with API KEY: {config}")

if __name__ == "__main__":
    main()
