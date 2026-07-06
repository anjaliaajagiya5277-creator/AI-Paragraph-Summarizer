from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""
    paragraph = ""
    error = ""

    if request.method == "POST":

        paragraph = request.form.get("paragraph")

        if len(paragraph.strip()) < 40:

            error = "Please enter at least 40 characters."

        else:

            try:

                summary = summarize_text(paragraph)

            except Exception:

                error = "Something went wrong."

    return render_template(
        "index.html",
        paragraph=paragraph,
        summary=summary,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)