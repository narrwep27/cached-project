import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { SnackbarService, Vue3Snackbar } from 'vue3-snackbar';
import "vue3-snackbar/dist/style.css";

const app = createApp(App);
app.use(router);
app.use(SnackbarService);
app.component('Vue3Snackbar', Vue3Snackbar);
app.mount('#app');
