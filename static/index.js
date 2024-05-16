fetch('https://fantastic-bassoon-7vvp459wrwv5hx9xw-8000.app.github.dev/')
.then(response => response.json()) // Parse JSON response
.then(data => {
    alert(data.message); // Handle the data from the server
})
.catch(error => {
    console.error('Error:', error); // Handle any errors
});