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

document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM is fully loaded!")
    // Get the dropdown and button elements
    var dropdown = document.getElementById('burger-menu-content');
    var button = document.getElementById('burger-menu');

    if (button) {


        // Function to close the dropdown by adding 'hidden' and removing 'block'
        function closeDropdown() {
            dropdown.classList.add('hidden');
            dropdown.classList.remove('block');
        }

        // Toggle visibility of the dropdown on button click
        button.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent the window click event from firing immediately
            dropdown.classList.remove('hidden');
            dropdown.classList.toggle('block');
        });

        // Close the dropdown when clicking outside of it
        window.addEventListener('click', function (event) {
            if (!dropdown.contains(event.target) && !button.contains(event.target)) {
                closeDropdown();
            }
        });

    }
});
