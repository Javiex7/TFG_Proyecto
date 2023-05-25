<template>
  <b-container style="padding: 1rem">
    <div>PERFIL DE USUARIO</div>
    <nav>
      <p><router-link to="/login"> Login </router-link></p>
    </nav>
  </b-container>
</template>

<script>
import axios from "axios";
import Constants from "@/constants";

export default {
  name: "HomeView",
  data: function () {
    return {
      user: null,
    };
  },
  updated() {
    const path = Constants.AUTH_URL + "users/me/";

    if (this.$store.state.isAuthenticated) {
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
    }
  },
};
</script>
