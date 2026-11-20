
from flask import Flask, render_template, abort

app = Flask(__name__)

# Portfolio project information
projects = [
    {
        "id": "sales-analysis",
        "title": "Sales Data Analysis",
        "category": "Data Analytics",
        "description": "Analyzed sales data using Python and Pandas to identify sales trends and business insights.",
        "technologies": ["Python", "Pandas", "Matplotlib"],
        "github": "https://github.com/pratikchune/skillpilots-Flask_Portfolio"
    },
    {
        "id": "spam-detection",
        "title": "Spam Email Detection",
        "category": "Machine Learning",
        "description": "Developed a machine learning model to classify emails as spam or legitimate.",
        "technologies": ["Python", "Scikit-learn", "Pandas"],
        "github": "https://github.com/pratikchune/skillpilots-Flask_Portfolio"
    },
    {
        "id": "customer-segmentation",
        "title": "Customer Segmentation",
        "category": "Machine Learning",
        "description": "Used clustering techniques to identify customer groups based on their characteristics.",
        "technologies": ["Python", "K-Means", "Scikit-learn"],
        "github": "https://github.com/pratikchune/skillpilots-Flask_Portfolio"
    }
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        projects=projects
    )

@app.route("/projects/<project_id>")
def project_details(project_id):
    project = next(
        (p for p in projects if p["id"] == project_id),
        None
    )

    if project is None:
        abort(404)

    return render_template(
        "project.html",
        project=project
    )

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(debug=True)
