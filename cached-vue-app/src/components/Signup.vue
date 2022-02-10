<template>
    <div class="signup-comp">
        <h1>cached.</h1>
        <form class="signup-form">
            <h2>Signup Here</h2>
            <label>Email:</label>
            <input type="email" placeholder="email" v-model="email" />
            <label>Password:</label>
            <input type="password" placeholder="password" v-model="password" />
            <label>Re-enter password:</label>
            <input type="password" placeholder="Re-enter password" v-model="reEntry" />
            <button type="submit">Sign Up!</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Signup',
    data: () => ({
        email: '',
        password: '',
        reEntry: ''
    }),
    methods: {
        handleSubmit() {}
    }
}
</script>

<style scoped>
    .signup-form {
        display: flex;
        flex-direction: column;
        margin: 0 auto;
        padding: 1.5em;
        width: 30%;
        border: 1px solid black;
        border-radius: 1em;
    }
    .signup-form label {
        text-align: left;
    }
    .signup-form button {
        margin: 1em auto;
        width: 60%;
    }
</style>