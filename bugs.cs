// bugs I have came across while building this web app
1. The problem is that the student variable, which is supposed 
to contain the newly inserted student's data, is assigned the 
result of the SELECT query before the student is inserted. As 
a result, session["user_id"] is assigned None.

// Flash_messages shown along new messages which not expected to be there
2. Summary:
    Upon encountering a bug in the application, the issue arises when 
    submitting a complaint form with incomplete or missing fields. Instead of 
    displaying only the relevant error messages for the incomplete fields, 
    the application incorrectly redirects the user to the show_flash messages 
    page, where the login success message is also displayed. This behavior 
    is inconsistent with the expected behavior, as the user should only see 
    error messages related to the complaint form submission.

Expected Behavior:
    When submitting an incomplete complaint form, the application should remain 
    on the complaint submission page and display error messages specific to the 
    incomplete fields. The error messages should inform the user about the missing 
    information and guide them to complete the form correctly.

Challenge Faced:
    The challenge lies in ensuring that the application redirects users to the 
    correct page (/show_flash) and displays only the relevant error messages for 
    the incomplete complaint form. There is an unexpected interference with the 
    flash messages related to the login success message, which should not be 
    displayed in this context.

    <!-- User info -->
    <!-- <div class= "ml-4 mt-0 flex" >
            < div class= "bg-gray-300 text-black rounded-2xl font-sans p-4" >
                < h1 > Welcome! { { student[0]["full_name"] } }</ h1 >
            </ div >
        </ div > -->


    < !--Route to the Compalint / Request Page -->
    <!-- <div class= "complaint-request m-4 w-56" >
            < a href = "/complaint" >
                < div class= "bg-blue-300 hover:bg-blue-400 p-4 rounded-md" >
                    < h2 > Complaint / Request </ h2 >
                    < p > If you have any request or want to complain, Feel free to provide us details</p>
                </div>
            </a>
        </div> -->