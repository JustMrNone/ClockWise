document.addEventListener('DOMContentLoaded', function() {
    // Get the calendar icon and text icon
    const calendarIcon = document.getElementById('toggle-calendar');
    const textIcon = document.getElementById('toggle-text');
    const timeIcon = document.getElementById('toggle-time');

    // Get the containers
    const calendarContainer = document.getElementById('calendar-container');
    const textContainer = document.getElementById('text-container');
    const timeContainer = document.getElementById('time-container');
    // Function to hide all containers
    function hideAllContainers() {
        calendarContainer.classList.remove('calendar-visible');
        textContainer.classList.remove('text-visible');
        timeContainer.classList.remove('time-visible')
    }

    // Add a click event listener to the calendar icon
    calendarIcon.addEventListener('click', function() {
        if (calendarContainer.classList.contains('calendar-visible')) {
            // If the calendar is already visible, just hide it
            calendarContainer.classList.remove('calendar-visible');
        } else {
            // Hide all containers and then show the calendar
            hideAllContainers();
            calendarContainer.classList.add('calendar-visible');
        }
    });

    // Add a click event listener to the text icon
    textIcon.addEventListener('click', function() {
        if (textContainer.classList.contains('text-visible')) {
            // If the text is already visible, just hide it
            textContainer.classList.remove('text-visible');
        } else {
            // Hide all containers and then show the text container
            hideAllContainers();
            textContainer.classList.add('text-visible');
        }
    });

    timeIcon.addEventListener('click', function() {
        if (timeContainer.classList.contains('time-visible')) {
            // If the time is already visible, just hide it
            timeContainer.classList.remove('time-visible');
        } else {
            // Hide all containers and then show the time container
            hideAllContainers();
            timeContainer.classList.add('time-visible');
        }
    });
});
