from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""
    paragraph = ""
    error = ""

    # Add these variables
    paragraph_lines = 0
    summary_lines = 0

    if request.method == "POST":

        paragraph = request.form.get("paragraph")

        if len(paragraph.strip()) < 40:

            error = "Please enter at least 40 characters."

        else:

            try:

                summary = summarize_text(paragraph)

                # Count original paragraph lines
                paragraph_lines = len(
                    [line for line in paragraph.splitlines() if line.strip()]
                )

                # Count summary lines
                summary_lines = len(
                    [line for line in summary.splitlines() if line.strip()]
                )

            except Exception:

                error = "Something went wrong."

    return render_template(
        "index.html",
        paragraph=paragraph,
        summary=summary,
        error=error,
        paragraph_lines=paragraph_lines,
        summary_lines=summary_lines
    )


if __name__ == "__main__":
    app.run(debug=True)