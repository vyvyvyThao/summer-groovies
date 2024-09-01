function handleRegistration(endpoint) {
    registerEndpoint = `http://localhost:8000${endpoint}register/`
    console.log(registerEndpoint);

    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access')
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: "GET",
        headers: headers
    }

    fetch(registerEndpoint, options)
        .then(response => {
            response.text();
            console.log(response);
        })
        .then(data => {
        });
}