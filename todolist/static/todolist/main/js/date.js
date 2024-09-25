const daysContainer = document.querySelector('.days');
const currentMonthEl = document.querySelector('.current-month');
const todayDateEl = document.querySelector('.today-date');
const dueDateInput = document.getElementById('due_date'); // Hidden input field for due date
const prevMonthBtn = document.querySelector('.prev-month');
const nextMonthBtn = document.querySelector('.next-month');
const weekDaysEl = document.querySelectorAll('.week-days div');

let currentDate = new Date();
let selectedDate = new Date();

// Function to initialize and update the calendar
function updateCalendar() {
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();

    // Set the current month text
    currentMonthEl.textContent = currentDate.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });

    // Get the number of days in the current month
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDayOfMonth = new Date(year, month, 1).getDay();

    // Clear out any existing day elements to prevent duplicate entries
    daysContainer.innerHTML = '';

    // Fill in the blank days before the first day of the month
    for (let i = 0; i < firstDayOfMonth; i++) {
        const blankDay = document.createElement('div');
        blankDay.classList.add('day', 'empty');
        daysContainer.appendChild(blankDay);
    }

    // Populate days of the current month
    for (let day = 1; day <= daysInMonth; day++) {
        const dayEl = document.createElement('div');
        dayEl.classList.add('day');
        dayEl.textContent = day;

        // Highlight today's date
        if (day === currentDate.getDate() && month === new Date().getMonth() && year === new Date().getFullYear()) {
            dayEl.classList.add('today');
        }

        // Highlight the selected date
        if (day === selectedDate.getDate() && month === selectedDate.getMonth() && year === selectedDate.getFullYear()) {
            dayEl.classList.add('selected');
        }

        // Add click event to pick a day
        dayEl.addEventListener('click', () => {
            selectedDate = new Date(year, month, day);
            updateSelectedDate();
            updateCalendar();
        });

        daysContainer.appendChild(dayEl);
    }

    // Highlight the current day's name (Su, Mo, Tu, etc.) based on the selected date
    highlightSelectedWeekday();
}

// Reset the calendar to the current date and show it
function openCalendar() {
    currentDate = new Date(); // Reset to current date
    updateCalendar();
    updateSelectedDate();
}

// Function to update the selected date and the hidden input
function updateSelectedDate() {
    // Update the "Today's Date" section with the selected date
    todayDateEl.textContent = selectedDate.toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
    });
    
    // Update the due date input with the selected date in YYYY-MM-DD format
    dueDateInput.value = selectedDate.toISOString().split('T')[0]; // Format as YYYY-MM-DD
}

function highlightSelectedWeekday() {
    // Remove the highlight from all weekdays first
    weekDaysEl.forEach((el) => el.classList.remove('highlighted'));

    // Get the selected day of the week (0 = Sunday, 6 = Saturday)
    const selectedWeekday = selectedDate.getDay();
    
    // Highlight the corresponding weekday name
    weekDaysEl[selectedWeekday].classList.add('highlighted');
}

// Function to navigate to the previous month
prevMonthBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    updateCalendar();
});

// Function to navigate to the next month
nextMonthBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    updateCalendar();
});

// Event listener to open the calendar
document.getElementById('toggle-calendar').addEventListener('click', openCalendar);

// Initialize the calendar with the current date
updateCalendar();
updateSelectedDate();
