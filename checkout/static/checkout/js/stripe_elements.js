/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
    - Through Code Institute walkthrough
*/

/* get client secret and public key from template, remove quotes */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
/* create instance of stripe elements */
var elements = stripe.elements();

/* create styles for card element */
var style = {
    base: {
        color: '#000',
        fontFamily: '"Source Serif Pro", serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
/* create card element and attach styles */
var card = elements.create('card', {style: style});
/* mount to div in checkout.html */
card.mount('#stripe-card-element');