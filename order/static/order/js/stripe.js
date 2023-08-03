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