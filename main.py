from internal.dataset_generator import web_clicker, charter, csv_interactor_with_features
import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description='ML Wikipedia Runner')
    parser.add_argument('-m', '--mode',
                        type=str,
                        help='program mode',
                        required=True,
                        choices=['generate', 'six-degrees-chart', 'generator-chart', 'generate-features', 'features-info', 'add-header'])
    parser.add_argument('-o', '--offset',
                        type=int,
                        help='from which row to begin')

    args = parser.parse_args()

    if args.mode == 'generate':
        web_clicker.launch()
        return
    elif args.mode == 'six-degrees-chart':
        charter.draw_chart('six_degrees')
        return
    elif args.mode == 'generator-chart':
        charter.draw_chart('generator')
        return
    elif args.mode == 'generate-features':
        csv_interactor_with_features.generate_dataset_saved(args.offset)
        return
    elif args.mode == 'features-info':
        csv_interactor_with_features.print_info()
        return
    elif args.mode == 'add-header':
        csv_interactor_with_features.add_header()
        return
    else:
        logging.error('Specified mode does not exist')
        exit(1)


if __name__ == "__main__":
    main()
    