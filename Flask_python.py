from flask import Flask, redirect, url_for, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


def pass_fail_function(image):
    return "val1", "val2"


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        # Get the list of files from webpage
        files = request.files.getlist("file")
        len_files = len(files)

        df = pd.DataFrame(columns=["file", "pass/fail", "fail reason"])

        # Iterate for each file in the files List, and Save them
        for file in files:
            output = pass_fail_function(file)
            df.loc[len(df.index)] = [file.filename, output[0], output[1]]
        return render_template(
            "Flask_html_output.html",
            tables=[df.to_html(classes="data")],
            titles=df.columns.values,
        )


if __name__ == "__main__":
    app.run(debug=True)
