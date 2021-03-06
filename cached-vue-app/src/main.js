import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import { SnackbarService, Vue3Snackbar } from 'vue3-snackbar';
import VueChartkick from 'vue-chartkick';
import 'chartkick/chart.js';
import "vue3-snackbar/dist/style.css";

const app = createApp(App);
app.use(router);
app.use(store);
app.use(SnackbarService);
app.use(VueChartkick);
app.component('Vue3Snackbar', Vue3Snackbar);
app.mount('#app');
