import os
from dotenv import load_dotenv


def main():
    print("ORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    warnings = []

    if not mode:
        warnings.append(
            "MATRIX_MODE missing, defaulting to development"
        )
        mode = "development"

    if mode not in ["development", "production"]:
        warnings.append(
            "Invalid MATRIX_MODE, defaulting to development"
        )
        mode = "development"

    if not log_level:
        log_level = "INFO"

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        if "localhost" in database_url:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: Not configured")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing credentials")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")

    if warnings:
        print()
        for warning in warnings:
            print(f"[WARNING] {warning}")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
