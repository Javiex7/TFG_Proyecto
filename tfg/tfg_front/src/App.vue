<template>
  <b-navbar toggleable dark="true" variant="dark">
    <b-navbar-brand href="/"> TFG </b-navbar-brand>

    <b-navbar-toggle target="navbar-toggle-collapse"> </b-navbar-toggle>

    <b-collapse id="navbar-toggle-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/categories">Categorías</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <router-view />
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authoritation"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authoritation"] = "";
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
