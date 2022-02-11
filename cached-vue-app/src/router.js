import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import About from './pages/About.vue';
import NotFound from './pages/NotFound.vue';

const routes = [
    { path: '/home', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/:catchAll(.*)', component: NotFound, name: 'NotFound' }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;