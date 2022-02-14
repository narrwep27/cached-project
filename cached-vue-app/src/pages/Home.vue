<template>
    <div class="page home-comp">
        <div>
            <Signup v-if="formState === 'signup'" v-on:toggleForm="toggleForm" />
            <Login v-else-if="formState === 'login'" v-on:toggleForm="toggleForm" />
        </div>
    </div>
</template>

<script>
import { VerifyToken, LoadUser } from '../services/CustomUser';
import Signup from '../components/Signup.vue';
import Login from '../components/Login.vue';

export default {
    name: 'Home',
    components: { Signup, Login },
    data: () => ({
        formState: 'signup',
    }),
    async beforeMount() {
        this.checkUser();
    },
    methods: {
    async checkUser() {
      if (localStorage.getItem('accessToken')) {
        const res = await VerifyToken(localStorage.getItem('accessToken'));
        if (res.status === 200) {
          const user = await LoadUser(localStorage.getItem('userId'))
          this.$store.commit('setUser', {
            auth: true,
            userObj: user
          });
          this.$router.push('/expenselist')
        }
      }
    },
        toggleForm() {
            this.formState === 'signup' 
                ? this.formState = 'login' 
                : this.formState = 'signup'
        }
    }
}
</script>