<template>
  <meta charset="UTF-8" />
  <body>
    <b-navbar
      toggleable="sm"
      class="py-2"
      dark="true"
      style="background-color: #586994"
      sticky="true"
      fixed="top"
    >
      <b-navbar-brand style="margin: 10px" href="/"
        ><h1>HISTOLOGÍA PRÁCTICA</h1></b-navbar-brand
      >

      <b-navbar-toggle
        style="margin: 10px"
        target="nav-collapse"
      ></b-navbar-toggle>

      <!-- 
        Left aligned nav items 
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="me-auto">
          <b-nav-item class="me-auto" href="/categories">
            - Categorías</b-nav-item
          >
        </b-navbar-nav>
      </b-collapse> 
      -->

      <!-- Right aligned nav items -->
      <b-collapse id="nav-collapse" is-nav style="margin: 10px">
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
    <router-view style="margin-top: 6rem" />
  </body>
</template>

<user-info user="{{ user }}" />

<style>
@font-face {
  font-family: abel_title;
  src: url("~@/assets/fonts/Abel-Regular.ttf");
}
@font-face {
  font-family: roboto_regular;
  src: url("~@/assets/fonts/Roboto/Roboto-Regular.ttf");
}

p {
  font-family: roboto_regular;
}

h1 {
  font-family: abel_title;
}

h2 {
  font-family: abel_title;
}

h3 {
  font-family: abel_title;
}

h4 {
  font-family: abel_title;
}
</style>

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
        console.log("Getting user authentication...");
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
