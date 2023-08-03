// Stripe
let stripePublicKey = document.getElementById('id_stripe_public_key');
stripePublicKey = stripePublicKey.textContent.trim().slice(1, -1);

let clientSecret = document.getElementById('id_client_secret');
console.log(clientSecret)

clientSecret = clientSecret.textContent.trim().slice(1, -1);
console.log(clientSecret)

let stripe = Stripe(stripePublicKey);

let elements = stripe.elements();

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
let card = elements.create('card', {style: style});

card.mount('#card-element');


// Handle validation errors
card.addEventListener('change', (event) => {
    let errorsDiv = document.getElementById('card-errors');
    if(event.error) {
        let html = `
            <dialog open>
                <form method="dialog">
                    ${event.error.message}
                    <button class="custom-pointer">
                        <i class="fa-solid fa-xmark custom-pointer"></i>
                    </button>
                </form>
            </dialog>
      `
        errorsDiv.innerHTML = html;
    } else {
        errorsDiv.textContent = '';
    }
})

// Handle Form Submit 
let form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    let submitButton = document.getElementById('submit-button');
    submitButton.setAttribute('disabled', true);
    console.log(clientSecret)
    // Confirm the card payment with Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        let errorsDiv = document.getElementById('card-errors');
        // If there is an error, display it in the 'card-errors'
        if(result.error) {
            let html = `
                <dialog open>
                    <form method="dialog">
                        ${result.error.message}
                        <button class="custom-pointer">
                            <i class="fa-solid fa-xmark custom-pointer"></i>
                        </button>
                    </form>
                </dialog>
          `
            errorsDiv.innerHTML = html;
            card.update({ 'disabled': false});
            submitButton.setAttribute('disabled', false);
        } else {
            // If there are no errors and the payment is successful
            if (result.paymentIntent.status === 'succeeded') {
                console.log(result);
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