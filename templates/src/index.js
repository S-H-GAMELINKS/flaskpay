import Vue from 'vue';
import Checkout from '../components/Checkout.vue';

const app = new Vue({
    el: '#app',
    components: {
        'payjp-checkout': Checkout
    }
});