// CREDIT: function to close messages after 2 seconds taken from Code Institute
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);
