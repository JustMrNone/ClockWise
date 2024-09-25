document.addEventListener("DOMContentLoaded", function () {
    // Get the textarea and hidden notes input
    const submitNotesButton = document.getElementById("submit-notes");
    const notesTextarea = document.getElementById("notes-textarea");
    const hiddenNotesInput = document.getElementById("notes");

    // Save the notes when the user clicks "Save Notes"
    submitNotesButton.addEventListener("click", function () {
        // Update the hidden notes input with the value from the textarea
        hiddenNotesInput.value = notesTextarea.value;
    });
});
