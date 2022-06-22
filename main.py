from internal.dataset_generator import web_clicker, charter
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description='ML Wikipedia Runner')
    parser.add_argument('-m', '--mode',
                        type=str,
                        help='program mode',
                        required=True,
                        choices=['generate', 'csv-chart'])

    args = parser.parse_args()

    if args.mode == 'generate':
        web_clicker.launch()
        return
    elif args.mode == 'csv-chart':
        charter.show_chart()
        return
    else:
        logging.error('Specified mode does not exist')
        exit(1)


if __name__ == "__main__":
    main()
