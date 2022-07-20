import requests
import random
import sys

# Rich imports
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress

# Internal imports
sys.path.append('..')
from internal.model.helper import get_input

# Maximum number of rows to be displayed
rows_limit = 100


def get_distance(page, target):
    page = page.replace(' ', '_')
    model_input = get_input(page, target)
    return random.uniform(1.0, 6.0)


def get_links(title):
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": "max"
    }

    response = session.get(url=url, params=params)
    data = response.json()
    pages = data["query"]["pages"]

    page_titles = []

    for key, val in pages.items():
        for link in val["links"]:
            page_titles.append(link["title"])

    while "continue" in data:
        plcontinue = data["continue"]["plcontinue"]
        params["plcontinue"] = plcontinue

        response = session.get(url=url, params=params)
        data = response.json()
        pages = data["query"]["pages"]

        for key, val in pages.items():
            for link in val["links"]:
                page_titles.append(link["title"])

    return page_titles


# Get page rows in a table format (id - page - distance)
def get_page_rows(page, target):
    rows_table = []
    raw_rows = []

    with Progress() as progress:
        getting_links = progress.add_task("[blue]Getting links...", total=100)
        links = get_links(page)
        progress.update(getting_links, advance=100)

        getting_distances = progress.add_task("[green]Getting distances...", total=len(links))
        for link in links:
            raw_rows.append([str(link), get_distance(link, target)])
            progress.update(getting_distances, advance=1)

        cleaning_up = progress.add_task("[red]Cleaning up...",total=100)
        raw_rows = sorted(raw_rows, key=lambda x: x[1], reverse=False)

        for row_id, row_value in enumerate(raw_rows):
            rows_table.append([str(row_id + 1), row_value[0], str(row_value[1])])
        progress.update(cleaning_up, advance=100)

    return rows_table


def print_table(title, target):
    table = Table(title="Shortest Paths")

    table.add_column("#", style="cyan", no_wrap=True)
    table.add_column("Page", style="magenta")
    table.add_column("Distance", justify="right", style="green")

    page_rows = get_page_rows(title, target)
    rows_number = min(len(page_rows), rows_limit)
    cut_rows = page_rows[:rows_number]
    reversed_rows = list(reversed(cut_rows))

    for row in reversed_rows:
        table.add_row(row[0], row[1], row[2])

    console = Console()
    console.print(table)


if __name__ == "__main__":
    current_page = Prompt.ask("Enter your current page")
    target_page = Prompt.ask("Enter your target page")

    print_table(current_page, target_page)
