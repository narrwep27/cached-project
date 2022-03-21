<template>
  <div>
    <div class="nav-div" v-if="$store.state.auth">
        <router-link to="/expenselist" class="nav-link">Expenses</router-link>
        <router-link to="/analysis" class="nav-link">Analysis</router-link>
        <router-link to="/goal" class="nav-link">Goals</router-link>
        <p>Hi, {{ $store.state.email }}</p>
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
import { VerifyToken, LoadUser } from './services/CustomUser';

export default {
  name: 'App',
  components: {},
  async beforeMount() {
    await this.checkUser();
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
    logout() {
      localStorage.removeItem('userId');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      this.$store.commit('clearUser');
      this.$router.push('/');
      this.infoLogout();
    },
    infoLogout() {
      this.$snackbar.add({
        type: 'info',
        text: 'You have been logged out.'
      })
    }
  }
}
</script>

<style>
  body {
    margin: 0;
    padding: 0 0 2em 0;
    background-image: url('./assets/18410.jpg');
    background-size: 100vw;
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
    border-radius: 8px;
    background-color: white;
  }
  form label {
    text-align: left;
    font-weight: 500;
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
    font-family: Avenir, Helvetica, Arial, sans-serif;
    font-size: 14px;
  }
  input[type="date"],
  input[type="month"] {
    font-family: Avenir, Helvetica, Arial, sans-serif;
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
      border-bottom: 4px solid transparent;
      text-decoration: none;
      transition: 250ms;
  }
  .nav-link:hover, .nav-link.router-link-active {
      border-bottom: 4px solid darkgreen;
  }
  .nav-div p {
    margin: 0 0 0 45em;
  }
  .nav-logout {
      font-size: 14px;
  }

  .fade-enter-from, .fade-leave-to {
      opacity: 0;
  }
  .fade-enter-active, .fade-leave-active {
      transition: opacity 300ms ease-out;
  }
</style>