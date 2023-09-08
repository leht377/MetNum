import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = "1.0.0"
PACKAGE_NAME = "metnum"
AUTHOR = "DIEGO ALEJANDRO ESPINEL B , LUIS EDUARDO HERNANDEZ T"
AUTHOR_EMAIL = "XXX@gmail.com"
URL = "https://github.com/leht377/metnum_base.git"

LICENSE = "MIT"
DESCRIPTION = "MetNum es una libreria de métodos numéricos, los métodos numéricos son una herramienta esencial para los científicos y matemáticos que necesitan resolver problemas que no se pueden resolver mediante métodos analíticos tradicionales. En lugar de obtener soluciones exactas, los métodos numéricos utilizan cálculos aproximados para encontrar soluciones que se acercan lo suficiente a la respuesta real."
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["numpy", "matplotlib", "tabulate"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
)
