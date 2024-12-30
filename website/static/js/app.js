document.addEventListener('DOMContentLoaded', () => {
    
    const playerComparisonForm = document.getElementById('player-comparison-form');
    playerComparisonForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const batter = document.getElementById('batter').value;
        const bowler = document.getElementById('bowler').value;
        const year = document.getElementById('year').value;

        alert(`Comparing ${batter} vs ${bowler} for the year ${year}.`);
    });

    const tabs = document.querySelectorAll('.standings-nav a');
    const groups = document.querySelectorAll('.standings-group');

    tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            e.preventDefault();

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));

            // Add active class to clicked tab
            tab.classList.add('active');

            // Hide all groups
            groups.forEach(group => (group.style.display = 'none'));

            // Show the selected group
            const targetGroup = document.querySelector(tab.getAttribute('href'));
            if (targetGroup) targetGroup.style.display = 'block';
        });
    });

    // Default: Show the first group (Group A)
    document.querySelector('#group-a').style.display = 'block';

    // Semi-finals Match Cards Interactivity
    const semiFinalsSection = document.querySelector('.semi-finals-section');
    if (semiFinalsSection) {
        const matchCards = semiFinalsSection.querySelectorAll('.match-card');
        matchCards.forEach(card => {
            card.addEventListener('click', () => {
                const winner = card.querySelector('.result span:first-child').innerText;
                alert(`Match Highlight: ${winner}`);
            });
        });
    }

    // Feedback Form
    const feedbackForm = document.getElementById("feedback-form");

    feedbackForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const firstName = document.getElementById("first-name").value;
        const lastName = document.getElementById("last-name").value;
        const email = document.getElementById("email").value;
        const company = document.getElementById("company").value;
        const country = document.getElementById("country").value;
        const services = document.getElementById("services").value;
        const message = document.getElementById("message").value;

        alert(`
            Thank you for your feedback, ${firstName} ${lastName}!
            We'll get back to you at ${email}.
        `);

        // Optionally reset the form
        feedbackForm.reset();
    });
});
