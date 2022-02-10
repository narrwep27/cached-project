<template>
    <div>
        <Signup v-if="formState === 'signup'" />
        <Login v-else-if="formState === 'login'" />
    </div>
</template>

<script>
import Signup from '../components/Signup.vue';
import Login from '../components/Login.vue';

export default {
    name: 'Home',
    components: { Signup, Login },
    data: () => ({
        formState: 'signup'
    }),
    methods: {
        toggleForm() {}
    }
}
</script>