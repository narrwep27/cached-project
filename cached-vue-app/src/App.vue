<template>
  <div>
    <h1>Cached.</h1>
    <h3>The budgeting tool</h3>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App'
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
    border: 1px solid black;
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
</style>