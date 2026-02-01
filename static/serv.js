// login.js

async function compLogin(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("All fields are required");
        return;
    }

    try {
        const res = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                task: "login",
                data: {
                    email,
                    password
                }
            })
        });

        const result = await res.json();

        if (result.status !== "ok") {
            alert(result.msg || "Login failed");
            return;
        }

        localStorage.setItem("user", JSON.stringify(result.user));
        localStorage.setItem("token", result.token);

            window.location.href = "/student/dashboard";

    } catch (err) {
        console.error(err);
        alert("Server error. Try again later.");
    }
}
async function compSignup(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("All fields are required");
        return;
    }

    try {
        const res = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                task: "newRecruiter",
                data: {
                    email,
                    password
                }
            })
        });

        const result = await res.json();

        if (result.status !== "ok") {
            alert(result.msg || "Login failed");
            return;
        }

        localStorage.setItem("user", JSON.stringify(result.user));
        localStorage.setItem("token", result.token);

            window.location.href = "/student/dashboard";

    } catch (err) {
        console.error(err);
        alert("Server error. Try again later.");
    }
}

