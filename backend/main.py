import os

from flask_migrate import Migrate

from app import create_app, db
from app.models.product import Product

app = create_app(os.getenv("FLASK_ENV", "development"))
Migrate(app, db)

@app.shell_context_processor
def create_context_processor():
    return dict(
        app=app,
        db=db,
        Product=Product
    )

if __name__ == "__main__":
    app.run(debug=True, port=3001)
