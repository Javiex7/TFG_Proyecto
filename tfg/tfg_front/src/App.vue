<template>
  <meta charset="UTF-8" />
  <body>
    <b-navbar
      toggleable="sm"
      class="py-3"
      dark="true"
      style="background-color: #4b71aa"
    >
      <b-navbar-brand href="/"><h1>TFG</h1></b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <!-- Left aligned nav items -->
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="me-auto">
          <b-nav-item class="me-auto" href="/categories">
            - Categorías</b-nav-item
          >
        </b-navbar-nav>
      </b-collapse>

      <!-- Right aligned nav items -->
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ms-auto">
          <b-button
            v-if="user"
            class="me-auto"
            type="link"
            href="/profile"
            variant="primary"
            >{{ user.email }}</b-button
          >
          <b-button
            v-if="!user"
            class="me-auto"
            type="link"
            href="/login"
            variant="primary"
            >Inicio de sesión</b-button
          >
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view />
  </body>
</template>

<user-info user="{{ user }}" />

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  name: "App",
  data: function () {
    return {
      user: null,
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authoritation"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authoritation"] = "";
    }
  },

  created() {
    this.check_user();
  },

  watch: {
    "$store.state.token": function () {
      this.check_user();
    },
  },

  methods: {
    check_user: function () {
      const path = Constants.AUTH_URL + "users/me/";

      if (this.$store.state.isAuthenticated) {
        console.log("CARGANDO...");
        axios
          .get(path, {
            headers: {
              Authorization: "Token " + localStorage.getItem("token"),
            },
          })
          .then((response) => {
            this.user = response.data;
            console.log(this.user);
          })
          .catch((error) => {
            console.log(error.response.data);
          });
      } else {
        this.user = null;
      }
    },
  },
};
</script>
