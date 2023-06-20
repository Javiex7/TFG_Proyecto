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
      <b-navbar-brand href="/" style="padding: 1rem; margin: 0px">
        <h2 class="align-bottom" style="margin: 0px">
          <a class="title-a">
            <i class="bi bi-fingerprint"></i> HISTOLOGÍA PRÁCTICA
          </a>
        </h2>
      </b-navbar-brand>

      <b-navbar-toggle
        style="margin: 0.5rem"
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
          <b-col class="text-start">
            <b-button
              v-if="userProfile"
              type="link"
              href="/profile"
              variant="primary"
              >{{ userProfile.userName }}
            </b-button>

            <b-badge
              style="margin: 0.5rem"
              class="highlightText"
              v-if="userProfile"
              variant="dark"
              pill
            >
              {{ userProfile.points }} Puntos <i class="bi bi-stars"></i>
            </b-badge>

            <b-button
              v-else
              class="me-auto"
              type="link"
              href="/login"
              variant="primary"
              >Inicio de sesión</b-button
            >
          </b-col>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view style="margin-top: 4.75rem" />
  </body>
</template>

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

h5 {
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
      userName: null,
      userProfile: null,
    };
  },

  methods: {
    checkUser() {
      const path = Constants.AUTH_URL + "users/me/";

      if (this.$store.state.isAuthenticated) {
        axios
          .get(path, {
            headers: {
              Authorization: "Token " + localStorage.getItem("token"),
            },
          })
          .then(() => {
            this.getProfile();
          })
          .catch((error) => {
            console.log(error.response.data);
          });
      }
    },

    getProfile() {
      const path = Constants.API_URL + "profiles/getProfile/";

      const headers = {
        Authorization: "Token " + this.$store.state.token,
      };

      axios
        .get(path, { headers })
        .then((response) => {
          this.userProfile = response.data;
          const updatedProfile = {
            userName: this.userProfile.user.email,
            points: this.userProfile.points,
            isUpdated: true,
          };
          localStorage.setItem("profile", JSON.stringify(updatedProfile));
          this.userProfile = JSON.parse(localStorage.getItem("profile"));
        })
        .catch((error) => {
          console.log(error);
          localStorage.clear();
          this.$router.go();
        });
    },

    updateUserInfo() {
      if (this.$store.state.isAuthenticated && this.userProfile)
        return this.performUserUpdate();
    },

    performUserUpdate() {
      this.getProfile();
      this.userProfile = JSON.parse(localStorage.getItem("profile"));
      return this.userProfile;
    },
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
    this.userProfile = JSON.parse(localStorage.getItem("profile"));
    if (this.$store.state.isAuthenticated && this.userProfile) {
      if (!this.userProfile.isUpdated) {
        // Logged user without profile data
        this.performUserUpdate();
      }
    } else {
      localStorage.clear();
    }
  },

  watch: {
    "$store.state.token": function () {
      this.userProfile = JSON.parse(localStorage.getItem("profile"));
      this.checkUser();
    },
  },
};
</script>
