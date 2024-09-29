document.addEventListener('DOMContentLoaded', function() {
    // Get the calendar icon and text icon
    const calendarIcon = document.getElementById('toggle-calendar');
    const textIcon = document.getElementById('toggle-text');
    const timeIcon = document.getElementById('toggle-time');
    const submitButton = document.getElementById('submit-notes');
    const notesContainer = document.getElementById('notes-container');

    // Get the containers
    const calendarContainer = document.getElementById('calendar-container');
    const textContainer = document.getElementById('text-container');
    const timeContainer = document.getElementById('time-container');

    // Function to hide all containers
    function hideAllContainers() {
        calendarContainer.classList.remove('calendar-visible');
        textContainer.classList.remove('text-visible');
        timeContainer.classList.remove('time-visible');
    }

    // Add a click event listener to the calendar icon
    calendarIcon.addEventListener('click', function() {
        if (calendarContainer.classList.contains('calendar-visible')) {
            calendarContainer.classList.remove('calendar-visible');
        } else {
            hideAllContainers();
            calendarContainer.classList.add('calendar-visible');
        }
    });

    // Add a click event listener to the text icon (toggle notesContainer)
    textIcon.addEventListener('click', function() {
        if (notesContainer.style.display === 'block') {
            // If notesContainer is visible, hide it
            notesContainer.style.display = 'none';
        } else {
            // If notesContainer is hidden, show it
            notesContainer.style.display = 'block';
            // Hide all other containers
            hideAllContainers();
        }

        // Manage text container visibility
        if (textContainer.classList.contains('text-visible')) {
            textContainer.classList.remove('text-visible');
        } else {
            hideAllContainers();
            textContainer.classList.add('text-visible');
        }
    });

    // Add a click event listener to the time icon (toggle timeContainer)
    timeIcon.addEventListener('click', function() {
        if (timeContainer.classList.contains('time-visible')) {
            // If timeContainer is visible, hide it
            timeContainer.classList.remove('time-visible');
        } else {
            // If timeContainer is hidden, show it
            hideAllContainers(); // Hide all other containers
            timeContainer.classList.add('time-visible');
        }
    });

    // Add a click event listener to the submit button
    submitButton.addEventListener('click', function() {
        // Your existing AJAX code to save notes would go here

        // Hide the notes container after saving
        notesContainer.style.display = 'none';
    });
});