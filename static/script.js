// // Define a custom function to assign category-specific styles
// function message_style(category) {
//     // Implement your logic to determine the category and return the corresponding class
//     switch (category) {
//         case 'error':
//             console.log("Error Printed on the console!")
//             return 'bg-red-500 text-white';
//         case 'info':
//             console.log("Info Printed on the console!")
//             return 'bg-blue-500 text-white';
//         case 'success':
//             console.log("Success Printed on the console!")
//             return 'bg-green-500 text-white';
//         // Add more cases as needed
//         default:
//             return 'bg-gray-500 text-white'; // Default style
//     }
// }

document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM is fully loaded!");
    // Get the dropdown and button elements
    var dropdown = document.getElementById("burger-menu-content");
    var button = document.getElementById("burger-menu");

    if (button) {
        // Function to close the dropdown by adding 'hidden' and removing 'block'
        function closeDropdown() {
            dropdown.classList.add("hidden");
            dropdown.classList.remove("block");
        }

        // Toggle visibility of the dropdown on button click
        button.addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent the window click event from firing immediately
            dropdown.classList.remove("hidden");
            dropdown.classList.toggle("block");
        });

        // Close the dropdown when clicking outside of it
        window.addEventListener("click", function (event) {
            if (!dropdown.contains(event.target) && !button.contains(event.target)) {
                closeDropdown();
            }
        });
    }
});

// element dynamically using JavaScript if it doesn't exist in the HTML
function showFlashMessage(message, category) {
    // Create or get the flash container
    var flashContainer = document.getElementById("flash-container");
    if (!flashContainer) {
        flashContainer = document.createElement("div");
        flashContainer.id = "flash-container";
        flashContainer.classList.add("absolute", "top-0", "right-0");
        document.body.appendChild(flashContainer);
    } else {
        // if flash_container exist then clear
        while (flashContainer.firstChild) {
            flashContainer.removeChild(flashContainer.firstChild);
        }
    }

    // Now create a new flash message div element
    var flashMessage = document.createElement("div");
    flashMessage.classList.add(
        "m-4",
        "p-4",
        "hover:bg-opacity-30",
        "rounded-md",
        "bg-green-500",
        "bg-opacity-50",
        "text-white",
        "transition-bg",
        "duration-300",
        "ease-in-out"
    );

    // Content of the flash message
    flashMessage.innerHTML = `<span class="mr-2">${message}</span><button class="text-white font-bold font-mono text-lg" onclick="closeFlashMessage(this.parentElement)">X</button>`;

    // Append the flash message to the container
    flashContainer.appendChild(flashMessage);

    // Using timeout to automatically remove the flash message after 5 seconds
    setTimeout(function () {
        closeFlashMessage(flashMessage);
    }, 5000);
}

function closeFlashMessage(flashMessage) {
    // Slide out the flash message
    flashMessage.style.transition = 'transform 0.3s ease-in-out';
    flashMessage.style.transform = 'translateX(110%)';

    // Remove the lement from the DOM after the transition completes
    flashMessage.addEventListener('transitionend', function() {
        flashMessage.remove();
    });
}

// Fetch and display Flask flash messages
document.addEventListener("DOMContentLoaded", function() {
    // The .parse() will convert it to the object
    var flashMessages = JSON.parse('{{ get_flashed_messages() | tojson | safe }}');

    // Check if have any messages to show
    if (flashMessages) {
        flashMessages.forEach(function (message) {
            // at index 0: message and index 1: category
            showFlashMessage(message[0], message[1]);
        });
    }
});
