import typer
from loguru import logger as log
import sys
import psycopg2
import vertica_python

# Log Setup
log.remove()
log.add(sys.stderr, level="INFO")

# CLI Setup
app = typer.Typer()

@log.catch
@app.command()
def helloworld():  ## Adjust function name for better information
    log.success("Dependencies are satisfied - success!")

# Execute CLI for all @app.command calls
if __name__ == "__main__":
    app()	
