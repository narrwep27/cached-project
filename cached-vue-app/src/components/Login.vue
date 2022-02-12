<template>
    <div class="login-comp">
        <h1>Cached.</h1>
        <h3>The budgeting tool</h3>
        <form class="login-form" v-on:submit.prevent="handleLogin">
            <h2>Log in here</h2>
            <label>Email:</label>
            <input type="email" placeholder="Email" v-model="email" />
            <label>Password:</label>
            <input type="password" placeholder="Password" v-model="password" />
            <button>Log in!</button>
            <a
                v-on:click.prevent="$emit('toggleForm')" 
                href="">
                Or <b>Sign up</b> if you want to make a new account
            </a>
        </form>
    </div>
</template>

<script>
import { Login } from '../services/CustomUser';

export default {
    name: 'Login',
    data: () => ({
        email: '',
        password: ''
    }),
    methods: {
        async handleLogin() {
            if (this.email && this.password) {
                const res = await Login({
                    email: this.email,
                    password: this.password
                });
                if (res.user_id) {
                    this.$store.commit('setUser', {userId: res.user_id, auth: true});
                    this.$router.push('/expenselist')
                } else {
                    this.errorWrongCreds(res.detail);
                }
            } else {
                this.errorMissingFields()
            }
        },
        errorMissingFields() {
            this.$snackbar.add({
                type: 'error',
                text: 'All fields must be filled to log in.'
            })
        },
        errorWrongCreds(message) {
            this.$snackbar.add({
                type: 'error',
                text: message
            })
        }
    }
}
</script>

<style scoped>
    .login-form {
        width: 30%;
    }
    .login-form h2 {
        margin-top: 0;
    }
    .login-form button {
        margin: 1em auto;
        width: 60%;
    }
</style>