import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home.vue';
import About from './pages/About.vue';
import ExpenseList from './pages/ExpenseList.vue';
import Analysis from './pages/Analysis.vue';
import Goal from './pages/Goal.vue';
import NotFound from './pages/NotFound.vue';

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/about', component: About, name: 'About' },
    { path: '/expenselist', component: ExpenseList, name: 'ExpenseList'},
    { path: '/analysis', component: Analysis, name: 'Analysis'},
    { path: '/goal', component: Goal, name: 'Goal'},
    { path: '/:catchAll(.*)*', component: NotFound, name: 'NotFound' }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;