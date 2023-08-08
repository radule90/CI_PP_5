// Stripe

// Get public key, clean extra white spaces and quotes
let stripePublicKey = document.getElementById('id_stripe_public_key');
stripePublicKey = stripePublicKey.textContent.trim().slice(1, -1);

// Get the client secret
let clientSecret = document.getElementById('id_client_secret');
clientSecret = clientSecret.textContent.trim().slice(1, -1);

// Initialize the Stripe with public key and create new Stripe instance element
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

// Style for Stripe card
let style = {
    base: {
        iconColor: '#8cada4',
        color: '#8cada4',
        fontWeight: '500',
        fontFamily: 'Quicksand, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
            color: '#8cada4',
        },
        '::placeholder': {
            color: '#8cada4',
        },
    },
    invalid: {
        iconColor: '#ff6961',
        color: '#ff6961',
    },
};

// Create and mount card element in #card-element div
let card = elements.create('card', { style: style });
card.mount('#card-element');


// Handle validation errors
card.addEventListener('change', (event) => {
    let errorsDiv = document.getElementById('card-errors');
    // If errors exist display them in #card-errors div
    if (event.error) {
        let html = `
            <dialog open>
                <form method="dialog">
                    ${event.error.message}
                    <button class="custom-pointer">
                        <i class="fa-solid fa-xmark custom-pointer"></i>
                    </button>
                </form>
            </dialog>
      `;
        errorsDiv.innerHTML = html;
    } else {
        // If there arno no errors clear message
        errorsDiv.textContent = '';
    }
});

// Handle Form Submit 
let form = document.getElementById('payment-form');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    let submitButton = document.getElementById('submit-button');
    submitButton.setAttribute('disabled', true);
    // Confirm the card payment with Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        let errorsDiv = document.getElementById('card-errors');
        // If there is an error, display it in the #card-errors div
        if (result.error) {
            let html = `
                <dialog open>
                    <form method="dialog">
                        ${result.error.message}
                        <button class="custom-pointer">
                            <i class="fa-solid fa-xmark custom-pointer"></i>
                        </button>
                    </form>
                </dialog>
          `;
            errorsDiv.innerHTML = html;
            card.update({ 'disabled': false });
            submitButton.setAttribute('disabled', false);
        } else {
            // If there are no errors and the payment is successful
            if (result.paymentIntent.status === 'succeeded') {
                // Create hidden input elements for the payment id and order id and append them to the form
                let hiddenInput = document.createElement('input');
                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'payment_id');
                hiddenInput.setAttribute('value', result.paymentIntent.id);
                let statusInput = document.createElement('input');
                statusInput.setAttribute('type', 'hidden');
                statusInput.setAttribute('name', 'status');
                statusInput.setAttribute('value', result.paymentIntent.status);
                let orderIdInput = document.createElement('input');
                orderIdInput.setAttribute('type', 'hidden');
                orderIdInput.setAttribute('name', 'order_id');
                orderIdInput.setAttribute('value', orderId);
                form.appendChild(hiddenInput);
                form.appendChild(statusInput);
                form.appendChild(orderIdInput);
                form.submit();
            }
        }
    });
});