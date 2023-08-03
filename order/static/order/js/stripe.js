// Stripe
let stripe_public_key = document.getElementById('id_stripe_public_key');
stripe_public_key = stripe_public_key.textContent.trim().slice(1, -1);

let stripe_client_secret = document.getElementById('id_client_secret');
stripe_client_secret = stripe_client_secret.textContent.trim().slice(1, -1);


let stripe = Stripe(stripe_public_key);

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
        // let html = `
        // <span class="stripe" role="alert">
        // <i class="fas fa-times"></i>
        // </span>
        // <span>${event.error.message}</span>`;
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