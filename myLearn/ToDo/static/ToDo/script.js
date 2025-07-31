function updateStatus(taskId, newStatus) {
    fetch(`/ToDo/update/${taskId}/${newStatus}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
        }
    }).then(() => window.location.reload());
}

function deleteTask(taskId) {
    fetch(`/ToDo/delete/${taskId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
        }
    }).then(() => window.location.reload());
}

function getCSRFToken() {
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
