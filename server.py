from apps.app import create_app


__author__ = ["mmarconm", "Marcelo Marcon"]
__version__ = "1.0.0"


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=8000)
