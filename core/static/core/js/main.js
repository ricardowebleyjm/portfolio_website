document.getElementById('hireMeForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    const formData = new FormData(this); 
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    var hireMeModal = bootstrap.Modal.getInstance(document.getElementById('hireMeModal'));
    
    try {
        const response = await fetch('hire-me/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: formData
        });

        const data = await response.json();
        const toastMessage = document.getElementById('toastMessage');

        if (response.ok) {
            toastMessage.textContent = data.message || 'Your message has been sent!';
            document.getElementById('successToast').classList.add('show'); 
        } else {
            toastMessage.textContent = data.message || 'Something went wrong, please try again.';
            document.getElementById('successToast').classList.add('show'); 
        }
        
        hireMeModal.hide(); 
        this.reset();
        setTimeout(() => {
            document.getElementById('successToast').classList.remove('show');
        }, 3000);

    } catch (error) {
        console.error('Error submitting form:', error);
        const toastMessage = document.getElementById('toastMessage');
        toastMessage.textContent = 'There was an error submitting the form.';
        document.getElementById('successToast').classList.add('show');
    }
});

