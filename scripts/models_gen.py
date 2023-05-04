import os
import re
from pathlib import Path
from urllib.parse import urlparse
from datamodel_code_generator import generate, InputFileType


JSON_API_URL = 'https://demo.mediascout.ru/swagger/v1/swagger.json'
src_dir = os.path.dirname(os.path.abspath("."))+"/src/ord_mediascout_client"

add_func: str = """
from pydantic import BaseModel, Extra


def capitalize(s: str) -> str:
    return s[0].upper() + s[1:]
"""

add_props = """
        extra = Extra.forbid
        alias_generator = capitalize
        allow_population_by_field_name = True
"""


def main() -> None:
    output = Path(f'{src_dir}/new_models.py')

    generate(
        urlparse(JSON_API_URL),
        input_file_type=InputFileType.OpenAPI,
        output=output,
    )

    model: str = output.read_text()
    model = re.sub(r'\nfrom pydantic import BaseModel, Extra\n', add_func, model)
    model = re.sub(r'\n        extra = Extra.forbid\n', add_props, model)

    output.write_text(model)

if __name__ == '__main__':
    main()
