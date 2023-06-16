import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
import all_func


def main():
    load_dotenv()
    filepath = os.getenv('FILEPATH')

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', help='Ваш путь к файлу, например example.xlsx или folder/example.xlsx')
    args = parser.parse_args()

    if args.filepath:
        filepath = args.filepath

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=f'{datetime.datetime.now().year - 1920} {all_func.get_correct_form_year(datetime.datetime.now().year)}',
        drinks=all_func.get_drinks(filepath),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
