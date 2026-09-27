from flask import Flask, jsonify

# ---------------------------------------------------------
# AI BlogNest API
# ---------------------------------------------------------

app = Flask(__name__)

# ---------------------------------------------------------
# Home / Main API Route
# ---------------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI BlogNest API is running"
    })


# ---------------------------------------------------------
# API Information Route
# ---------------------------------------------------------

@app.route("/api", methods=["GET"])
def api_information():
    return jsonify({
        "name": "AI BlogNest API",
        "version": "1.0",
        "status": "running",
        "description": "An API for an AI powered blogging application"
    })


# ---------------------------------------------------------
# Health Check Route
# ---------------------------------------------------------

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "AI BlogNest server is working properly"
    })


# ---------------------------------------------------------
# About Route
# ---------------------------------------------------------

@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "application": "AI BlogNest",
        "purpose": "AI powered blog management system",
        "technology": "Python Flask",
        "server": "Development Server"
    })


# ---------------------------------------------------------
# Blog Information Route
# ---------------------------------------------------------

@app.route("/blogs", methods=["GET"])
def blogs():
    blog_data = [
        {
            "id": 1,
            "title": "Introduction to Artificial Intelligence",
            "category": "AI",
            "status": "published"
        },
        {
            "id": 2,
            "title": "Understanding Machine Learning",
            "category": "Machine Learning",
            "status": "published"
        },
        {
            "id": 3,
            "title": "Future of Technology",
            "category": "Technology",
            "status": "draft"
        }
    ]

    return jsonify({
        "total_blogs": len(blog_data),
        "blogs": blog_data
    })


# ---------------------------------------------------------
# User Information Route
# ---------------------------------------------------------

@app.route("/users", methods=["GET"])
def users():
    users_data = [
        {
            "id": 1,
            "name": "Admin",
            "role": "Administrator"
        },
        {
            "id": 2,
            "name": "Author",
            "role": "Writer"
        }
    ]

    return jsonify({
        "total_users": len(users_data),
        "users": users_data
    })


# ---------------------------------------------------------
# Start Flask Application
# ---------------------------------------------------------

if __name__ == "__main__":
    print("--------------------------------------------")
    print("       AI BlogNest API Server")
    print("--------------------------------------------")
    print("Server is starting...")
    print("Open your browser and visit:")
    print("http://127.0.0.1:5000/")
    print("--------------------------------------------")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )