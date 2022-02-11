<template>
    <div>
        <Signup v-if="formState === 'signup'" v-on:toggleForm="toggleForm" />
        <Login 
            v-else-if="formState === 'login'" 
            v-on:toggleForm="toggleForm"
            v-on:setUser="setUser"
        />
    </div>
</template>

<script>
import Signup from '../components/Signup.vue';
import Login from '../components/Login.vue';

export default {
    name: 'Home',
    components: { Signup, Login },
    data: () => ({
        formState: 'signup',
        user: null,
        auth: false
    }),
    methods: {
        toggleForm() {
            this.formState === 'signup' 
                ? this.formState = 'login' 
                : this.formState = 'signup'
        },
        setUser(userId, auth) {
            this.user = userId,
            this.auth = auth
        }
    }
}
</script>