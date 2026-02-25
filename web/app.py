from flask import Flask, render_template, request, jsonify
from problems_data import problems
import traceback
import io
import sys

app = Flask(__name__)

# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("home.html")


# =========================
# TUTORIALS
# =========================

from tutorials_data import tutorials
@app.route("/tutorials/")
@app.route("/tutorials")
def tutorials_home():
    first = tutorials[0]  # default first tutorial

    return render_template(
        "tutorial_detail.html",
        tutorial=first,
        tutorials=tutorials
    )


@app.route("/tutorials/<slug>")
def tutorial_detail(slug):
    tutorial = next((t for t in tutorials if t["slug"] == slug), None)

    if not tutorial:
        return "Tutorial not found", 404

    return render_template(
        "tutorial_detail.html",
        tutorial=tutorial,
        tutorials=tutorials   # important for sidebar
    )

# =========================
# PROBLEM DETAIL
# =========================

@app.route("/practice/<slug>")
def problem_detail(slug):

    problem = next((p for p in problems if p["slug"] == slug), None)

    if not problem:
        return "Problem not found", 404

    return render_template("problem_detail.html", problem=problem)


# =========================
# SUBMIT ENGINE (CLASS BASED)
# =========================

@app.route("/submit/<slug>", methods=["POST"])
def submit_code(slug):

    problem = next((p for p in problems if p["slug"] == slug), None)

    if not problem:
        return jsonify({"error": "Problem not found"}), 404

    data = request.get_json()
    user_code = data.get("code", "")

    function_name = problem["function_name"]
    visible_tests = problem["visible_tests"]
    hidden_tests = problem["hidden_tests"]

    results = []
    all_passed = True

    try:
        exec_globals = {}
        exec(user_code, exec_globals)

        # ✅ Ensure class exists
        if "Solution" not in exec_globals:
            return jsonify({
                "status": "error",
                "message": "Class 'Solution' not found."
            })

        SolutionClass = exec_globals["Solution"]
        solution_instance = SolutionClass()

        # ✅ Ensure method exists
        if not hasattr(solution_instance, function_name):
            return jsonify({
                "status": "error",
                "message": f"Method '{function_name}' not found in Solution class."
            })

        user_function = getattr(solution_instance, function_name)

        # ===== Visible Tests =====
        for i, test in enumerate(visible_tests):
            user_output = user_function(*test["input"])
            expected = test["expected"]

            passed = user_output == expected

            results.append({
                "type": "visible",
                "test_number": i + 1,
                "input": test["input"],
                "passed": passed,
                "expected": expected,
                "actual": user_output
            })

            if not passed:
                all_passed = False

        # ===== Hidden Tests =====
        for test in hidden_tests:
            user_output = user_function(*test["input"])
            expected = test["expected"]

            if user_output != expected:
                all_passed = False

    except Exception:
        return jsonify({
            "status": "error",
            "message": traceback.format_exc()
        })

    return jsonify({
        "status": "success",
        "all_passed": all_passed,
        "results": results
    })


# =========================
# COMPILER (OLD SECTION)
# =========================

@app.route("/compiler", methods=["GET", "POST"])
def compiler():

    output = ""
    starter_code = ""

    problem = request.args.get("problem")

    if problem == "sum":
        starter_code = """def add(a, b):
    return a + b

print(add(5, 3))"""

    elif problem == "evenodd":
        starter_code = """num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")"""

    elif problem == "factorial":
        starter_code = """def factorial(n):
    pass

print(factorial(5))"""

    if request.method == "POST":

        data = request.get_json()
        code = data.get("code", "")
        user_input = data.get("user_input", "")

        old_stdout = sys.stdout
        old_stdin = sys.stdin

        sys.stdout = buffer = io.StringIO()
        sys.stdin = io.StringIO(user_input)

        try:
            exec(code)
            output = buffer.getvalue()
        except Exception as e:
            output = f"ERROR:\n{str(e)}"

        sys.stdout = old_stdout
        sys.stdin = old_stdin

        return jsonify({"output": output})

    return render_template("compiler.html", starter_code=starter_code)


if __name__ == "__main__":
    app.run(debug=True)