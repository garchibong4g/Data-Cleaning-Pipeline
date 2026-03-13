import argparse
from src.logger import setup_logger
from src.config_loader import load_config
from src.data_loader import load_csv
from src.cleaner import clean_data
from src.analyzer import compute_power, generate_summary
from src.reporter import export_cleaned, export_summary
from src.visualization import plot_power

def main():

    # Step 1: Parse CLI arguments
    parser = argparse.ArgumentParser(description="Sensor Data Automation Pipeline")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--config", default="config.yaml", help="Path to config file")
    args = parser.parse_args()

    # Step 2: Setup logging
    logger = setup_logger()

    # Step 3: Load configuration
    config = load_config(args.config)

    # Step 4: Load data
    data = load_csv(args.input)

    # Step 5: Clean data (THIS is where config is used)
    cleaned_data = clean_data(data, config)

    # Step 6: Compute power
    df_power = compute_power(cleaned_data)

    # Step 7: Generate summary
    summary = generate_summary(df_power)

    # Step 8: Export outputs
    export_cleaned(df_power, config["output"]["cleaned_file"])
    export_summary(summary, config["output"]["summary_file"])
    plot_power(df_power, config["output"]["plot_file"])

    logger.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()