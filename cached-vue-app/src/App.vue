<template>
  <div>
    <div class="nav-div" v-if="$store.state.auth && $store.state.user">
        <router-link to="/expenselist" class="nav-link">Expenses</router-link>
        <router-link to="/analysis" class="nav-link">Analysis</router-link>
        <router-link to="/goal" class="nav-link">Goals</router-link>
        <button class="nav-logout" v-on:click="logout">Logout</button>
    </div>
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
    <Vue3Snackbar bottom right :duration="6500" />
  </div>
</template>

<script>
import { VerifyToken } from './services/CustomUser';

export default {
  name: 'App',
  components: {},
  data: () => ({}),
  async beforeMount() {
    await this.checkUser();
    console.log(this.$route)
  },
  methods: {
    async checkUser() {
      if (localStorage.getItem('accessToken')) {
        const res = await VerifyToken(localStorage.getItem('accessToken'));
        if (res.status === 200) {
          this.$store.commit('setUser', {
            userId: localStorage.getItem('userId'),
            auth: true
          });
          this.$router.push('/expenselist')
        }
      }
    },
    logout() {
      localStorage.removeItem('userId');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      this.$store.commit('clearUser');
      this.$router.push('/home');
    }
  }
}
</script>

<style>
  body {
    margin: 0;
    padding: 0 0 2em 0;
    background-image: url('./assets/18410.jpg');
    background-size:cover;
  }
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin: 0;
  }
  form {
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    padding: 1.5em;
    border: 1px solid #2c3e50;
    border-radius: 1em;
    background-color: white;
  }
  form label {
    text-align: left;
  }
  button {
    cursor: pointer;
    padding: .5em;
    background-color: white;
    font-weight: bold;
    font-size: 16px;
    border-radius: 10px;
    border: 2px solid #2c3e50;
    transition: 500ms;
  }
  button:hover {
    color: white;
    background-color: #2c3e50;
  }
  input {
    margin: .5em 0 1em 0;
    border-top-style: none;
    border-left-style: none;
    border-right-style: none;
    border-bottom: 1px solid gray;
    font-size: 14px;
  }
  input:focus {
    outline: none;
  }
  input::placeholder {
    font-size: 14px;
  }
  a {
    color: black
  }
  a:visited {
    color: black;
  }

  .nav-div {
    display: flex;
    background-color: white;
    border-bottom: 1px solid #9db7d1;
    justify-content: space-evenly;
    align-items: center;
    padding: 8px;
  }
  .nav-link {
      text-decoration: none;
      transition: 150ms;
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
      transition: opacity 300ms ease-out;
  }
</style>