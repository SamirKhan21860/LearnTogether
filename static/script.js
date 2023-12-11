// Define a custom function to assign category-specific styles
function get_message_style_class(category) {
    // Implement your logic to determine the category and return the corresponding class
    switch (category) {
        case 'error':
            return 'bg-red-500 text-white';
        case 'info':
            return 'bg-blue-500 text-white';
        case 'success':
            return 'bg-green-500 text-white';
        // Add more cases as needed
        default:
            return 'bg-gray-500 text-white'; // Default style
    }
}

// Even listener for menu button
document.getElementById('burger-menu').addEventListener('click', function () {
    document.getElementById('burger-menu-content').classList.toggle('hidden');
});

z