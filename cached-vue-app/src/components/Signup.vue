<template>
    <div class="signup-comp">
        <form v-on:submit.prevent='handleSubmit' class="signup-form">
            <h2>Sign up here</h2>
            <label>Email:</label>
            <input type="email" placeholder="Email" v-model="email" />
            <label>Password:</label>
            <input type="password" placeholder="Password" v-model="password" />
            <label>Re-enter password:</label>
            <input type="password" placeholder="Re-enter password" v-model="reEntry" />
            <div class="password-check" v-if='!password && !reEntry'>
                <CheckboxBlankCircleOutline />
                <p>Passwords must match</p>
            </div>
            <div v-else>
                <div class="password-check match" v-if="password === reEntry">
                    <CheckCircleOutline />
                    <p>Passwords must match</p>
                </div>
                <div class="password-check mismatch" v-else>
                    <AlertCircleOutline />
                    <p>Passwords must match</p>
                </div>
            </div>
            <button type="submit">Sign Up!</button>
            <a 
                v-on:click.prevent="$emit('toggleForm')" 
                href=''>
                Or <b>Login</b> if you already have an account
            </a>
        </form>
    </div>
</template>

<script>
import CheckCircleOutline from 'vue-material-design-icons/CheckCircleOutline.vue';
import AlertCircleOutline from 'vue-material-design-icons/AlertCircleOutline.vue';
import CheckboxBlankCircleOutline from 'vue-material-design-icons/CheckboxBlankCircleOutline.vue';

export default {
    name: 'Signup',
    data: () => ({
        email: '',
        password: '',
        reEntry: ''
    }),
    components: {
        CheckCircleOutline,
        AlertCircleOutline,
        CheckboxBlankCircleOutline
    },
    methods: {
        handleSubmit() {
            if (this.email && this.password && this.reEntry) {
                if (this.password === this.reEntry) {
                    this.successSignup();
                } else {
                    this.errorMismatch();
                }
            } else {
                this.errorMissingFields();
            }
        },
        successSignup() {
            this.$snackbar.add({
                type: 'success',
                title: 'Signed up!',
                text: 'Please, log in to access your account'
            })
        },
        errorMissingFields() {
            this.$snackbar.add({
                type: 'error',
                title: 'Error',
                text: 'All fields must be filled'
            })
        },
        errorMismatch() {
            this.$snackbar.add({
                type: 'error',
                title: 'Error',
                text: 'Passwords do not match'
            })
        }
    }
}
</script>

<style scoped>
    .signup-form {
        width: 30%;
    }
    .signup-form h2 {
        margin-top: 0;
    }
    .signup-form button {
        margin: 1em auto;
        width: 60%;
    }
    .password-check {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 5px;
        text-decoration: underline;
    }
    .password-check.match {
        text-decoration: underline;
        color: green;
    }
    .password-check.mismatch {
        text-decoration: underline;
        color: red;
    }
</style>