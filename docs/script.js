document.getElementById('questionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const question = document.getElementById('question').value;
    
    try {
        const response = await fetch('https://magic-8-ball-iabdulahk7217-w4idun4v.leapcell.dev/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        console.log('Response status:', response.status);
        console.log('Response data:', data);

        if (data.response) {
            document.getElementById('response').textContent = data.response;
        } else if (data.error) {
            document.getElementById('response').textContent = `Error: ${data.error}`;
        }
        
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('response').textContent = 'An error occurred. Please try again.';
    }
});
