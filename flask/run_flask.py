from datetime import datetime
import os

import click
import flask


@click.command()
@click.option(
    "--vite", is_flag=True, default=False,
    help="If true, serve the vite directory. Otherwise, serve browser-js"
)
def main(vite):
    if vite:
        app = flask.Flask(
            __name__, instance_path=os.getcwd(),
            static_folder="../vite/dist/assets"
        )
        @app.route("/")
        def homepage():
            """Return the homepage."""
            return flask.send_file(
                "../vite/dist/index.html")
    else:
        app = flask.Flask(
            __name__, instance_path=os.getcwd(),
            static_folder="../browser-js/src"
        )
        @app.route("/")
        def homepage():
            """Return the homepage."""
            return flask.send_file(
                "../browser-js/index.html")

    @app.route("/api/time/current", methods=["GET"])
    def get_current_time():
        """Return the homepage."""
        return {"current_time": datetime.now()}

    app.run(host="127.0.0.1", port=5212)


if __name__ == "__main__":
    main()
