# htmlTemplates.py

# CSS for Leaner UI with White Background
css = '''
<style>
/* General Body Style */
body {
    background-color: #ffffff;
    color: #333;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* Chat Message Styling */
.chat-message {
    padding: 1rem;  /* Reduced padding for a leaner look */
    border-radius: 0.5rem;
    margin-bottom: 0.8rem;  /* Reduced margin for a compact layout */
    display: flex;
    max-width: 100%;
}

.chat-message.user {
    background-color: #f7f7f7; /* Lighter background for user messages */
}

.chat-message.bot {
    background-color: #e2e2e2; /* Lighter background for bot messages */
}

/* Avatar Styling */
.chat-message .avatar {
    width: 15%;  /* Smaller avatar size */
    min-width: 50px;
}

.chat-message .avatar img {
    max-width: 50px;  /* Adjusted avatar size */
    max-height: 50px;
    border-radius: 50%;
    object-fit: cover;
}

/* Message Styling */
.chat-message .message {
    width: 85%;  /* Adjusted width to make messages take more space */
    padding: 0 1rem;  /* Reduced padding */
    font-size: 0.9rem;  /* Reduced font size for a cleaner look */
    color: #333;  /* Darker text color for better readability */
}

/* Dark Mode Styles (Optional) */
body.dark-mode {
    background-color: #2b313e;
    color: #fff;
}

body.dark-mode .chat-message.user {
    background-color: #3e4a59;
}

body.dark-mode .chat-message.bot {
    background-color: #475063;
}

body.dark-mode .chat-message .message {
    color: #fff;
}

</style>
'''

# Bot template (HTML structure)
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# User template (HTML structure)
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img  style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
