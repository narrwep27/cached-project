<template>
    <div>
        <h1>Home page</h1>
        <Signup />
        <Login />
    </div>
</template>

<script>
import Signup from '../components/Signup.vue';
import Login from '../components/Login.vue';

export default {
    name: 'Home',
    components: { Signup, Login }
}
</script>