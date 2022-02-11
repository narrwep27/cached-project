<template>
    <div class="nav-comp">
        <router-link to="/expenselist" class="nav-link">Expenses</router-link>
        <router-link to="/analysis" class="nav-link">Analysis</router-link>
        <router-link to="/goal" class="nav-link">Goals</router-link>
        <button class="nav-logout" v-on:click="logout">Logout</button>
    </div>
</template>

<script>
export default {
    name: 'Nav'
}
</script>

<style scoped>
    .nav-comp {
        display: flex;
        background-color: white;
        border-bottom: 1px solid #9db7d1;
        justify-content: space-evenly;
        align-items: center;
        padding: 8px;
    }
    .nav-link {
        text-decoration: none;
        transition: 100ms;
    }
    .nav-link:hover, .nav-link.router-link-active {
        border-bottom: 3px solid darkgreen;
    }
    .nav-logout {
        font-size: 14px;
        margin: 0 0 0 60em;
    }
    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
    .fade-enter-active, .fade-leave-active {
        transition: opacity 500ms ease-out;
    }
</style>