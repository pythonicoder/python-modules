import importlib


def check_versions(pd, np, req, mpl):
    print("Checking dependencies:")
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    print(f"[OK] requests ({req.__version__}) - Network access ready")
    print(f"[OK] matplotlib ({mpl.__version__}) - Visualization ready")


def dependency_info():
    print("\nDependency management:")
    print("pip -> requirements.txt")
    print("Poetry -> pyproject.toml")
    print()


def main():
    print("LOADING STATUS: Loading programs...")

    try:
        pd = importlib.import_module("pandas")
        np = importlib.import_module("numpy")
        req = importlib.import_module("requests")
        plt = importlib.import_module("matplotlib.pyplot")
        mpl = importlib.import_module("matplotlib")

    except ImportError as e:
        print(f"[MISSING] {e}")

        print("\nInstall with pip:")
        print("pip install -r requirements.txt")

        print("\nOr with Poetry:")
        print("poetry install")
        return

    check_versions(pd, np, req, mpl)
    dependency_info()

    print("Analyzing Matrix data...")

    matrix_data = np.random.normal(loc=50, scale=15, size=1000)

    df = pd.DataFrame({
        "signal_strength": matrix_data
    })

    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")

    plt.hist(df["signal_strength"], bins=20)

    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    plt.grid(True)
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
